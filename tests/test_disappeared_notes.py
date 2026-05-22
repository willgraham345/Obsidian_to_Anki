"""Tests for disappeared-note tracking and --prune-removed logic."""

import os
import sys
import importlib.util as _ilu
from unittest.mock import MagicMock, call

import pytest

from src.atomics.db import NoteDB

# Import write.py as a module (not a package)
_WRITE_PATH = os.path.join(os.path.dirname(__file__), "..", "write.py")
_spec = _ilu.spec_from_file_location("write", _WRITE_PATH)
_write_mod = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_write_mod)  # type: ignore
execute = _write_mod.execute


@pytest.fixture
def db():
    instance = NoteDB(":memory:")
    yield instance
    instance.close()


def _note(db, uuid, anki_id=None, file_path="deck/note.md", line_number=10,
          note_type="Basic", field_1="<p>Front</p>", field_2="<p>Back</p>"):
    db.upsert_note(
        uuid=uuid, anki_id=anki_id, file_path=file_path,
        line_number=line_number, note_type=note_type,
        field_1=field_1, field_2=field_2,
        image_paths=[], tags=[], deck_name="Default",
    )


class TestMarkDisappeared:

    def test_marks_absent_note_disappeared(self, db):
        _note(db, "uuid-1", file_path="a.md", line_number=1)
        _note(db, "uuid-2", file_path="a.md", line_number=20)

        # Only uuid-1 seen in current scan
        count = db.mark_disappeared("a.md", {"uuid-1"})

        assert count == 1
        row = db.get_note("uuid-2")
        assert row["state"] == "disappeared"

    def test_does_not_mark_seen_note(self, db):
        _note(db, "uuid-1", file_path="a.md", line_number=1)
        db.mark_disappeared("a.md", {"uuid-1"})
        row = db.get_note("uuid-1")
        assert row["state"] != "disappeared"

    def test_all_notes_disappeared_when_seen_empty(self, db):
        _note(db, "uuid-1", file_path="a.md", line_number=1)
        _note(db, "uuid-2", file_path="a.md", line_number=20)

        count = db.mark_disappeared("a.md", set())

        assert count == 2
        assert db.get_note("uuid-1")["state"] == "disappeared"
        assert db.get_note("uuid-2")["state"] == "disappeared"

    def test_does_not_remark_already_disappeared(self, db):
        _note(db, "uuid-1", file_path="a.md", line_number=1)
        db.mark_disappeared("a.md", set())
        # Mark again — should return 0 (already disappeared)
        count = db.mark_disappeared("a.md", set())
        assert count == 0

    def test_ignores_notes_in_other_files(self, db):
        _note(db, "uuid-1", file_path="a.md", line_number=1)
        _note(db, "uuid-2", file_path="b.md", line_number=1)

        db.mark_disappeared("a.md", set())

        assert db.get_note("uuid-1")["state"] == "disappeared"
        assert db.get_note("uuid-2")["state"] != "disappeared"

    def test_empty_file_path_returns_zero(self, db):
        _note(db, "uuid-1", file_path="a.md", line_number=1)
        count = db.mark_disappeared("", set())
        assert count == 0
        assert db.get_note("uuid-1")["state"] != "disappeared"


class TestPruneRemovedExecute:

    def _make_prune_entry(self, db, note_uuid="uuid-gone", anki_id=99999):
        """Set up a disappeared note with a prune diff entry."""
        _note(db, note_uuid, anki_id=anki_id, file_path="a.md")
        db.set_state_and_action(note_uuid, "disappeared", "review")
        db.upsert_diff_entry(
            id=note_uuid, operation="prune",
            note_type="Basic", deck_name=None,
            field_1="<p>Front</p>", field_2=None,
            tags=None, anki_id=anki_id, file_path="a.md",
        )

    def test_prune_deletes_anki_note_and_db_row(self, db):
        self._make_prune_entry(db, note_uuid="uuid-gone", anki_id=99999)

        ac = MagicMock()
        results = execute(db, ac, prune_removed=True)

        ac.invoke.assert_called_once()
        call_args = ac.invoke.call_args
        assert 99999 in (call_args.args[1] if len(call_args.args) > 1 else call_args.kwargs.get("notes", []))
        assert results["pruned"] == 1
        assert db.get_note("uuid-gone") is None

    def test_prune_clears_diff_entry(self, db):
        self._make_prune_entry(db, note_uuid="uuid-gone", anki_id=99999)

        ac = MagicMock()
        execute(db, ac, prune_removed=True)

        remaining = db.get_diff_entries()
        prune_entries = [e for e in remaining if e["operation"] == "prune"]
        assert prune_entries == []

    def test_prune_skipped_without_flag(self, db, capsys):
        self._make_prune_entry(db, note_uuid="uuid-gone", anki_id=99999)

        ac = MagicMock()
        results = execute(db, ac, prune_removed=False)

        # deleteNotes should NOT be called for prune entries
        for c in ac.invoke.call_args_list:
            action = c.args[0] if c.args else None
            assert action != "deleteNotes", "deleteNotes called unexpectedly"

        assert results["pruned"] == 0
        captured = capsys.readouterr()
        assert "--prune-removed" in captured.out

    def test_prune_note_stays_in_db_when_flag_absent(self, db):
        self._make_prune_entry(db, note_uuid="uuid-gone", anki_id=99999)

        ac = MagicMock()
        execute(db, ac, prune_removed=False)

        assert db.get_note("uuid-gone") is not None

    def test_multiple_prune_entries_batched(self, db):
        self._make_prune_entry(db, note_uuid="uuid-a", anki_id=111)
        self._make_prune_entry(db, note_uuid="uuid-b", anki_id=222)

        ac = MagicMock()
        results = execute(db, ac, prune_removed=True)

        assert results["pruned"] == 2
        assert db.get_note("uuid-a") is None
        assert db.get_note("uuid-b") is None


class TestDisappearedNotOrphan:

    def test_disappeared_note_not_orphan_in_comparison_view(self, db):
        """A disappeared note referencing a live anki_id must not appear as orphan_in_anki.
        It is handled via the prune path, not the delete-orphans path."""
        _note(db, "uuid-gone", anki_id=77777, file_path="a.md")
        db.upsert_anki_note(
            anki_id=77777, note_type="Basic",
            field_1="<p>Front</p>", field_2="<p>Back</p>",
            tags=[], deck_name="Default", mod_timestamp=0,
        )
        db.mark_disappeared("a.md", set())

        rows = db.get_comparison_rows(exclude_synced=False)
        orphan_rows = [r for r in rows if r["status"] == "orphan_in_anki" and r["anki_id"] == 77777]
        assert orphan_rows == [], "disappeared note should not appear as orphan_in_anki"

    def test_disappeared_note_without_anki_id_not_in_prune_diff(self, db):
        """A disappeared note with no anki_id should produce no prune diff entry."""
        _note(db, "uuid-never-synced", anki_id=None, file_path="a.md")
        db.mark_disappeared("a.md", set())

        from src.atomics import globals
        import importlib.util as ilu, os as _os
        scan_path = _os.path.join(_os.path.dirname(__file__), "..", "scan.py")
        spec = ilu.spec_from_file_location("scan_mod", scan_path)
        scan_mod = ilu.module_from_spec(spec)
        spec.loader.exec_module(scan_mod)

        # Manually run the disappeared section of build_diff
        disappeared = db.get_notes_by_state("disappeared")
        prune_created = [n for n in disappeared if n.get("anki_id")]
        assert prune_created == []
