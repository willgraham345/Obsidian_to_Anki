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


class TestStateAndAction:

    def test_default_state_is_unknown(self, db):
        _make_note(db, uuid="s-1")
        assert db.get_note("s-1")["state"] == "unknown"

    def test_default_recommended_action_is_null(self, db):
        _make_note(db, uuid="s-1")
        assert db.get_note("s-1")["recommended_action"] is None

    def test_set_state_and_action(self, db):
        _make_note(db, uuid="s-1")
        db.set_state_and_action("s-1", "not_in_anki", "add")
        note = db.get_note("s-1")
        assert note["state"] == "not_in_anki"
        assert note["recommended_action"] == "add"

    def test_set_state_and_action_updates_timestamp(self, db):
        _make_note(db, uuid="s-1")
        before = db.get_note("s-1")["updated_at"]
        db.set_state_and_action("s-1", "synced", "none")
        assert db.get_note("s-1")["updated_at"] >= before

    def test_clear_recommended_action(self, db):
        _make_note(db, uuid="s-1")
        db.set_state_and_action("s-1", "not_in_anki", "add")
        db.clear_recommended_action("s-1")
        assert db.get_note("s-1")["recommended_action"] is None

    def test_clear_recommended_action_preserves_state(self, db):
        _make_note(db, uuid="s-1")
        db.set_state_and_action("s-1", "not_in_anki", "add")
        db.clear_recommended_action("s-1")
        assert db.get_note("s-1")["state"] == "not_in_anki"

    def test_get_pending_review_returns_review_items(self, db):
        _make_note(db, uuid="r-1", line_number=1)
        _make_note(db, uuid="r-2", line_number=2)
        _make_note(db, uuid="r-3", line_number=3)
        db.set_state_and_action("r-1", "not_in_anki", "review")
        db.set_state_and_action("r-2", "stale_id", "review")
        db.set_state_and_action("r-3", "not_in_anki", "add")
        items = db.get_pending_review()
        assert len(items) == 2
        assert {i["id"] for i in items} == {"r-1", "r-2"}

    def test_get_pending_review_empty(self, db):
        assert db.get_pending_review() == []

    def test_mark_synced_sets_state_unknown(self, db):
        _make_note(db, uuid="s-1")
        db.set_state_and_action("s-1", "not_in_anki", "add")
        db.mark_synced("s-1", 9001)
        assert db.get_note("s-1")["state"] == "unknown"


