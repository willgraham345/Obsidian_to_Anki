"""Tests for the NoteDB SQLite wrapper."""

import json
import pytest

from src.obsidian_to_anki.db import NoteDB


@pytest.fixture
def db():
    """In-memory NoteDB for each test."""
    instance = NoteDB(":memory:")
    yield instance
    instance.close()


def _make_note(db, uuid="uuid-1", anki_id=None, file_path="deck/note.md",
               line_number=10, note_type="Basic",
               field_1="<p>Front</p>", field_2="<p>Back</p>",
               image_paths=None, tags=None, deck_name="Default"):
    db.upsert_note(
        uuid=uuid,
        anki_id=anki_id,
        file_path=file_path,
        line_number=line_number,
        note_type=note_type,
        field_1=field_1,
        field_2=field_2,
        image_paths=image_paths or [],
        tags=tags or ["Obsidian_to_Anki"],
        deck_name=deck_name,
    )


class TestNotesCRUD:

    def test_upsert_and_get_by_uuid(self, db):
        _make_note(db, uuid="abc-123")
        row = db.get_note("abc-123")
        assert row is not None
        assert row["id"] == "abc-123"
        assert row["note_type"] == "Basic"
        assert row["field_1"] == "<p>Front</p>"
        assert row["field_2"] == "<p>Back</p>"

    def test_get_nonexistent_returns_none(self, db):
        assert db.get_note("does-not-exist") is None

    def test_get_note_by_location(self, db):
        _make_note(db, uuid="loc-1", file_path="a/b.md", line_number=5, note_type="Cloze")
        row = db.get_note_by_location("a/b.md", 5, "Cloze")
        assert row is not None
        assert row["id"] == "loc-1"

    def test_get_note_by_location_no_match(self, db):
        _make_note(db, file_path="a/b.md", line_number=5, note_type="Basic")
        assert db.get_note_by_location("a/b.md", 99, "Basic") is None
        assert db.get_note_by_location("a/b.md", 5, "Cloze") is None

    def test_upsert_updates_existing(self, db):
        _make_note(db, uuid="upd-1", field_1="Old")
        _make_note(db, uuid="upd-1", field_1="New")
        row = db.get_note("upd-1")
        assert row["field_1"] == "New"

    def test_upsert_preserves_created_at(self, db):
        _make_note(db, uuid="ts-1")
        created_at = db.get_note("ts-1")["created_at"]
        _make_note(db, uuid="ts-1", field_1="changed")
        assert db.get_note("ts-1")["created_at"] == created_at

    def test_delete_note(self, db):
        _make_note(db, uuid="del-1")
        db.delete_note("del-1")
        assert db.get_note("del-1") is None

    def test_get_notes_for_file(self, db):
        _make_note(db, uuid="f-1", file_path="x.md", line_number=1)
        _make_note(db, uuid="f-2", file_path="x.md", line_number=20)
        _make_note(db, uuid="f-3", file_path="y.md", line_number=1)
        rows = db.get_notes_for_file("x.md")
        assert len(rows) == 2
        assert {r["id"] for r in rows} == {"f-1", "f-2"}

    def test_image_paths_serialized(self, db):
        _make_note(db, uuid="img-1", image_paths=["foo.jpg", "bar.png"])
        row = db.get_note("img-1")
        assert json.loads(row["image_paths"]) == ["foo.jpg", "bar.png"]

    def test_tags_serialized(self, db):
        _make_note(db, uuid="tag-1", tags=["tag1", "tag2"])
        row = db.get_note("tag-1")
        assert json.loads(row["tags"]) == ["tag1", "tag2"]

    def test_cloze_note_null_field_2(self, db):
        _make_note(db, uuid="cloze-1", note_type="Cloze", field_1="{{c1::text}}", field_2=None)
        row = db.get_note("cloze-1")
        assert row["field_2"] is None


class TestMarkSynced:

    def test_mark_synced_sets_anki_id(self, db):
        _make_note(db, uuid="sync-1", anki_id=None)
        db.mark_synced("sync-1", 12345)
        assert db.get_note("sync-1")["anki_id"] == 12345

    def test_mark_synced_updates_timestamp(self, db):
        _make_note(db, uuid="sync-2", anki_id=None)
        before = db.get_note("sync-2")["updated_at"]
        db.mark_synced("sync-2", 99)
        after = db.get_note("sync-2")["updated_at"]
        assert after >= before


class TestFileHashes:

    def test_set_and_get_file_hash(self, db):
        db.set_file_hash("vault/note.md", "abc123")
        assert db.get_file_hash("vault/note.md") == "abc123"

    def test_get_missing_hash_returns_none(self, db):
        assert db.get_file_hash("nonexistent.md") is None

    def test_set_file_hash_overwrites(self, db):
        db.set_file_hash("f.md", "old")
        db.set_file_hash("f.md", "new")
        assert db.get_file_hash("f.md") == "new"

    def test_get_all_file_hashes(self, db):
        db.set_file_hash("a.md", "hash-a")
        db.set_file_hash("b.md", "hash-b")
        hashes = db.get_all_file_hashes()
        assert hashes == {"a.md": "hash-a", "b.md": "hash-b"}


