"""SQLite database for storing parsed Obsidian notes."""

import json
import os
import sqlite3
import uuid as uuid_module
from datetime import datetime, timezone

from .utils import strip_html as _plain


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _strip_stem(text: str | None) -> str | None:
    """Remove <br><b>...</b> file-stem suffix injected by FormatConverter."""
    if text is None:
        return None
    idx = text.find('<br><b>')
    return text[:idx] if idx >= 0 else text


def _strip_obsidian_link(text: str | None) -> str | None:
    """Remove <br><a href="obsidian://...">...</a> vault link from field_1.

    Used in content comparisons so that notes match even when the source file
    was moved (which changes the embedded obsidian:// URL).
    """
    if text is None:
        return None
    idx = text.find('<br><a href="obsidian://')
    return text[:idx] if idx >= 0 else text


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
                id                 TEXT PRIMARY KEY,
                anki_id            INTEGER,
                file_path          TEXT NOT NULL,
                line_number        INTEGER NOT NULL,
                note_type          TEXT NOT NULL,
                field_1            TEXT,
                field_2            TEXT,
                image_paths        TEXT,
                tags               TEXT,
                deck_name          TEXT,
                state              TEXT DEFAULT 'unknown',
                recommended_action TEXT,
                created_at         TEXT NOT NULL,
                updated_at         TEXT NOT NULL
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

            CREATE TABLE IF NOT EXISTS anki_diff (
                id           TEXT PRIMARY KEY,
                operation    TEXT NOT NULL,
                note_type    TEXT,
                deck_name    TEXT,
                field_1      TEXT,
                field_2      TEXT,
                tags         TEXT,
                anki_id      INTEGER,
                file_path    TEXT,
                created_at   TEXT NOT NULL
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
                    WHEN v.note_type IS NOT a.note_type             THEN 'modify_type'
                    WHEN (CASE WHEN INSTR(v.field_1,'<br><b>')>0 THEN SUBSTR(v.field_1,1,INSTR(v.field_1,'<br><b>')-1) ELSE v.field_1 END
                          IS NOT
                          CASE WHEN INSTR(a.field_1,'<br><b>')>0 THEN SUBSTR(a.field_1,1,INSTR(a.field_1,'<br><b>')-1) ELSE a.field_1 END)
                      AND (v.field_2 IS NOT a.field_2)             THEN 'modify_fields'
                    WHEN CASE WHEN INSTR(v.field_1,'<br><b>')>0 THEN SUBSTR(v.field_1,1,INSTR(v.field_1,'<br><b>')-1) ELSE v.field_1 END
                         IS NOT
                         CASE WHEN INSTR(a.field_1,'<br><b>')>0 THEN SUBSTR(a.field_1,1,INSTR(a.field_1,'<br><b>')-1) ELSE a.field_1 END
                                                                    THEN 'modify_field_1'
                    WHEN v.field_2 IS NOT a.field_2                THEN 'modify_field_2'
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
        if "recommended_action" not in notes_cols:
            self._conn.execute("ALTER TABLE notes ADD COLUMN recommended_action TEXT")

        fh_cols = [r[1] for r in self._conn.execute("PRAGMA table_info(file_hashes)").fetchall()]
        if "atomic_id" not in fh_cols:
            self._conn.execute("ALTER TABLE file_hashes ADD COLUMN atomic_id TEXT")

        # anki_diff table added post-initial-schema
        existing_tables = {r[0] for r in self._conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()}
        if "anki_diff" not in existing_tables:
            self._conn.execute("""
                CREATE TABLE anki_diff (
                    id           TEXT PRIMARY KEY,
                    operation    TEXT NOT NULL,
                    note_type    TEXT,
                    deck_name    TEXT,
                    field_1      TEXT,
                    field_2      TEXT,
                    tags         TEXT,
                    anki_id      INTEGER,
                    file_path    TEXT,
                    created_at   TEXT NOT NULL
                )
            """)

        self._dedup_notes()
        self._recover_anki_ids()
        self._conn.commit()

    def _dedup_notes(self) -> int:
        """Delete duplicate notes accumulated by line-shift cascade rescans.

        For each group of rows sharing (file_path, note_type, field_1, field_2,
        deck_name), keep the row with an anki_id (highest anki_id wins when
        multiple exist) and delete the rest. Returns number of rows deleted.
        """
        dupes = self._conn.execute("""
            SELECT file_path, note_type, field_1, field_2, deck_name
            FROM notes
            GROUP BY file_path, note_type, field_1, field_2, deck_name
            HAVING COUNT(*) > 1
        """).fetchall()

        deleted = 0
        for row in dupes:
            group = self._conn.execute("""
                SELECT id, anki_id FROM notes
                WHERE file_path IS ? AND note_type IS ? AND field_1 IS ?
                  AND field_2 IS ? AND deck_name IS ?
                ORDER BY (anki_id IS NOT NULL) DESC, anki_id DESC, updated_at DESC
            """, (row[0], row[1], row[2], row[3], row[4])).fetchall()
            keep_id = group[0]["id"]
            stale_ids = [r["id"] for r in group[1:]]
            for sid in stale_ids:
                self._conn.execute("DELETE FROM notes WHERE id = ?", (sid,))
                deleted += 1

        if deleted:
            print(f"[db] Deduped {deleted} stale note record(s)")
        return deleted

    def _recover_anki_ids(self) -> int:
        """Link vault notes that lost their anki_id to matching Anki snapshot entries.

        For each note with anki_id IS NULL, calls find_anki_note_by_content.
        Skips notes queued for interactive resolution (review/link) since those
        have already been flagged as ambiguous by similarity_search.
        Returns number of links made.
        """
        unlinked = self._conn.execute("""
            SELECT id, note_type, field_1, field_2
            FROM notes
            WHERE anki_id IS NULL
              AND (recommended_action IS NULL
                   OR recommended_action NOT IN ('review', 'link'))
        """).fetchall()

        linked = 0
        for row in unlinked:
            recovered = self.find_anki_note_by_content(
                row["note_type"], row["field_1"], row["field_2"]
            )
            if recovered is not None:
                self.mark_synced(row["id"], recovered)
                linked += 1

        if linked:
            print(f"[db] Recovered {linked} anki_id(s) via snapshot content match")
        return linked

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
                anki_id     = COALESCE(excluded.anki_id, anki_id),
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
        # When duplicates exist at the same location (from line-shift cascade), prefer
        # the row that already has an anki_id, then most recently updated.
        row = self._conn.execute(
            """SELECT * FROM notes
               WHERE file_path = ? AND line_number = ? AND note_type = ?
               ORDER BY (anki_id IS NOT NULL) DESC, updated_at DESC
               LIMIT 1""",
            (file_path, line_number, note_type),
        ).fetchone()
        return dict(row) if row else None

    def get_note_by_content(
        self,
        file_path: str,
        note_type: str,
        field_1: str | None,
        field_2: str | None = None,
        deck_name: str | None = None,
    ) -> dict | None:
        """Fallback lookup by content when line numbers have shifted.

        Matches on file_path + note_type + field_1 + field_2 + deck_name.
        When duplicates exist (accumulated from previous failed rescans), prefers
        the row with anki_id so the sync link is not lost.
        """
        rows = self._conn.execute(
            """SELECT * FROM notes
               WHERE file_path = ? AND note_type = ?
                 AND field_1 IS ? AND field_2 IS ? AND deck_name IS ?
               ORDER BY (anki_id IS NOT NULL) DESC, updated_at DESC""",
            (file_path, note_type, field_1, field_2, deck_name),
        ).fetchall()
        if not rows:
            return None
        # Prefer the unique anki_id row; if multiple rows share the same anki_id
        # (or none have one), return the highest-priority row from the ORDER BY.
        with_id = [r for r in rows if r["anki_id"] is not None]
        if len(with_id) == 1:
            return dict(with_id[0])
        return dict(rows[0])

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

    def set_state_and_action(self, uuid: str, state: str, action: str) -> None:
        """Set state and recommended_action atomically."""
        self._conn.execute(
            "UPDATE notes SET state = ?, recommended_action = ?, updated_at = ? WHERE id = ?",
            (state, action, _now(), uuid),
        )
        self._conn.commit()

    def clear_recommended_action(self, uuid: str) -> None:
        """Clear recommended_action after write script executes."""
        self._conn.execute(
            "UPDATE notes SET recommended_action = NULL, updated_at = ? WHERE id = ?",
            (_now(), uuid),
        )
        self._conn.commit()

    def get_pending_review(self) -> list[dict]:
        """Return notes queued for user review."""
        rows = self._conn.execute(
            "SELECT * FROM notes WHERE recommended_action = 'review'"
        ).fetchall()
        return [dict(r) for r in rows]

    def get_review_queue(self) -> list[dict]:
        """Return notes with recommended_action = 'review' or 'link' (need interactive resolution)."""
        rows = self._conn.execute(
            "SELECT * FROM notes WHERE recommended_action IN ('review', 'link')"
        ).fetchall()
        return [dict(r) for r in rows]

    def get_notes_by_state(self, state: str) -> list[dict]:
        """Return all notes with the given state value."""
        rows = self._conn.execute(
            "SELECT * FROM notes WHERE state = ?", (state,)
        ).fetchall()
        return [dict(r) for r in rows]

    def similarity_search(
        self,
        field_1: str | None,
        field_2: str | None,
        note_type: str,
    ) -> list[int]:
        """Return anki_ids of orphan Anki notes matching field content and note_type.

        Strips <br><b>...</b> stem suffix from field_1 before comparing.
        Searches only anki_notes with no corresponding vault entry.
        Returns list of matching anki_ids (empty = no match, len > 1 = ambiguous).
        """
        stripped_f1 = _strip_stem(field_1)
        orphans = self._conn.execute("""
            SELECT a.anki_id, a.field_1, a.field_2
            FROM anki_notes a
            WHERE a.note_type = ?
              AND NOT EXISTS (SELECT 1 FROM notes n WHERE n.anki_id = a.anki_id)
        """, (note_type,)).fetchall()
        return [
            row["anki_id"] for row in orphans
            if _strip_stem(row["field_1"]) == stripped_f1 and row["field_2"] == field_2
        ]

    def find_anki_note_by_content(
        self,
        note_type: str,
        field_1: str | None,
        field_2: str | None,
    ) -> int | None:
        """Return anki_id when exactly one anki_note matches note_type + field content.

        Used to recover anki_id for vault notes whose DB link was lost (e.g. from a
        line-number cascade or file move). Strips both the <br><b>...</b> file-stem
        suffix and the <br><a href="obsidian://..."> vault link from field_1 before
        comparing, so the match is stable across file renames and vault moves.

        Two-stage match:
        1. field_1 + field_2 (exact) — handles unmodified notes
        2. field_1 only — handles notes where the user updated field_2 (back field);
           the comparison view will surface the diff as modify_field_2 rather than add

        Returns None when no unique match is found at either stage.
        """
        core_f1 = _strip_obsidian_link(_strip_stem(field_1))
        rows = self._conn.execute(
            "SELECT anki_id, field_1, field_2 FROM anki_notes WHERE note_type = ?",
            (note_type,),
        ).fetchall()
        stripped = [
            (r["anki_id"], _strip_obsidian_link(_strip_stem(r["field_1"])), r["field_2"])
            for r in rows
        ]
        # Stage 1: field_1 + field_2 exact match
        matches = [aid for aid, sf1, f2 in stripped if sf1 == core_f1 and f2 == field_2]
        if len(matches) == 1:
            return matches[0]
        # Stage 2: field_1 only (back field may have been updated in vault)
        matches = [aid for aid, sf1, _ in stripped if sf1 == core_f1]
        return matches[0] if len(matches) == 1 else None

    def revert_note_to_anki(self, uuid: str) -> bool:
        """Overwrite vault note fields in DB with current Anki snapshot.

        Returns True when a matching Anki note was found and applied.
        After this call the note comparison view will show the note as 'synced'.
        """
        note = self.get_note(uuid)
        if not note or not note.get("anki_id"):
            return False
        anki = self._conn.execute(
            "SELECT field_1, field_2 FROM anki_notes WHERE anki_id = ?",
            (note["anki_id"],),
        ).fetchone()
        if not anki:
            return False
        self._conn.execute(
            "UPDATE notes SET field_1 = ?, field_2 = ?, updated_at = ? WHERE id = ?",
            (anki["field_1"], anki["field_2"], _now(), uuid),
        )
        self._conn.commit()
        return True

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

    # ------------------------------------------------------------------
    # Diff table (anki_diff)
    # ------------------------------------------------------------------

    def upsert_diff_entry(
        self,
        id: str,
        operation: str,
        note_type: str | None,
        deck_name: str | None,
        field_1: str | None,
        field_2: str | None,
        tags: list | None,
        anki_id: int | None,
        file_path: str | None,
    ) -> None:
        self._conn.execute(
            """
            INSERT INTO anki_diff
                (id, operation, note_type, deck_name, field_1, field_2,
                 tags, anki_id, file_path, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                operation  = excluded.operation,
                note_type  = excluded.note_type,
                deck_name  = excluded.deck_name,
                field_1    = excluded.field_1,
                field_2    = excluded.field_2,
                tags       = excluded.tags,
                anki_id    = excluded.anki_id,
                file_path  = excluded.file_path
            """,
            (
                id, operation, note_type, deck_name, field_1, field_2,
                json.dumps(tags) if tags is not None else None,
                anki_id, file_path, _now(),
            ),
        )
        self._conn.commit()

    def get_diff_entries(self, operation: str | None = None) -> list[dict]:
        if operation:
            rows = self._conn.execute(
                "SELECT * FROM anki_diff WHERE operation = ? ORDER BY file_path",
                (operation,),
            ).fetchall()
        else:
            rows = self._conn.execute(
                "SELECT * FROM anki_diff ORDER BY operation, file_path"
            ).fetchall()
        return [dict(r) for r in rows]

    def delete_diff_entry(self, id: str) -> None:
        self._conn.execute("DELETE FROM anki_diff WHERE id = ?", (id,))
        self._conn.commit()

    def clear_diff(self) -> None:
        self._conn.execute("DELETE FROM anki_diff")
        self._conn.commit()

    def get_diff_summary(self) -> list[dict]:
        rows = self._conn.execute(
            "SELECT operation, COUNT(*) AS n FROM anki_diff"
            " GROUP BY operation ORDER BY operation"
        ).fetchall()
        return [dict(r) for r in rows]