class TestModifyDeck:

    def test_modify_deck_status_in_view(self, db):
        """Fields match but vault deck differs from Anki deck → modify_deck."""
        _make_note(db, uuid="m-1", anki_id=8001, deck_name="VaultDeck")
        db.upsert_anki_note(
            anki_id=8001,
            note_type="Basic",
            field_1="<p>Front</p>",
            field_2="<p>Back</p>",
            tags=[],
            deck_name="AnkiDeck",
            mod_timestamp=None,
        )
        rows = db.get_comparison_rows(exclude_synced=True)
        modify_deck_rows = [r for r in rows if r["status"] == "modify_deck"]
        assert len(modify_deck_rows) == 1
        assert modify_deck_rows[0]["vault_deck"] == "VaultDeck"
        assert modify_deck_rows[0]["anki_deck"] == "AnkiDeck"

    def test_synced_when_decks_match(self, db):
        """Same fields AND same deck → synced, not modify_deck."""
        _make_note(db, uuid="m-2", anki_id=8002, deck_name="SameDeck")
        db.upsert_anki_note(
            anki_id=8002,
            note_type="Basic",
            field_1="<p>Front</p>",
            field_2="<p>Back</p>",
            tags=[],
            deck_name="SameDeck",
            mod_timestamp=None,
        )
        rows = db.get_comparison_rows(exclude_synced=False)
        statuses = {r["status"] for r in rows if r["anki_id"] == 8002}
        assert statuses == {"synced"}

    def test_modify_field_1_takes_priority_over_modify_deck(self, db):
        """field_1 differs → modify_field_1 even when decks also differ."""
        _make_note(db, uuid="m-3", anki_id=8003,
                   field_1="<p>NewFront</p>", deck_name="VaultDeck")
        db.upsert_anki_note(
            anki_id=8003,
            note_type="Basic",
            field_1="<p>OldFront</p>",
            field_2="<p>Back</p>",
            tags=[],
            deck_name="AnkiDeck",
            mod_timestamp=None,
        )
        rows = db.get_comparison_rows(exclude_synced=True)
        target = [r for r in rows if r["anki_id"] == 8003]
        assert len(target) == 1
        assert target[0]["status"] == "modify_field_1"

    def test_modify_type_status_in_view(self, db):
        """Vault note_type differs from Anki note_type → modify_type, not modify_fields."""
        _make_note(db, uuid="m-4", anki_id=8004,
                   field_1="<p>Front</p>", field_2="<p>Back</p>",
                   deck_name="Default", note_type="Basic")
        db.upsert_anki_note(
            anki_id=8004,
            note_type="Basic (reversed card)",
            field_1="<p>Front</p>",
            field_2="<p>Back</p>",
            tags=[],
            deck_name="Default",
            mod_timestamp=None,
        )
        rows = db.get_comparison_rows(exclude_synced=True)
        target = [r for r in rows if r["anki_id"] == 8004]
        assert len(target) == 1
        assert target[0]["status"] == "modify_type"

    def test_modify_type_takes_priority_over_modify_fields(self, db):
        """Type change takes priority over field change."""
        _make_note(db, uuid="m-5", anki_id=8005,
                   field_1="<p>NewFront</p>", field_2="<p>Back</p>",
                   deck_name="Default", note_type="Basic")
        db.upsert_anki_note(
            anki_id=8005,
            note_type="Basic (reversed card)",
            field_1="<p>OldFront</p>",
            field_2="<p>Back</p>",
            tags=[],
            deck_name="Default",
            mod_timestamp=None,
        )
        rows = db.get_comparison_rows(exclude_synced=True)
        target = [r for r in rows if r["anki_id"] == 8005]
        assert len(target) == 1
        assert target[0]["status"] == "modify_type"


class TestSimilaritySearch:

    def test_exact_match_returns_anki_id(self, db):
        _make_anki_note(db, anki_id=5001, field_1="<p>Q</p>", field_2="<p>A</p>")
        results = db.similarity_search("<p>Q</p>", "<p>A</p>", "Basic")
        assert results == [5001]

    def test_no_match_returns_empty(self, db):
        _make_anki_note(db, anki_id=5001, field_1="<p>Q</p>", field_2="<p>A</p>")
        assert db.similarity_search("<p>Different</p>", "<p>A</p>", "Basic") == []

    def test_stem_stripped_before_compare(self, db):
        _make_anki_note(db, anki_id=5002, field_1="<p>Q</p>", field_2="<p>A</p>")
        results = db.similarity_search("<p>Q</p><br><b>note-stem</b>", "<p>A</p>", "Basic")
        assert results == [5002]

    def test_linked_note_excluded(self, db):
        """Anki note already linked to a vault note — not returned as candidate."""
        _make_note(db, uuid="v-1", anki_id=5003, field_1="<p>Q</p>", field_2="<p>A</p>")
        _make_anki_note(db, anki_id=5003, field_1="<p>Q</p>", field_2="<p>A</p>")
        assert db.similarity_search("<p>Q</p>", "<p>A</p>", "Basic") == []

    def test_note_type_scoped(self, db):
        _make_anki_note(db, anki_id=5004, note_type="Cloze",
                        field_1="<p>Q</p>", field_2="<p>A</p>")
        assert db.similarity_search("<p>Q</p>", "<p>A</p>", "Basic") == []

    def test_multiple_candidates_returned(self, db):
        _make_anki_note(db, anki_id=5005, field_1="<p>Q</p>", field_2="<p>A</p>")
        _make_anki_note(db, anki_id=5006, field_1="<p>Q</p>", field_2="<p>A</p>")
        results = db.similarity_search("<p>Q</p>", "<p>A</p>", "Basic")
        assert set(results) == {5005, 5006}

    def test_null_field_2_matches(self, db):
        _make_anki_note(db, anki_id=5007, note_type="Cloze",
                        field_1="<p>{{c1::text}}</p>", field_2=None)
        results = db.similarity_search("<p>{{c1::text}}</p>", None, "Cloze")
        assert results == [5007]

    def test_revert_note_to_anki_copies_fields(self, db):
        _make_note(db, uuid="rv-1", anki_id=7001,
                   field_1="<p>VaultFront</p>", field_2="<p>VaultBack</p>")
        _make_anki_note(db, anki_id=7001,
                        field_1="<p>AnkiFront</p>", field_2="<p>AnkiBack</p>")
        result = db.revert_note_to_anki("rv-1")
        assert result is True
        note = db.get_note("rv-1")
        assert note["field_1"] == "<p>AnkiFront</p>"
        assert note["field_2"] == "<p>AnkiBack</p>"

    def test_revert_note_to_anki_no_anki_id_returns_false(self, db):
        _make_note(db, uuid="rv-2", anki_id=None)
        assert db.revert_note_to_anki("rv-2") is False

    def test_revert_note_to_anki_no_snapshot_returns_false(self, db):
        _make_note(db, uuid="rv-3", anki_id=7003)
        # No matching row in anki_notes — anki snapshot not populated
        assert db.revert_note_to_anki("rv-3") is False

    def test_revert_makes_note_synced_in_view(self, db):
        """After revert, note_comparison status should be 'synced'."""
        _make_note(db, uuid="rv-4", anki_id=7004,
                   field_1="<p>VaultFront</p>", field_2="<p>VaultBack</p>",
                   deck_name="Default")
        _make_anki_note(db, anki_id=7004,
                        field_1="<p>AnkiFront</p>", field_2="<p>AnkiBack</p>",
                        deck_name="Default")
        db.revert_note_to_anki("rv-4")
        rows = db.get_comparison_rows(exclude_synced=False)
        target = [r for r in rows if r["anki_id"] == 7004]
        assert target[0]["status"] == "synced"


