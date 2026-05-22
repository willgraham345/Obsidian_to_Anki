"""Tests for scan.py helper functions (vault-independent)."""

import os
import sys

import pytest
import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from src.atomics.db import NoteDB

# Import the function under test directly from scan.py (not a package module)
_SCAN_PATH = os.path.join(os.path.dirname(__file__), "..", "scan.py")
import importlib.util as _ilu

_spec = _ilu.spec_from_file_location("scan", _SCAN_PATH)
_scan_mod = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_scan_mod)  # type: ignore

add_atomic_id = _scan_mod.add_atomic_id
find_vault_modifications = _scan_mod.find_vault_modifications
_read_frontmatter_sync = _scan_mod._read_frontmatter_sync
run_vault_scan = _scan_mod.run_vault_scan


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

    def test_empty_db_returns_zero_zero(self, tmp_path, db):
        abs_r, stale_r = find_vault_modifications(db, str(tmp_path))
        assert abs_r == 0
        assert stale_r == 0

    def test_already_stale_not_recounted(self, tmp_path, db):
        self._make_note(db, "n-1", "gone.md")
        db.set_state_and_action("n-1", "stale", "review")
        _, stale_r = find_vault_modifications(db, str(tmp_path))
        assert stale_r == 0

    def test_mixed_existing_and_missing(self, tmp_path, db):
        alive = tmp_path / "alive.md"
        alive.write_text("content", encoding="utf-8")
        self._make_note(db, "n-1", "alive.md")
        self._make_note(db, "n-2", "gone.md")
        _, stale_r = find_vault_modifications(db, str(tmp_path))
        assert stale_r == 1
        assert db.get_note("n-1")["state"] == "unknown"
        assert db.get_note("n-2")["state"] == "stale"

    def test_returns_abs_and_stale_independently(self, tmp_path, db):
        self._make_note(db, "n-1", "/absolute/path/note.md")
        self._make_note(db, "n-2", "gone.md")
        abs_r, stale_r = find_vault_modifications(db, str(tmp_path))
        assert abs_r == 1
        assert stale_r == 1


class TestReadFrontmatterSync:

    def test_returns_anki_sync_dict(self, tmp_path):
        f = tmp_path / "note.md"
        f.write_text("---\nanki_sync:\n  uuid-1: 1234\n  uuid-2: 5678\n---\n# Body\n", encoding="utf-8")
        result = _read_frontmatter_sync(str(f))
        assert result == {"uuid-1": 1234, "uuid-2": 5678}

    def test_no_frontmatter_returns_empty(self, tmp_path):
        f = tmp_path / "note.md"
        f.write_text("# Just a heading\n", encoding="utf-8")
        assert _read_frontmatter_sync(str(f)) == {}

    def test_missing_anki_sync_key_returns_empty(self, tmp_path):
        f = tmp_path / "note.md"
        f.write_text("---\ntitle: My Note\n---\n# Body\n", encoding="utf-8")
        assert _read_frontmatter_sync(str(f)) == {}

    def test_missing_file_returns_empty(self, tmp_path):
        assert _read_frontmatter_sync(str(tmp_path / "nonexistent.md")) == {}

    def test_invalid_yaml_returns_empty(self, tmp_path):
        f = tmp_path / "note.md"
        f.write_text("---\n: bad: yaml: [\n---\n# Body\n", encoding="utf-8")
        assert _read_frontmatter_sync(str(f)) == {}

    def test_empty_anki_sync_returns_empty(self, tmp_path):
        f = tmp_path / "note.md"
        f.write_text("---\nanki_sync: {}\n---\n# Body\n", encoding="utf-8")
        assert _read_frontmatter_sync(str(f)) == {}


import hashlib
import re

# globals module as seen by scan.py (may differ from src.atomics.globals)
_scan_globals = _scan_mod.globals


# Files used in hashing tests always include atomic_id upfront so add_atomic_id
# is a no-op — keeps the on-disk hash stable across scans.
_FM = "---\natomic_id: {aid}\n---\n"


def _md(path, name="note.md", aid="test-aid", body="# Hello\n"):
    f = path / name
    f.write_text(_FM.format(aid=aid) + body, encoding="utf-8")
    return f


