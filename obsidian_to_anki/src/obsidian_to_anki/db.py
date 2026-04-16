"""SQLite database for storing parsed Obsidian notes."""

import json
import os
import sqlite3
import uuid as uuid_module
from datetime import datetime, timezone


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


class NoteDB:
    """SQLite-backed store for parsed notes, file hashes, and added media."""

    DEFAULT_DB_PATH = os.path.normpath(os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "..", "..",
        "obsidian_to_anki.db"
    ))

    def __init__(self, db_path: str | None = None):
        self.db_path = db_path if db_path is not None else self.DEFAULT_DB_PATH
        self._conn = sqlite3.connect(self.db_path)
        self._conn.row_factory = sqlite3.Row
        self._create_tables()

    def _create_tables(self):
        self._conn.executescript("""
            CREATE TABLE IF NOT EXISTS notes (
                id          TEXT PRIMARY KEY,
                anki_id     INTEGER,
                file_path   TEXT NOT NULL,
                line_number INTEGER NOT NULL,
                note_type   TEXT NOT NULL,
                field_1     TEXT,
                field_2     TEXT,
                image_paths TEXT,
                tags        TEXT,
                deck_name   TEXT,
                created_at  TEXT NOT NULL,
                updated_at  TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS file_hashes (
                file_path   TEXT PRIMARY KEY,
                sha256      TEXT NOT NULL,
                updated_at  TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS added_media (
                filename    TEXT PRIMARY KEY
            );
        """)
        self._conn.commit()

    def close(self):
        self._conn.close()

    # ------------------------------------------------------------------
    # Notes
    # ------------------------------------------------------------------

    def upsert_note(
        self,
        uuid: str,
        anki_id: int | None,
        file_path: str,
        line_number: int,
        note_type: str,
        field_1: str | None,
        field_2: str | None,
        image_paths: list,
        tags: list,
        deck_name: str,
    ) -> None:
        now = _now()
        existing = self.get_note(uuid)
        created_at = existing["created_at"] if existing else now
        self._conn.execute(
            """
            INSERT INTO notes
                (id, anki_id, file_path, line_number, note_type,
                 field_1, field_2, image_paths, tags, deck_name,
                 created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                anki_id     = excluded.anki_id,
                file_path   = excluded.file_path,
                line_number = excluded.line_number,
                note_type   = excluded.note_type,
                field_1     = excluded.field_1,
                field_2     = excluded.field_2,
                image_paths = excluded.image_paths,
                tags        = excluded.tags,
                deck_name   = excluded.deck_name,
                updated_at  = excluded.updated_at
            """,
            (
                uuid, anki_id, file_path, line_number, note_type,
                field_1, field_2,
                json.dumps(image_paths),
                json.dumps(tags),
                deck_name,
                created_at, now,
            ),
        )
        self._conn.commit()

    def get_note(self, uuid: str) -> dict | None:
        row = self._conn.execute(
            "SELECT * FROM notes WHERE id = ?", (uuid,)
        ).fetchone()
        return dict(row) if row else None

    def get_note_by_location(
        self, file_path: str, line_number: int, note_type: str
    ) -> dict | None:
        row = self._conn.execute(
            "SELECT * FROM notes WHERE file_path = ? AND line_number = ? AND note_type = ?",
            (file_path, line_number, note_type),
        ).fetchone()
        return dict(row) if row else None

    def delete_note(self, uuid: str) -> None:
        self._conn.execute("DELETE FROM notes WHERE id = ?", (uuid,))
        self._conn.commit()

    def get_notes_for_file(self, file_path: str) -> list[dict]:
        rows = self._conn.execute(
            "SELECT * FROM notes WHERE file_path = ?", (file_path,)
        ).fetchall()
        return [dict(r) for r in rows]

    def mark_synced(self, uuid: str, anki_id: int) -> None:
        self._conn.execute(
            "UPDATE notes SET anki_id = ?, updated_at = ? WHERE id = ?",
            (anki_id, _now(), uuid),
        )
        self._conn.commit()

    # ------------------------------------------------------------------
    # File hashes
    # ------------------------------------------------------------------

    def get_file_hash(self, file_path: str) -> str | None:
        row = self._conn.execute(
            "SELECT sha256 FROM file_hashes WHERE file_path = ?", (file_path,)
        ).fetchone()
        return row["sha256"] if row else None

    def set_file_hash(self, file_path: str, sha256: str) -> None:
        self._conn.execute(
            """
            INSERT INTO file_hashes (file_path, sha256, updated_at)
            VALUES (?, ?, ?)
            ON CONFLICT(file_path) DO UPDATE SET
                sha256     = excluded.sha256,
                updated_at = excluded.updated_at
            """,
            (file_path, sha256, _now()),
        )
        self._conn.commit()

    def get_all_file_hashes(self) -> dict:
        rows = self._conn.execute("SELECT file_path, sha256 FROM file_hashes").fetchall()
        return {r["file_path"]: r["sha256"] for r in rows}

    # ------------------------------------------------------------------
    # Added media
    # ------------------------------------------------------------------

    def add_media(self, filename: str) -> None:
        self._conn.execute(
            "INSERT OR IGNORE INTO added_media (filename) VALUES (?)", (filename,)
        )
        self._conn.commit()

    def get_added_media(self) -> list:
        rows = self._conn.execute("SELECT filename FROM added_media").fetchall()
        return [r["filename"] for r in rows]
