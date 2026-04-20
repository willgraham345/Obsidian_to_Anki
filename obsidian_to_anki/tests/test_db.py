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