class TestAddedMedia:

    def test_add_and_get_media(self, db):
        db.add_media("image.jpg")
        assert "image.jpg" in db.get_added_media()

    def test_add_media_idempotent(self, db):
        db.add_media("dup.jpg")
        db.add_media("dup.jpg")
        assert db.get_added_media().count("dup.jpg") == 1

    def test_get_added_media_empty(self, db):
        assert db.get_added_media() == []


def _make_anki_note(db, anki_id=1001, note_type="Basic",
                    field_1="<p>Front</p>", field_2="<p>Back</p>",
                    tags=None, deck_name="Default", mod_timestamp=None):
    db.upsert_anki_note(
        anki_id=anki_id,
        note_type=note_type,
        field_1=field_1,
        field_2=field_2,
        tags=tags or [],
        deck_name=deck_name,
        mod_timestamp=mod_timestamp,
    )


class TestReconcileOrphans:

    def test_links_exact_match(self, db):
        """Orphan Anki note matched to unlinked vault note — link made."""
        _make_note(db, uuid="v-1", anki_id=None, field_1="<p>Q</p>", field_2="<p>A</p>")
        _make_anki_note(db, anki_id=9001, field_1="<p>Q</p>", field_2="<p>A</p>")
        assert db.reconcile_orphans() == 1
        assert db.get_note("v-1")["anki_id"] == 9001

    def test_skips_already_linked(self, db):
        """Vault note already has anki_id — not re-linked."""
        _make_note(db, uuid="v-1", anki_id=9001, field_1="<p>Q</p>", field_2="<p>A</p>")
        _make_anki_note(db, anki_id=9002, field_1="<p>Q</p>", field_2="<p>A</p>")
        assert db.reconcile_orphans() == 0
        assert db.get_note("v-1")["anki_id"] == 9001

    def test_skips_ambiguous_multiple_candidates(self, db):
        """Two vault notes with identical fields — skip to avoid wrong link."""
        _make_note(db, uuid="v-1", anki_id=None, field_1="<p>Q</p>", field_2="<p>A</p>", line_number=1)
        _make_note(db, uuid="v-2", anki_id=None, field_1="<p>Q</p>", field_2="<p>A</p>", line_number=2)
        _make_anki_note(db, anki_id=9001, field_1="<p>Q</p>", field_2="<p>A</p>")
        assert db.reconcile_orphans() == 0
        assert db.get_note("v-1")["anki_id"] is None
        assert db.get_note("v-2")["anki_id"] is None

    def test_skips_note_type_mismatch(self, db):
        """Vault note_type differs from Anki note_type — no link."""
        _make_note(db, uuid="v-1", anki_id=None, note_type="Basic",
                   field_1="<p>Q</p>", field_2="<p>A</p>")
        _make_anki_note(db, anki_id=9001, note_type="Cloze",
                        field_1="<p>Q</p>", field_2="<p>A</p>")
        assert db.reconcile_orphans() == 0

    def test_no_orphans_returns_zero(self, db):
        """No orphaned Anki notes — nothing to do."""
        _make_note(db, uuid="v-1", anki_id=9001)
        _make_anki_note(db, anki_id=9001)
        assert db.reconcile_orphans() == 0

    def test_null_field_2_matches(self, db):
        """NULL field_2 (e.g. Cloze) matches correctly via IS comparison."""
        _make_note(db, uuid="v-1", anki_id=None, note_type="Cloze",
                   field_1="<p>{{c1::text}}</p>", field_2=None)
        _make_anki_note(db, anki_id=9001, note_type="Cloze",
                        field_1="<p>{{c1::text}}</p>", field_2=None)
        assert db.reconcile_orphans() == 1
        assert db.get_note("v-1")["anki_id"] == 9001

    def test_multiple_independent_matches(self, db):
        """Multiple distinct orphans each matched to a distinct vault note."""
        _make_note(db, uuid="v-1", anki_id=None, field_1="<p>Q1</p>", field_2="<p>A1</p>", line_number=1)
        _make_note(db, uuid="v-2", anki_id=None, field_1="<p>Q2</p>", field_2="<p>A2</p>", line_number=2)
        _make_anki_note(db, anki_id=9001, field_1="<p>Q1</p>", field_2="<p>A1</p>")
        _make_anki_note(db, anki_id=9002, field_1="<p>Q2</p>", field_2="<p>A2</p>")
        assert db.reconcile_orphans() == 2
        assert db.get_note("v-1")["anki_id"] == 9001
        assert db.get_note("v-2")["anki_id"] == 9002

    def test_obsidian_link_stripped_for_plaintext_match(self, db):
        """Vault field_1 with obsidian-link anchor matches Anki note without it."""
        vault_f1 = (
            'Type erasure'
            '<br><a href="obsidian://open?vault=Work&amp;file=Docs/note.md"'
            ' class="obsidian-link">Obsidian</a>'
        )
        _make_note(db, uuid="v-1", anki_id=None, field_1=vault_f1, field_2="<p>Back</p>")
        _make_anki_note(db, anki_id=9001, field_1="Type erasure", field_2="<p>Back</p>")
        assert db.reconcile_orphans() == 1
        assert db.get_note("v-1")["anki_id"] == 9001
