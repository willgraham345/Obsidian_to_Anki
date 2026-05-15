"""Tests for build_diff / _plain — HTML-only diff filtering (functions now live in scan.py)."""

import os
import sys
import importlib.util as _ilu

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from src.atomics.db import NoteDB

_SCAN_PATH = os.path.join(os.path.dirname(__file__), "..", "scan.py")
_spec = _ilu.spec_from_file_location("scan", _SCAN_PATH)
_scan_mod = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_scan_mod)  # type: ignore

build_diff = _scan_mod.build_diff
_plain = _scan_mod._plain
_diff_globals = _scan_mod.globals


# ── _plain ────────────────────────────────────────────────────────────────────

class TestPlain:

    def test_strips_p_tags(self):
        assert _plain("<p>hello</p>") == "hello"

    def test_strips_br_tag(self):
        assert _plain("line1<br>line2") == "line1line2"

    def test_strips_bold(self):
        assert _plain("<b>bold</b>") == "bold"

    def test_none_returns_empty(self):
        assert _plain(None) == ""

    def test_plain_text_unchanged(self):
        assert _plain("no html here") == "no html here"

    def test_tag_only_content_returns_empty(self):
        assert _plain("<p></p>") == ""

    def test_nested_tags_stripped(self):
        assert _plain("<p><b>text</b></p>") == "text"

    def test_stem_suffix_stripped(self):
        assert _plain("question<br><b>FileName</b>") == "questionFileName"


# ── build_diff HTML filtering ─────────────────────────────────────────────────

class TestBuildDiffHtmlFiltering:

    @pytest.fixture(autouse=True)
    def setup_globals(self):
        _diff_globals.CONFIG_DATA = {
            "ATOMICS": {},
            "FOLDER_DECKS": [],
        }
        yield

    @pytest.fixture
    def db(self):
        instance = NoteDB(":memory:")
        yield instance
        instance.close()

    def _vault_note(self, db, uuid, anki_id, field_1, field_2,
                    note_type="Basic", file_path="notes/test.md"):
        db.upsert_note(
            uuid=uuid, anki_id=anki_id, file_path=file_path, line_number=1,
            note_type=note_type, field_1=field_1, field_2=field_2,
            image_paths=[], tags=[], deck_name="Default",
        )

    def _anki_note(self, db, anki_id, field_1, field_2, note_type="Basic"):
        db.upsert_anki_note(
            anki_id=anki_id, note_type=note_type, field_1=field_1,
            field_2=field_2, tags=[], deck_name="Default", mod_timestamp=None,
        )

    # ── HTML-only diffs must be suppressed ───────────────────────────────────

    def test_p_wrapped_field_1_excluded(self, db):
        """<p> wrapping in vault vs plain text in Anki → not in update bucket."""
        self._vault_note(db, "u1", 1001, "<p>question</p>", "answer")
        self._anki_note(db, 1001, "question", "answer")
        diff = build_diff(db, "/vault")
        assert not any(e.get("uuid") == "u1" for e in diff["update"])

    def test_p_wrapped_field_2_excluded(self, db):
        """<p> wrapping only in field_2 → not in update bucket."""
        self._vault_note(db, "u1", 1001, "question", "<p>answer</p>")
        self._anki_note(db, 1001, "question", "answer")
        diff = build_diff(db, "/vault")
        assert not any(e.get("uuid") == "u1" for e in diff["update"])

    def test_p_wrapped_both_fields_excluded(self, db):
        """<p> wrapping on both fields → not in update bucket."""
        self._vault_note(db, "u1", 1001, "<p>question</p>", "<p>answer</p>")
        self._anki_note(db, 1001, "question", "answer")
        diff = build_diff(db, "/vault")
        assert not any(e.get("uuid") == "u1" for e in diff["update"])

    def test_br_only_diff_excluded(self, db):
        """<br> tag present in vault but absent in Anki → HTML-only → excluded."""
        self._vault_note(db, "u1", 1001, "line1<br>line2", "answer")
        self._anki_note(db, 1001, "line1line2", "answer")
        diff = build_diff(db, "/vault")
        assert not any(e.get("uuid") == "u1" for e in diff["update"])

    def test_multiple_html_only_notes_all_excluded(self, db):
        """Several HTML-only diffs → none appear in update bucket."""
        for i, (vf1, af1) in enumerate([
            ("<p>q1</p>", "q1"),
            ("<p>q2</p>", "q2"),
            ("<p>q3</p>", "q3"),
        ]):
            self._vault_note(db, f"u{i}", 1000 + i, vf1, "answer",
                             file_path=f"notes/test{i}.md")
            self._anki_note(db, 1000 + i, af1, "answer")
        diff = build_diff(db, "/vault")
        assert diff["update"] == []

    # ── Real content diffs must be preserved ─────────────────────────────────

    def test_real_field_1_diff_included(self, db):
        """Content actually changed in field_1 → must appear in update bucket."""
        self._vault_note(db, "u1", 1001, "new question", "answer")
        self._anki_note(db, 1001, "old question", "answer")
        diff = build_diff(db, "/vault")
        assert any(e.get("uuid") == "u1" for e in diff["update"])

    def test_real_field_2_diff_included(self, db):
        """Content actually changed in field_2 → must appear in update bucket."""
        self._vault_note(db, "u1", 1001, "question", "new answer")
        self._anki_note(db, 1001, "question", "old answer")
        diff = build_diff(db, "/vault")
        assert any(e.get("uuid") == "u1" for e in diff["update"])

    def test_html_field_1_but_real_field_2_diff_included(self, db):
        """Field 1 HTML-only diff but field 2 actually changed → include."""
        self._vault_note(db, "u1", 1001, "<p>question</p>", "new answer")
        self._anki_note(db, 1001, "question", "old answer")
        diff = build_diff(db, "/vault")
        assert any(e.get("uuid") == "u1" for e in diff["update"])

    def test_real_field_1_diff_html_field_2_included(self, db):
        """Field 1 actually changed, field 2 HTML-only diff → include."""
        self._vault_note(db, "u1", 1001, "new question", "<p>answer</p>")
        self._anki_note(db, 1001, "old question", "answer")
        diff = build_diff(db, "/vault")
        assert any(e.get("uuid") == "u1" for e in diff["update"])

    # ── Other buckets unaffected ──────────────────────────────────────────────

    def test_synced_note_not_in_any_bucket(self, db):
        """Identical fields → absent from all diff buckets."""
        self._vault_note(db, "u1", 1001, "question", "answer")
        self._anki_note(db, 1001, "question", "answer")
        diff = build_diff(db, "/vault")
        all_entries = [e for bucket in diff.values() for e in bucket]
        assert not any(e.get("uuid") == "u1" for e in all_entries)

    def test_note_without_anki_id_goes_to_add(self, db):
        """Vault note with no anki_id → add bucket, not update."""
        self._vault_note(db, "u1", None, "question", "answer")
        diff = build_diff(db, "/vault")
        assert any(e.get("uuid") == "u1" for e in diff["add"])
        assert not any(e.get("uuid") == "u1" for e in diff["update"])
