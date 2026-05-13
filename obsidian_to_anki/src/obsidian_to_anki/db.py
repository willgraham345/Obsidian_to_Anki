"""SQLite database for storing parsed Obsidian notes."""

import json
import os
import sqlite3
import uuid as uuid_module
from datetime import datetime, timezone

from .utils import strip_html as _plain


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
                state       TEXT DEFAULT 'unknown',
                created_at  TEXT NOT NULL,
                updated_at  TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS file_hashes (
                file_path   TEXT PRIMARY KEY,
                sha256      TEXT NOT NULL,
                atomic_id   TEXT,
                updated_at  TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS added_media (
                filename    TEXT PRIMARY KEY
            );

            CREATE TABLE IF NOT EXISTS anki_notes (
                anki_id       INTEGER PRIMARY KEY,
                note_type     TEXT NOT NULL,
                field_1       TEXT,
                field_2       TEXT,
                tags          TEXT,
                deck_name     TEXT,
                mod_timestamp INTEGER,
                synced_at     TEXT NOT NULL
            );

            DROP VIEW IF EXISTS note_comparison;
            CREATE VIEW note_comparison AS
            SELECT
                v.anki_id          AS anki_id,
                v.note_type        AS note_type,
                v.file_path,
                v.field_1          AS vault_field_1,
                a.field_1          AS anki_field_1,
                v.field_2          AS vault_field_2,
                a.field_2          AS anki_field_2,
                v.tags             AS vault_tags,
                a.tags             AS anki_tags,
                v.deck_name        AS vault_deck,
                a.deck_name        AS anki_deck,
                a.mod_timestamp,
                CASE
                    WHEN v.anki_id IS NULL                          THEN 'not_in_anki'
                    WHEN a.anki_id IS NULL                          THEN 'stale_id'
                    WHEN (SELECT COUNT(*) FROM notes _n WHERE _n.anki_id = v.anki_id) > 1
                                                                    THEN 'synced'
                    WHEN CASE WHEN INSTR(v.field_1,'<br><b>')>0 THEN SUBSTR(v.field_1,1,INSTR(v.field_1,'<br><b>')-1) ELSE v.field_1 END
                         IS NOT
                         CASE WHEN INSTR(a.field_1,'<br><b>')>0 THEN SUBSTR(a.field_1,1,INSTR(a.field_1,'<br><b>')-1) ELSE a.field_1 END
                      OR v.field_2 IS NOT a.field_2                THEN 'modified'
                    WHEN v.deck_name IS NOT a.deck_name             THEN 'modify_deck'
                    ELSE 'synced'
                END AS status
            FROM notes v
            LEFT JOIN anki_notes a ON v.anki_id = a.anki_id

            UNION ALL

            SELECT
                a.anki_id,
                a.note_type,
                NULL  AS file_path,
                NULL  AS vault_field_1,
                a.field_1,
                NULL  AS vault_field_2,
                a.field_2,
                NULL  AS vault_tags,
                a.tags,
                NULL  AS vault_deck,
                a.deck_name,
                a.mod_timestamp,
                'orphan_in_anki' AS status
            FROM anki_notes a
            LEFT JOIN notes v ON a.anki_id = v.anki_id
            WHERE v.anki_id IS NULL;
        """)
        self._conn.commit()
        self._migrate()

    def _migrate(self):
        """Add columns introduced after initial schema (idempotent)."""
        notes_cols = [r[1] for r in self._conn.execute("PRAGMA table_info(notes)").fetchall()]
        if "state" not in notes_cols:
            self._conn.execute("ALTER TABLE notes ADD COLUMN state TEXT DEFAULT 'unknown'")

        fh_cols = [r[1] for r in self._conn.execute("PRAGMA table_info(file_hashes)").fetchall()]
        if "atomic_id" not in fh_cols:
            self._conn.execute("ALTER TABLE file_hashes ADD COLUMN atomic_id TEXT")

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

    def get_note_by_content(
        self, file_path: str, note_type: str, field_1: str | None
    ) -> dict | None:
        """Fallback lookup by content when line numbers have shifted.

        Returns the single matching note if exactly one exists, else None.
        """
        rows = self._conn.execute(
            "SELECT * FROM notes WHERE file_path = ? AND note_type = ? AND field_1 IS ?",
            (file_path, note_type, field_1),
        ).fetchall()
        return dict(rows[0]) if len(rows) == 1 else None

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
            "UPDATE notes SET anki_id = ?, state = 'unknown', updated_at = ? WHERE id = ?",
            (anki_id, _now(), uuid),
        )
        self._conn.commit()

    def mark_stale(self, file_path: str) -> int:
        """Mark all notes for a file as stale. Returns row count."""
        cur = self._conn.execute(
            "UPDATE notes SET state = 'stale', updated_at = ? WHERE file_path = ?",
            (_now(), file_path),
        )
        self._conn.commit()
        return cur.rowcount

    def get_stale_notes(self) -> list[dict]:
        """Return all notes with state='stale'."""
        rows = self._conn.execute(
            "SELECT * FROM notes WHERE state = 'stale'"
        ).fetchall()
        return [dict(r) for r in rows]

    def update_anki_note_fields(self, anki_id: int, field_1: str | None, field_2: str | None) -> None:
        self._conn.execute(
            "UPDATE anki_notes SET field_1 = ?, field_2 = ?, synced_at = ? WHERE anki_id = ?",
            (field_1, field_2, _now(), anki_id),
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

    def set_file_atomic_id(self, file_path: str, atomic_id: str) -> None:
        self._conn.execute(
            """
            INSERT INTO file_hashes (file_path, sha256, atomic_id, updated_at)
            VALUES (?, '', ?, ?)
            ON CONFLICT(file_path) DO UPDATE SET
                atomic_id  = excluded.atomic_id,
                updated_at = excluded.updated_at
            """,
            (file_path, atomic_id, _now()),
        )
        self._conn.commit()

    def get_file_atomic_id(self, file_path: str) -> str | None:
        row = self._conn.execute(
            "SELECT atomic_id FROM file_hashes WHERE file_path = ?", (file_path,)
        ).fetchone()
        return row["atomic_id"] if row else None

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

    # ------------------------------------------------------------------
    # Anki snapshot
    # ------------------------------------------------------------------

    def upsert_anki_note(
        self,
        anki_id: int,
        note_type: str,
        field_1: str | None,
        field_2: str | None,
        tags: list,
        deck_name: str | None,
        mod_timestamp: int | None,
    ) -> None:
        self._conn.execute(
            """
            INSERT INTO anki_notes
                (anki_id, note_type, field_1, field_2, tags, deck_name,
                 mod_timestamp, synced_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(anki_id) DO UPDATE SET
                note_type     = excluded.note_type,
                field_1       = excluded.field_1,
                field_2       = excluded.field_2,
                tags          = excluded.tags,
                deck_name     = excluded.deck_name,
                mod_timestamp = excluded.mod_timestamp,
                synced_at     = excluded.synced_at
            """,
            (
                anki_id, note_type, field_1, field_2,
                json.dumps(tags),
                deck_name, mod_timestamp, _now(),
            ),
        )
        self._conn.commit()

    def clear_anki_notes(self) -> None:
        """Wipe the anki_notes table before re-snapshotting."""
        self._conn.execute("DELETE FROM anki_notes")
        self._conn.commit()

    def reconcile_orphans(self) -> int:
        """Match orphaned Anki notes to unlinked vault notes by field content.

        For each Anki note not referenced by any vault entry (orphan_in_anki),
        search for a vault note whose anki_id is either NULL or stale (not in
        the current anki_notes snapshot), with matching field_1, field_2, and
        note_type. If exactly one candidate exists, link them via mark_synced().
        Skips if zero or multiple candidates (ambiguous).

        Returns the number of links made.
        """
        orphans = self._conn.execute("""
            SELECT a.anki_id, a.note_type, a.field_1, a.field_2
            FROM anki_notes a
            WHERE NOT EXISTS (
                SELECT 1 FROM notes n WHERE n.anki_id = a.anki_id
            )
        """).fetchall()

        linked = 0
        for orphan in orphans:
            # Pass 1: exact HTML match — only truly unlinked vault notes
            candidates = self._conn.execute("""
                SELECT id FROM notes
                WHERE anki_id IS NULL
                  AND note_type = ?
                  AND field_1 IS ?
                  AND field_2 IS ?
            """, (orphan["note_type"], orphan["field_1"], orphan["field_2"])).fetchall()

            if len(candidates) == 1:
                self.mark_synced(candidates[0]["id"], orphan["anki_id"])
                linked += 1
                continue

            # Pass 2: plaintext fallback (Anki normalises HTML on storage)
            if candidates:
                continue  # ambiguous exact match — skip
            plain_f1 = _plain(orphan["field_1"])
            plain_f2 = _plain(orphan["field_2"])
            unlinked = self._conn.execute("""
                SELECT id, field_1, field_2 FROM notes
                WHERE anki_id IS NULL
                  AND note_type = ?
            """, (orphan["note_type"],)).fetchall()
            text_matches = [
                r for r in unlinked
                if _plain(r["field_1"]) == plain_f1 and _plain(r["field_2"]) == plain_f2
            ]
            if len(text_matches) == 1:
                self.mark_synced(text_matches[0]["id"], orphan["anki_id"])
                linked += 1

        return linked

    def get_comparison_summary(self) -> list[dict]:
        """Return [{status, n}, ...] from note_comparison grouped by status."""
        rows = self._conn.execute(
            "SELECT status, COUNT(*) AS n FROM note_comparison"
            " GROUP BY status ORDER BY n DESC"
        ).fetchall()
        return [dict(r) for r in rows]

    def get_comparison_rows(self, exclude_synced: bool = True) -> list[dict]:
        """Return all rows from note_comparison, optionally skipping synced ones."""
        query = "SELECT * FROM note_comparison"
        if exclude_synced:
            query += " WHERE status != 'synced'"
        query += " ORDER BY status, note_type, file_path"
        rows = self._conn.execute(query).fetchall()
        return [dict(r) for r in rows]
