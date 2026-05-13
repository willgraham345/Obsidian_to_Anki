"""Tests for scan.py helper functions (vault-independent)."""

import os
import sys

import pytest
import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from src.obsidian_to_anki.db import NoteDB

# Import the function under test directly from scan.py (not a package module)
_SCAN_PATH = os.path.join(os.path.dirname(__file__), "..", "scan.py")
import importlib.util as _ilu

_spec = _ilu.spec_from_file_location("scan", _SCAN_PATH)
_scan_mod = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_scan_mod)  # type: ignore

add_atomic_id = _scan_mod.add_atomic_id
find_vault_modifications = _scan_mod.find_vault_modifications


@pytest.fixture
def db():
    instance = NoteDB(":memory:")
    yield instance
    instance.close()


class TestAddAtomicId:

    def test_creates_frontmatter_when_absent(self, tmp_path, db):
        f = tmp_path / "note.md"
        f.write_text("# Hello\n\nsome content\n", encoding="utf-8")
        atomic_id = add_atomic_id(str(f), db)
        content = f.read_text(encoding="utf-8")
        assert content.startswith("---\n")
        assert "atomic_id:" in content
        assert atomic_id in content

    def test_stores_atomic_id_in_db(self, tmp_path, db):
        f = tmp_path / "note.md"
        f.write_text("# Hello\n", encoding="utf-8")
        atomic_id = add_atomic_id(str(f), db)
        assert db.get_file_atomic_id(str(f)) == atomic_id

    def test_idempotent_same_uuid_on_second_call(self, tmp_path, db):
        f = tmp_path / "note.md"
        f.write_text("# Hello\n", encoding="utf-8")
        first = add_atomic_id(str(f), db)
        second = add_atomic_id(str(f), db)
        assert first == second

    def test_does_not_rewrite_file_when_id_present(self, tmp_path, db):
        f = tmp_path / "note.md"
        f.write_text("---\natomic_id: existing-id\n---\n# Body\n", encoding="utf-8")
        mtime_before = f.stat().st_mtime
        add_atomic_id(str(f), db)
        mtime_after = f.stat().st_mtime
        assert mtime_before == mtime_after

    def test_preserves_existing_frontmatter_keys(self, tmp_path, db):
        f = tmp_path / "note.md"
        f.write_text("---\ntitle: My Note\ntags: [foo]\n---\n# Body\n", encoding="utf-8")
        add_atomic_id(str(f), db)
        content = f.read_text(encoding="utf-8")
        # Parse frontmatter
        fm_block = content.split("---\n")[1]
        fm = yaml.safe_load(fm_block)
        assert fm.get("title") == "My Note"
        assert fm.get("tags") == ["foo"]
        assert "atomic_id" in fm

    def test_preserves_file_body(self, tmp_path, db):
        body = "# My Note\n\nSome content here.\n"
        f = tmp_path / "note.md"
        f.write_text(body, encoding="utf-8")
        add_atomic_id(str(f), db)
        content = f.read_text(encoding="utf-8")
        assert body in content


class TestFindVaultModifications:

    def _make_note(self, db, uuid, file_path, line_number=1):
        db.upsert_note(
            uuid=uuid,
            anki_id=None,
            file_path=file_path,
            line_number=line_number,
            note_type="Basic",
            field_1="Front",
            field_2="Back",
            image_paths=[],
            tags=[],
            deck_name="Default",
        )

    def test_marks_missing_file_as_stale(self, tmp_path, db):
        self._make_note(db, "n-1", "gone.md")
        abs_r, stale_r = find_vault_modifications(db, str(tmp_path))
        assert stale_r == 1
        assert db.get_note("n-1")["state"] == "stale"

    def test_existing_file_not_marked_stale(self, tmp_path, db):
        f = tmp_path / "alive.md"
        f.write_text("content", encoding="utf-8")
        self._make_note(db, "n-1", "alive.md")
        _, stale_r = find_vault_modifications(db, str(tmp_path))
        assert stale_r == 0
        assert db.get_note("n-1")["state"] == "unknown"

    def test_removes_absolute_path_contamination(self, tmp_path, db):
        self._make_note(db, "n-1", "/absolute/path/note.md")
        abs_r, _ = find_vault_modifications(db, str(tmp_path))
        assert abs_r == 1
        assert db.get_note("n-1") is None