class TestAtomicId:

    def test_set_and_get_file_atomic_id(self, db):
        db.set_file_atomic_id("deck/note.md", "test-uuid-1234")
        assert db.get_file_atomic_id("deck/note.md") == "test-uuid-1234"

    def test_get_atomic_id_missing_returns_none(self, db):
        assert db.get_file_atomic_id("nonexistent.md") is None

    def test_set_atomic_id_updates_existing(self, db):
        db.set_file_hash("deck/note.md", "sha256abc")
        db.set_file_atomic_id("deck/note.md", "uuid-v1")
        db.set_file_atomic_id("deck/note.md", "uuid-v2")
        assert db.get_file_atomic_id("deck/note.md") == "uuid-v2"


class TestGetNoteByContent:

    def test_returns_single_match(self, db):
        _make_note(db, uuid="u1", file_path="deck/a.md", note_type="Basic", field_1="<p>Q</p>")
        row = db.get_note_by_content("deck/a.md", "Basic", "<p>Q</p>")
        assert row is not None
        assert row["id"] == "u1"

    def test_returns_none_when_no_match(self, db):
        assert db.get_note_by_content("deck/a.md", "Basic", "<p>Q</p>") is None

    def test_returns_none_when_ambiguous(self, db):
        _make_note(db, uuid="u1", file_path="deck/a.md", line_number=1, note_type="Basic", field_1="<p>Q</p>")
        _make_note(db, uuid="u2", file_path="deck/a.md", line_number=2, note_type="Basic", field_1="<p>Q</p>")
        assert db.get_note_by_content("deck/a.md", "Basic", "<p>Q</p>") is None

    def test_note_type_scoped(self, db):
        _make_note(db, uuid="u1", file_path="deck/a.md", note_type="Basic", field_1="<p>Q</p>")
        assert db.get_note_by_content("deck/a.md", "Cloze", "<p>Q</p>") is None

    def test_matches_null_field_1(self, db):
        _make_note(db, uuid="u1", file_path="deck/a.md", note_type="Basic", field_1=None)
        row = db.get_note_by_content("deck/a.md", "Basic", None)
        assert row is not None


