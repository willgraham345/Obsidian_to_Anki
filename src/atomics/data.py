"""Class for managing the data file (not meant to be changed by users.)"""

import json
import os

from . import globals
from .db import NoteDB


class Data:
    """Manages persistence via SQLite (primary) and JSON backup."""

    def __init__(self):
        self.DATA_PATH = os.path.normpath(os.path.expanduser(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "..",
                "..",
                "atomics_data.json"
            )
        ))

    def _db(self) -> NoteDB:
        if globals.NOTE_DB is None:
            globals.NOTE_DB = NoteDB()
        return globals.NOTE_DB

    def create_data_file(self):
        """Creates the DB and an empty JSON backup."""
        print("Creating data file...")
        self._db()  # creates tables on init
        with open(self.DATA_PATH, "w") as f:
            json.dump(dict(), f)

    def update_data_file(self, data):
        """Writes data to the DB, then dumps a JSON backup."""
        print("Updating data file...")
        db = self._db()
        added_media = data.get("Added Media", [])
        file_hashes = data.get("File Hashes", {})
        for filename in added_media:
            db.add_media(filename)
        for path, sha256 in file_hashes.items():
            db.set_file_hash(path, sha256)
        backup = {
            "Added Media": db.get_added_media(),
            "File Hashes": db.get_all_file_hashes(),
        }
        with open(self.DATA_PATH, "w") as f:
            json.dump(backup, f)

    def load_data_file(self):
        """Loads persisted state into globals. DB is primary; falls back to JSON."""
        db = self._db()
        added_media = db.get_added_media()
        file_hashes = db.get_all_file_hashes()
        if not added_media and not file_hashes and os.path.exists(self.DATA_PATH):
            # First-run migration: seed DB from existing JSON
            try:
                with open(self.DATA_PATH, "r") as f:
                    legacy = json.load(f)
                for filename in legacy.get("Added Media", []):
                    db.add_media(filename)
                for path, sha256 in legacy.get("File Hashes", {}).items():
                    db.set_file_hash(path, sha256)
                added_media = db.get_added_media()
                file_hashes = db.get_all_file_hashes()
            except (json.JSONDecodeError, OSError):
                pass
        globals.ADDED_MEDIA = added_media
        globals.FILE_HASHES = file_hashes