class TestRunVaultScanHashing:

    @pytest.fixture(autouse=True)
    def setup_globals(self):
        _scan_globals.CONFIG_DATA = {
            "Vault": "",
            "DECK_LINE": "TARGET DECK",
            "TAG_LINE": "FILE TAGS",
            "NOTE_PREFIX": "START",
            "NOTE_SUFFIX": "END",
            "FROZEN_LINE": "FROZEN",
            "INLINE_PREFIX": "STARTI",
            "INLINE_SUFFIX": "ENDI",
            "Comment": False,
            "ATOMICS": {},
            "FOLDER_DECKS": [],
        }
        _scan_globals.VAULT_PATH_REGEXP = re.compile(r"^$")
        _scan_globals.DECK_REGEXP = re.compile(r"^TARGET DECK(?:\n|: )(.*)", re.MULTILINE)
        _scan_globals.TAG_REGEXP = re.compile(r"^FILE TAGS(?:\n|: )(.*)", re.MULTILINE)
        _scan_globals.NOTE_REGEXP = re.compile(r"^START.*?\n([\s\S]*?\n)END\n?", re.MULTILINE)
        _scan_globals.EMPTY_REGEXP = re.compile(r"^START\n(?:<!--)?ID: [\s\S]*?\nEND", re.MULTILINE)
        _scan_globals.INLINE_REGEXP = re.compile(r"STARTI(.*?)ENDI")
        _scan_globals.INLINE_EMPTY_REGEXP = re.compile(r"STARTI\s+(?:<!--)?ID: .*?ENDI")
        _scan_globals.FROZEN_REGEXP = re.compile(r"FROZEN - (.*?):\n((?:[^\n][\n]?)+)")
        _scan_globals.EXISTING_IDS = []
        _scan_globals.FIELDS_DICT = {}
        _scan_globals.NOTE_DICT_TEMPLATE = {"tags": [], "deckName": "Default"}
        _scan_globals.NOTE_DB = None
        yield

    @pytest.fixture
    def db(self):
        instance = NoteDB(":memory:")
        yield instance
        instance.close()

    def test_new_file_hash_stored_after_scan(self, tmp_path, db):
        f = _md(tmp_path)
        run_vault_scan(str(tmp_path), db)
        assert db.get_file_hash(str(f)) is not None

    def test_correct_hash_value_stored(self, tmp_path, db):
        f = _md(tmp_path)
        run_vault_scan(str(tmp_path), db)
        expected = hashlib.sha256(f.read_bytes()).hexdigest()
        assert db.get_file_hash(str(f)) == expected

    def test_unchanged_file_skipped_on_second_scan(self, tmp_path, db, capsys):
        _md(tmp_path)
        run_vault_scan(str(tmp_path), db)
        capsys.readouterr()
        run_vault_scan(str(tmp_path), db)
        assert "1 skipped" in capsys.readouterr().out

    def test_changed_file_rescanned(self, tmp_path, db, capsys):
        f = _md(tmp_path)
        run_vault_scan(str(tmp_path), db)
        f.write_text(_FM.format(aid="test-aid") + "# Modified\n", encoding="utf-8")
        capsys.readouterr()
        run_vault_scan(str(tmp_path), db)
        assert "skipped" not in capsys.readouterr().out

    def test_wrong_stored_hash_triggers_rescan(self, tmp_path, db):
        content = _FM.format(aid="test-aid") + "# Hello\n"
        f = tmp_path / "note.md"
        f.write_text(content, encoding="utf-8")
        db.set_file_hash(str(f), "wrong-hash")
        run_vault_scan(str(tmp_path), db)
        expected = hashlib.sha256(content.encode()).hexdigest()
        assert db.get_file_hash(str(f)) == expected

    def test_force_rescans_despite_matching_hash(self, tmp_path, db, capsys):
        _md(tmp_path)
        run_vault_scan(str(tmp_path), db)
        capsys.readouterr()
        run_vault_scan(str(tmp_path), db, force=True)
        assert "skipped" not in capsys.readouterr().out

    def test_multiple_files_one_skipped_one_rescanned(self, tmp_path, db, capsys):
        _md(tmp_path, name="a.md", aid="aid-a")
        f2 = _md(tmp_path, name="b.md", aid="aid-b")
        run_vault_scan(str(tmp_path), db)
        f2.write_text(_FM.format(aid="aid-b") + "# Modified\n", encoding="utf-8")
        capsys.readouterr()
        run_vault_scan(str(tmp_path), db)
        assert "1 skipped" in capsys.readouterr().out

    def test_non_md_files_not_hashed(self, tmp_path, db):
        f = tmp_path / "note.txt"
        f.write_text("content", encoding="utf-8")
        run_vault_scan(str(tmp_path), db)
        assert db.get_file_hash(str(f)) is None

    def test_hidden_dirs_not_scanned(self, tmp_path, db):
        hidden = tmp_path / ".hidden"
        hidden.mkdir()
        f = hidden / "note.md"
        f.write_text("# Hidden\n", encoding="utf-8")
        run_vault_scan(str(tmp_path), db)
        assert db.get_file_hash(str(f)) is None