class TestUpdateAnkiNoteFields:

    def test_updates_field_values(self, db):
        db.upsert_anki_note(99, "Basic", "old_front", "old_back", [], "Default", 1000)
        db.update_anki_note_fields(99, "new_front", "new_back")
        row = db._conn.execute(
            "SELECT field_1, field_2 FROM anki_notes WHERE anki_id = 99"
        ).fetchone()
        assert row["field_1"] == "new_front"
        assert row["field_2"] == "new_back"

    def test_accepts_null_field_2(self, db):
        db.upsert_anki_note(99, "Basic", "q", "a", [], "Default", 1000)
        db.update_anki_note_fields(99, "q", None)
        row = db._conn.execute(
            "SELECT field_2 FROM anki_notes WHERE anki_id = 99"
        ).fetchone()
        assert row["field_2"] is None

    def test_noop_on_unknown_id(self, db):
        db.update_anki_note_fields(9999, "x", "y")  # should not raise


class TestClearAnkiNotes:

    def test_wipes_all_rows(self, db):
        db.upsert_anki_note(1, "Basic", "f1", "f2", [], "Default", 100)
        db.upsert_anki_note(2, "Basic", "g1", "g2", [], "Default", 100)
        db.clear_anki_notes()
        n = db._conn.execute("SELECT COUNT(*) AS n FROM anki_notes").fetchone()["n"]
        assert n == 0

    def test_idempotent_on_empty(self, db):
        db.clear_anki_notes()
        db.clear_anki_notes()  # should not raise


class TestModifyFieldStatuses:

    def _anki(self, db, anki_id, f1, f2, deck="Default"):
        db.upsert_anki_note(anki_id, "Basic", f1, f2, [], deck, None)

    def test_modify_field_1_only(self, db):
        _make_note(db, uuid="mf-1", anki_id=9101, field_1="<p>New</p>", field_2="<p>Back</p>")
        self._anki(db, 9101, "<p>Old</p>", "<p>Back</p>")
        rows = db.get_comparison_rows()
        target = next(r for r in rows if r["anki_id"] == 9101)
        assert target["status"] == "modify_field_1"

    def test_modify_field_2_only(self, db):
        _make_note(db, uuid="mf-2", anki_id=9102, field_1="<p>Same</p>", field_2="<p>New</p>")
        self._anki(db, 9102, "<p>Same</p>", "<p>Old</p>")
        rows = db.get_comparison_rows()
        target = next(r for r in rows if r["anki_id"] == 9102)
        assert target["status"] == "modify_field_2"

    def test_modify_fields_both(self, db):
        _make_note(db, uuid="mf-3", anki_id=9103, field_1="<p>NewF</p>", field_2="<p>NewB</p>")
        self._anki(db, 9103, "<p>OldF</p>", "<p>OldB</p>")
        rows = db.get_comparison_rows()
        target = next(r for r in rows if r["anki_id"] == 9103)
        assert target["status"] == "modify_fields"

    def test_stem_suffix_not_a_field_change(self, db):
        _make_note(db, uuid="mf-4", anki_id=9104,
                   field_1="<p>Q</p><br><b>stem</b>", field_2="<p>A</p>")
        self._anki(db, 9104, "<p>Q</p>", "<p>A</p>")
        rows = db.get_comparison_rows(exclude_synced=False)
        target = next(r for r in rows if r["anki_id"] == 9104)
        assert target["status"] == "synced"


class TestGetComparisonSummary:

    def test_returns_status_counts(self, db):
        # Two vault notes without anki_id → 'not_in_anki'
        _make_note(db, uuid="u1", anki_id=None)
        _make_note(db, uuid="u2", anki_id=None, line_number=20)
        summary = db.get_comparison_summary()
        assert any(r["status"] == "not_in_anki" and r["n"] == 2 for r in summary)

    def test_synced_status(self, db):
        _make_note(db, uuid="u1", anki_id=10)
        db.upsert_anki_note(10, "Basic", "<p>Front</p>", "<p>Back</p>", [], "Default", 1000)
        summary = db.get_comparison_summary()
        assert any(r["status"] == "synced" for r in summary)

    def test_empty_db_returns_empty_list(self, db):
        assert db.get_comparison_summary() == []
