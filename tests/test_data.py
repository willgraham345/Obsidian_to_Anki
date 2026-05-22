import pytest
from unittest.mock import patch, MagicMock, mock_open
import os
import json

from src.atomics.data import Data
from src.atomics.db import NoteDB
from src.atomics import globals


@pytest.fixture(autouse=True)
def reset_globals():
    """Reset globals and NOTE_DB before each test."""
    globals.ADDED_MEDIA = []
    globals.FILE_HASHES = {}
    prev_db = globals.NOTE_DB
    globals.NOTE_DB = None
    yield
    if globals.NOTE_DB and globals.NOTE_DB is not prev_db:
        try:
            globals.NOTE_DB.close()
        except Exception:
            pass
    globals.NOTE_DB = prev_db


def _in_memory_db():
    """Create a fresh in-memory NoteDB."""
    return NoteDB(":memory:")


class TestData:

    def test_init(self):
        data_instance = Data()
        expected_path_suffix = "atomics_data.json"
        assert data_instance.DATA_PATH.endswith(expected_path_suffix)
        assert os.path.isabs(data_instance.DATA_PATH)

    def test_create_data_file_creates_db_and_json(self):
        db = _in_memory_db()
        globals.NOTE_DB = db
        data_instance = Data()
        with patch('builtins.open', mock_open()):
            with patch('json.dump') as mock_dump:
                data_instance.create_data_file()
                mock_dump.assert_called_once_with(dict(), unittest_any())

    def test_update_data_file_stores_in_db_and_writes_json(self):
        db = _in_memory_db()
        globals.NOTE_DB = db
        data_instance = Data()
        test_data = {
            "Added Media": ["img.jpg"],
            "File Hashes": {"notes/foo.md": "abc123"},
        }
        with patch('builtins.open', mock_open()):
            with patch('json.dump') as mock_dump:
                data_instance.update_data_file(test_data)
                assert "img.jpg" in db.get_added_media()
                assert db.get_file_hash("notes/foo.md") == "abc123"
                # JSON backup written with current DB state
                written = mock_dump.call_args[0][0]
                assert "img.jpg" in written["Added Media"]
                assert written["File Hashes"]["notes/foo.md"] == "abc123"

    def test_load_data_file_reads_from_db(self):
        db = _in_memory_db()
        db.add_media("media1.jpg")
        db.add_media("media2.jpg")
        db.set_file_hash("a.md", "hash_a")
        globals.NOTE_DB = db
        data_instance = Data()
        data_instance.load_data_file()
        assert set(globals.ADDED_MEDIA) == {"media1.jpg", "media2.jpg"}
        assert globals.FILE_HASHES == {"a.md": "hash_a"}

    def test_load_data_file_migrates_from_json_when_db_empty(self):
        db = _in_memory_db()
        globals.NOTE_DB = db
        legacy = {
            "Added Media": ["legacy.jpg"],
            "File Hashes": {"old.md": "oldhash"},
        }
        data_instance = Data()
        with patch('os.path.exists', return_value=True):
            with patch('builtins.open', side_effect=lambda *a, **kw: __import__('io').StringIO(json.dumps(legacy))):
                data_instance.load_data_file()
        assert "legacy.jpg" in globals.ADDED_MEDIA
        assert globals.FILE_HASHES.get("old.md") == "oldhash"

    def test_load_data_file_empty_db_no_json(self):
        db = _in_memory_db()
        globals.NOTE_DB = db
        data_instance = Data()
        with patch('os.path.exists', return_value=False):
            data_instance.load_data_file()
        assert globals.ADDED_MEDIA == []
        assert globals.FILE_HASHES == {}


class unittest_any:
    """Matches any value — for assert_called_once_with when content doesn't matter."""
    def __eq__(self, other):
        return True
