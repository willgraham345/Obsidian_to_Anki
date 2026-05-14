import pytest
from unittest.mock import patch, MagicMock, mock_open, call
import os
import re
import hashlib

from src.obsidian_to_anki.file import File, _extract_images, _db_upsert_note
from src.obsidian_to_anki.note import RegexNote
from src.obsidian_to_anki.anki_connect import AnkiConnect
from src.obsidian_to_anki import globals
from src.obsidian_to_anki.utils import findignore, spans
from src.obsidian_to_anki.db import NoteDB


class TestFile:

    @pytest.fixture(autouse=True)
    def setup(self):
        globals.CONFIG_DATA = {
            "Vault": "",
            "DECK_LINE": "Deck",
            "TAG_LINE": "Tags",
            "Comment": False,
            "ATOMICS": {}
        }
        globals.VAULT_PATH_REGEXP = re.compile(r"VaultName/(.*)")
        globals.DECK_REGEXP = re.compile(r"^Deck(?:\n|: )(.*)", re.MULTILINE)
        globals.TAG_REGEXP = re.compile(r"^Tags(?:\n|: )(.*)", re.MULTILINE)
        globals.OBS_INLINE_MATH_REGEXP = re.compile(r"(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)", re.DOTALL)
        globals.OBS_DISPLAY_MATH_REGEXP = re.compile(r"\$\$(.*?)\$\$", re.DOTALL)
        globals.OBS_CODE_REGEXP = re.compile(r"(?<!`)`(?!`)(.*?)(?<!`)`(?!`)", re.DOTALL)
        globals.OBS_DISPLAY_CODE_REGEXP = re.compile(r"```[\s\S]*?```")
        globals.EXISTING_IDS = []
        globals.FIELDS_DICT = {}
        globals.NOTE_DICT_TEMPLATE = {"tags": [], "deckName": "Default"}
        globals.ID_PREFIX = "ID: "
        globals.TAG_SEP = " "
        globals.NOTE_DB = None  # disable DB in file tests
        with patch('builtins.open', mock_open(read_data="")):
            yield

    @patch('src.obsidian_to_anki.file.os.path.abspath', return_value="/mock/path/to/file.md")
    def test_file_init_no_vault(self, mock_abspath):
        file_instance = File("file.md")
        assert file_instance.filename == "file.md"
        assert file_instance.path == "/mock/path/to/file.md"
        assert file_instance.url == ""
        assert file_instance.file == ""

    @patch('src.obsidian_to_anki.file.os.path.abspath', return_value="/mock/path/to/VaultName/sub/file.md")
    def test_file_init_with_vault(self, mock_abspath):
        globals.CONFIG_DATA["Vault"] = "VaultName"
        globals.VAULT_PATH_REGEXP = re.compile(r"VaultName/(.*)")
        file_instance = File("file.md")
        assert file_instance.url == "obsidian://open?vault=VaultName&file=sub/file.md"

    def test_hash_property(self):
        file_instance = File("dummy.md")
        file_instance.file = "test content"
        expected_hash = hashlib.sha256("test content".encode('utf-8')).hexdigest()
        assert file_instance.hash == expected_hash

    def test_setup_frozen_fields_dict(self):
        file_instance = File("dummy.md")
        globals.FIELDS_DICT = {"NoteType1": ["Field1", "Field2"], "NoteType2": ["FieldA"]}
        file_instance.setup_frozen_fields_dict()
        assert file_instance.frozen_fields_dict == {
            "NoteType1": {"Field1": "", "Field2": ""},
            "NoteType2": {"FieldA": ""}
        }

    def test_setup_target_deck(self):
        file_instance = File("dummy.md")
        file_instance.file = "Deck: MyDeck"
        file_instance.setup_target_deck()
        assert file_instance.target_deck == "MyDeck"

        file_instance.file = "No Deck Line"
        file_instance.setup_target_deck()
        assert file_instance.target_deck == globals.NOTE_DICT_TEMPLATE["deckName"]

    @patch('src.obsidian_to_anki.file.os.path.abspath',
           return_value="/vault/Docs/Programming_and_OS/Cpp/templates.md")
    def test_setup_target_deck_folder_first_match(self, _):
        globals.CONFIG_DATA["Vault"] = "vault"
        globals.VAULT_PATH_REGEXP = re.compile(r"vault/(.*)")
        globals.CONFIG_DATA["FOLDER_DECKS"] = [
            (re.compile(r"Docs/Programming_and_OS/Cpp"), "Cpp"),
            (re.compile(r"Docs/Programming_and_OS/.*"), "Programming"),
        ]
        file_instance = File("templates.md")
        file_instance.file = "no deck line here"
        file_instance.setup_target_deck()
        assert file_instance.target_deck == "Cpp"

    @patch('src.obsidian_to_anki.file.os.path.abspath',
           return_value="/vault/Docs/Programming_and_OS/Python/foo.md")
    def test_setup_target_deck_folder_second_match(self, _):
        globals.CONFIG_DATA["Vault"] = "vault"
        globals.VAULT_PATH_REGEXP = re.compile(r"vault/(.*)")
        globals.CONFIG_DATA["FOLDER_DECKS"] = [
            (re.compile(r"Docs/Programming_and_OS/Cpp"), "Cpp"),
            (re.compile(r"Docs/Programming_and_OS/.*"), "Programming"),
        ]
        file_instance = File("foo.md")
        file_instance.file = "no deck line here"
        file_instance.setup_target_deck()
        assert file_instance.target_deck == "Programming"

    @patch('src.obsidian_to_anki.file.os.path.abspath',
           return_value="/vault/Docs/Programming_and_OS/Cpp/templates.md")
    def test_setup_target_deck_priority_file_marker_wins(self, _):
        globals.CONFIG_DATA["Vault"] = "vault"
        globals.VAULT_PATH_REGEXP = re.compile(r"vault/(.*)")
        globals.CONFIG_DATA["FOLDER_DECKS"] = [
            (re.compile(r"Docs/Programming_and_OS/Cpp"), "Cpp"),
        ]
        file_instance = File("templates.md")
        file_instance.file = "Deck: ExplicitDeck"
        file_instance.setup_target_deck()
        assert file_instance.target_deck == "ExplicitDeck"

    def test_setup_target_deck_no_vault_skips_folder(self):
        globals.CONFIG_DATA["Vault"] = ""
        globals.CONFIG_DATA["FOLDER_DECKS"] = [
            (re.compile(r".*"), "ShouldNotMatch"),
        ]
        file_instance = File("dummy.md")
        file_instance.file = "no deck line here"
        file_instance.setup_target_deck()
        assert file_instance.target_deck == globals.NOTE_DICT_TEMPLATE["deckName"]

    def test_setup_target_deck_no_folder_decks_key(self):
        globals.CONFIG_DATA["Vault"] = "vault"
        globals.CONFIG_DATA.pop("FOLDER_DECKS", None)
        file_instance = File("dummy.md")
        file_instance.file = "no deck line here"
        file_instance.setup_target_deck()
        assert file_instance.target_deck == globals.NOTE_DICT_TEMPLATE["deckName"]

    @patch('src.obsidian_to_anki.file.os.path.abspath',
           return_value="/vault/Biology/genetics.md")
    def test_setup_target_deck_no_matching_folder(self, _):
        globals.CONFIG_DATA["Vault"] = "vault"
        globals.VAULT_PATH_REGEXP = re.compile(r"vault/(.*)")
        globals.CONFIG_DATA["FOLDER_DECKS"] = [
            (re.compile(r"Docs/Programming_and_OS/Cpp"), "Cpp"),
        ]
        file_instance = File("genetics.md")
        file_instance.file = "no deck line here"
        file_instance.setup_target_deck()
        assert file_instance.target_deck == "Obsidian Unmatched Transfer"

    def test_setup_global_tags(self):
        file_instance = File("dummy.md")
        file_instance.file = "Tags: tag1 tag2"
        file_instance.setup_global_tags()
        assert file_instance.global_tags == "tag1 tag2"

        file_instance.file = "No Tags Line"
        file_instance.setup_global_tags()
        assert file_instance.global_tags == ""

    @patch('src.obsidian_to_anki.file.spans')
    def test_add_spans_to_ignore(self, mock_spans):
        file_instance = File("dummy.md")
        file_instance.file = "some content"
        file_instance.ignore_spans = []

        mock_spans.side_effect = [[(0, 10)], [(11, 20)], [(21, 30)], [(31, 40)]]

        file_instance.add_spans_to_ignore()

        assert len(file_instance.ignore_spans) == 4
        mock_spans.assert_has_calls([
            call(globals.OBS_INLINE_MATH_REGEXP, file_instance.file),
            call(globals.OBS_DISPLAY_MATH_REGEXP, file_instance.file),
            call(globals.OBS_CODE_REGEXP, file_instance.file),
            call(globals.OBS_DISPLAY_CODE_REGEXP, file_instance.file),
        ])

    @patch('src.obsidian_to_anki.file.File.setup_frozen_fields_dict')
    @patch('src.obsidian_to_anki.file.File.setup_target_deck')
    @patch('src.obsidian_to_anki.file.File.setup_global_tags')
    @patch('src.obsidian_to_anki.file.File.add_spans_to_ignore')
    @patch('src.obsidian_to_anki.file.File.search')
    def test_scan_file_calls_search_for_atomics(self, mock_search, mock_add_spans, *_):
        globals.CONFIG_DATA["ATOMICS"] = {"MyNoteType": "MY_REGEX"}
        file_instance = File("dummy.md")
        file_instance.file = "some content"

        file_instance.scan_file()

        mock_add_spans.assert_called_once()
        mock_search.assert_called_once_with("MyNoteType", "MY_REGEX")
        assert file_instance.notes_to_delete == []

    @patch('src.obsidian_to_anki.file.findignore')
    @patch('src.obsidian_to_anki.file.RegexNote')
    def test_search(self, MockRegexNote, mock_findignore):
        file_instance = File("dummy.md")
        file_instance.file = "test content"
        file_instance.ignore_spans = []
        file_instance.url = "mock_url"
        file_instance.frozen_fields_dict = {}
        file_instance.target_deck = "Default"
        file_instance.global_tags = ""
        file_instance.notes_to_edit = []
        file_instance.notes_to_add = []
        file_instance.regex_id_indexes = []
        file_instance.uuid_for_regex_add = []
        file_instance.notes_to_delete = []

        # Mock matches for findignore
        mock_match_id_tags = MagicMock(group=lambda x: "123" if x == 1 else "tag1", span=lambda: (0, 10))
        mock_match_id = MagicMock(group=lambda x: "456" if x == 1 else None, span=lambda: (11, 20))
        mock_match_tags = MagicMock(group=lambda x: "tag2" if x == 1 else None, end=lambda: 30, span=lambda: (21, 30))
        mock_match_no_id_tags = MagicMock(group=lambda x: "content" if x == 1 else None, end=lambda: 40, span=lambda: (31, 40))

        mock_findignore.side_effect = [
            [mock_match_id_tags], # regexp_tags_id
            [mock_match_id],      # regexp_id
            [mock_match_tags],    # regexp_tags
            [mock_match_no_id_tags] # regexp_plain
        ]

        # Mock RegexNote parsing
        mock_parsed_id_tags = MagicMock(id=123, note={"tags": []})
        mock_parsed_id = MagicMock(id=456, note={"tags": []})
        mock_parsed_tags = MagicMock(id=None, note={"tags": []})
        mock_parsed_no_id_tags = MagicMock(id=None, note={"tags": []})

        MockRegexNote.return_value.parse.side_effect = [
            mock_parsed_id_tags,
            mock_parsed_id,
            mock_parsed_tags,
            mock_parsed_no_id_tags
        ]

        globals.EXISTING_IDS = [123, 456]
        MockRegexNote.TAG_REGEXP_STR = ""
        MockRegexNote.ID_REGEXP_STR = ""

        file_instance.search("MyNoteType", "MY_REGEX")

        assert len(file_instance.notes_to_edit) == 2
        assert file_instance.notes_to_edit[0] == mock_parsed_id_tags
        assert file_instance.notes_to_edit[1] == mock_parsed_id
        assert len(file_instance.notes_to_add) == 2
        assert file_instance.notes_to_add[0] == mock_parsed_tags.note
        assert file_instance.notes_to_add[1] == mock_parsed_no_id_tags.note
        assert len(file_instance.regex_id_indexes) == 2
        assert file_instance.regex_id_indexes[0] == 30
        assert file_instance.regex_id_indexes[1] == 40
        assert len(file_instance.ignore_spans) == 4

    @patch('src.obsidian_to_anki.file.AnkiConnect.request')
    def test_get_add_notes(self, mock_anki_request):
        file_instance = File("dummy.md")
        file_instance.notes_to_add = [{"note": "add1"}, {"note": "add2"}]
        result = file_instance.get_add_notes()
        mock_anki_request.assert_has_calls([
            call("addNote", note={"note": "add1"}),
            call("addNote", note={"note": "add2"}),
            call("multi", actions=[mock_anki_request.return_value, mock_anki_request.return_value])
        ], any_order=True)
        assert result == mock_anki_request.return_value

    @patch('src.obsidian_to_anki.file.AnkiConnect.request')
    def test_get_delete_notes(self, mock_anki_request):
        file_instance = File("dummy.md")
        file_instance.notes_to_delete = [1, 2, 3]
        result = file_instance.get_delete_notes()
        mock_anki_request.assert_called_once_with("deleteNotes", notes=[1, 2, 3])
        assert result == mock_anki_request.return_value

    @patch('src.obsidian_to_anki.file.AnkiConnect.request')
    def test_get_update_fields(self, mock_anki_request):
        file_instance = File("dummy.md")
        mock_parsed1 = MagicMock(id=1, note={"fields": {"F1": "V1"}, "audio": []})
        mock_parsed2 = MagicMock(id=2, note={"fields": {"F2": "V2"}, "audio": []})
        file_instance.notes_to_edit = [mock_parsed1, mock_parsed2]
        result = file_instance.get_update_fields()
        mock_anki_request.assert_has_calls([
            call("updateNoteFields", note={"id": 1, "fields": {"F1": "V1"}, "audio": []}),
            call("updateNoteFields", note={"id": 2, "fields": {"F2": "V2"}, "audio": []}),
            call("multi", actions=[mock_anki_request.return_value, mock_anki_request.return_value])
        ], any_order=True)
        assert result == mock_anki_request.return_value

    @patch('src.obsidian_to_anki.file.AnkiConnect.request')
    def test_get_note_info(self, mock_anki_request):
        file_instance = File("dummy.md")
        mock_parsed1 = MagicMock(id=1)
        mock_parsed2 = MagicMock(id=2)
        file_instance.notes_to_edit = [mock_parsed1, mock_parsed2]
        result = file_instance.get_note_info()
        mock_anki_request.assert_called_once_with("notesInfo", notes=[1, 2])
        assert result == mock_anki_request.return_value

    def test_get_cards(self):
        file_instance = File("dummy.md")
        file_instance.card_ids = [
            {"cards": ["card1", "card2"]},
            {"cards": ["card3"]}
        ]
        file_instance.get_cards()
        assert file_instance.cards == ["card1", "card2", "card3"]

    @patch('src.obsidian_to_anki.file.AnkiConnect.request')
    def test_get_change_decks(self, mock_anki_request):
        file_instance = File("dummy.md")
        file_instance.cards = ["cardA", "cardB"]
        file_instance.target_deck = "MyDeck"
        result = file_instance.get_change_decks()
        mock_anki_request.assert_called_once_with("changeDeck", cards=["cardA", "cardB"], deck="MyDeck")
        assert result == mock_anki_request.return_value

    @patch('src.obsidian_to_anki.file.AnkiConnect.request')
    def test_get_clear_tags(self, mock_anki_request):
        file_instance = File("dummy.md")
        mock_parsed1 = MagicMock(id=1)
        mock_parsed2 = MagicMock(id=2)
        file_instance.notes_to_edit = [mock_parsed1, mock_parsed2]
        file_instance.tags = ["existing_tag1", "existing_tag2"]
        result = file_instance.get_clear_tags()
        mock_anki_request.assert_called_once_with("removeTags", notes=[1, 2], tags="existing_tag1 existing_tag2")
        assert result == mock_anki_request.return_value

    @patch('src.obsidian_to_anki.file.AnkiConnect.request')
    def test_get_add_tags(self, mock_anki_request):
        file_instance = File("dummy.md")
        mock_parsed1 = MagicMock(id=1, note={"tags": ["new_tag1"]})
        mock_parsed2 = MagicMock(id=2, note={"tags": ["new_tag2", "new_tag3"]})
        file_instance.notes_to_edit = [mock_parsed1, mock_parsed2]
        file_instance.global_tags = "global_tag"
        result = file_instance.get_add_tags()
        mock_anki_request.assert_has_calls([
            call("addTags", notes=[1], tags="new_tag1 global_tag"),
            call("addTags", notes=[2], tags="new_tag2 new_tag3 global_tag"),
            call("multi", actions=[mock_anki_request.return_value, mock_anki_request.return_value])
        ], any_order=True)
        assert result == mock_anki_request.return_value


class TestExtractImages:

    def test_single_image(self):
        fields = {"Front": '<img src="cat.png">', "Back": "no image"}
        assert _extract_images(fields) == ["cat.png"]

    def test_multiple_images(self):
        fields = {"Front": '<img src="a.png"><img src="b.jpg">'}
        assert sorted(_extract_images(fields)) == ["a.png", "b.jpg"]

    def test_images_across_fields(self):
        fields = {"F1": '<img src="x.png">', "F2": '<img src="y.png">'}
        assert sorted(_extract_images(fields)) == ["x.png", "y.png"]

    def test_no_images(self):
        assert _extract_images({"Front": "<p>text</p>"}) == []

    def test_empty_fields(self):
        assert _extract_images({}) == []


class TestDbUpsertNote:

    @pytest.fixture(autouse=True)
    def setup(self):
        db = NoteDB(":memory:")
        globals.NOTE_DB = db
        yield
        db.close()
        globals.NOTE_DB = None

    def _make_parsed(self, anki_id=None, model="Basic", f1="<p>Q</p>", f2="<p>A</p>"):
        note = {
            "modelName": model,
            "fields": {"Front": f1, "Back": f2},
            "tags": ["tag1"],
            "deckName": "Default",
        }
        return MagicMock(id=anki_id, note=note)

    def test_inserts_new_note_returns_uuid(self):
        parsed = self._make_parsed()
        uuid = _db_upsert_note(parsed, "deck/a.md", 5)
        assert uuid is not None
        row = globals.NOTE_DB.get_note(uuid)
        assert row["field_1"] == "<p>Q</p>"
        assert row["file_path"] == "deck/a.md"
        assert row["line_number"] == 5

    def test_returns_none_when_db_not_set(self):
        globals.NOTE_DB = None
        parsed = self._make_parsed()
        assert _db_upsert_note(parsed, "deck/a.md", 5) is None

    def test_reuses_existing_uuid_by_location(self):
        parsed = self._make_parsed()
        uuid1 = _db_upsert_note(parsed, "deck/a.md", 5)
        uuid2 = _db_upsert_note(parsed, "deck/a.md", 5)
        assert uuid1 == uuid2
        assert len(globals.NOTE_DB.get_notes_for_file("deck/a.md")) == 1

    def test_extracts_images_into_db(self):
        parsed = self._make_parsed(f1='<img src="diagram.png">')
        uuid = _db_upsert_note(parsed, "deck/a.md", 1)
        row = globals.NOTE_DB.get_note(uuid)
        import json
        assert "diagram.png" in json.loads(row["image_paths"])


class TestApplyChangeDetection:

    @pytest.fixture(autouse=True)
    def setup(self):
        globals.CONFIG_DATA = {
            "Vault": "",
            "DECK_LINE": "Deck",
            "TAG_LINE": "Tags",
            "Comment": False,
            "ATOMICS": {}
        }
        globals.NOTE_DICT_TEMPLATE = {"tags": [], "deckName": "Default"}
        db = NoteDB(":memory:")
        globals.NOTE_DB = db
        globals.EXISTING_IDS = []
        with patch('builtins.open', mock_open(read_data="")):
            yield
        db.close()
        globals.NOTE_DB = None

    def _file(self):
        with patch('src.obsidian_to_anki.file.os.path.abspath', return_value="/mock/file.md"):
            f = File("file.md")
        f.notes_to_delete = []
        return f

    def _parsed(self, model="Basic", f1="<p>New</p>", f2="<p>A</p>"):
        note = {"modelName": model, "fields": {"Front": f1, "Back": f2},
                "tags": [], "deckName": "Default", "audio": []}
        return globals.Note_and_id(note=note, id=None)

    def test_no_db_passthrough(self):
        globals.NOTE_DB = None
        f = self._file()
        parsed = self._parsed()
        result = f._apply_change_detection(parsed, "deck/a.md", 5)
        assert result is parsed

    def test_parsed_has_id_passthrough(self):
        f = self._file()
        note = {"modelName": "Basic", "fields": {"Front": "<p>Q</p>", "Back": "<p>A</p>"},
                "tags": [], "deckName": "Default", "audio": []}
        parsed = globals.Note_and_id(note=note, id=123)
        result = f._apply_change_detection(parsed, "deck/a.md", 5)
        assert result is parsed

    def test_changed_content_routes_to_edit(self):
        globals.NOTE_DB.upsert_note(
            uuid="u1", anki_id=42, file_path="deck/a.md", line_number=5,
            note_type="Basic", field_1="<p>Old</p>", field_2="<p>A</p>",
            image_paths=[], tags=[], deck_name="Default"
        )
        globals.EXISTING_IDS = [42]
        f = self._file()
        parsed = self._parsed(f1="<p>New</p>")
        result = f._apply_change_detection(parsed, "deck/a.md", 5)
        assert result.id == 42
        assert f.notes_to_delete == []

    def test_changed_content_stale_id_passthrough(self):
        """ID not in Anki: note falls through to re-add, not in-place update."""
        globals.NOTE_DB.upsert_note(
            uuid="u1", anki_id=42, file_path="deck/a.md", line_number=5,
            note_type="Basic", field_1="<p>Old</p>", field_2="<p>A</p>",
            image_paths=[], tags=[], deck_name="Default"
        )
        globals.EXISTING_IDS = []  # 42 is gone from Anki
        f = self._file()
        parsed = self._parsed(f1="<p>New</p>")
        result = f._apply_change_detection(parsed, "deck/a.md", 5)
        assert result.id is None
        assert f.notes_to_delete == []

    def test_unchanged_content_passthrough(self):
        globals.NOTE_DB.upsert_note(
            uuid="u1", anki_id=42, file_path="deck/a.md", line_number=5,
            note_type="Basic", field_1="<p>Same</p>", field_2="<p>A</p>",
            image_paths=[], tags=[], deck_name="Default"
        )
        globals.EXISTING_IDS = [42]
        f = self._file()
        parsed = self._parsed(f1="<p>Same</p>", f2="<p>A</p>")
        result = f._apply_change_detection(parsed, "deck/a.md", 5)
        assert result.id is None
        assert f.notes_to_delete == []

    def test_stem_suffix_not_treated_as_change(self):
        """field_1 differs only by <br><b>stem</b> suffix → no modification routed."""
        globals.NOTE_DB.upsert_note(
            uuid="u1", anki_id=42, file_path="deck/a.md", line_number=5,
            note_type="Basic", field_1="<p>Same</p>", field_2="<p>A</p>",
            image_paths=[], tags=[], deck_name="Default"
        )
        globals.EXISTING_IDS = [42]
        f = self._file()
        parsed = self._parsed(f1="<p>Same</p><br><b>note-stem</b>", f2="<p>A</p>")
        result = f._apply_change_detection(parsed, "deck/a.md", 5)
        assert result.id is None
        assert f.notes_to_delete == []

    def test_no_anki_id_passthrough(self):
        globals.NOTE_DB.upsert_note(
            uuid="u1", anki_id=None, file_path="deck/a.md", line_number=5,
            note_type="Basic", field_1="<p>Old</p>", field_2="<p>A</p>",
            image_paths=[], tags=[], deck_name="Default"
        )
        f = self._file()
        parsed = self._parsed(f1="<p>New</p>")
        result = f._apply_change_detection(parsed, "deck/a.md", 5)
        assert result.id is None
        assert f.notes_to_delete == []


class TestUpdateDbAnkiIds:

    @pytest.fixture(autouse=True)
    def setup(self):
        db = NoteDB(":memory:")
        globals.NOTE_DB = db
        globals.CONFIG_DATA = {
            "Vault": "",
            "DECK_LINE": "Deck",
            "TAG_LINE": "Tags",
            "Comment": False,
            "ATOMICS": {}
        }
        globals.NOTE_DICT_TEMPLATE = {"tags": [], "deckName": "Default"}
        globals.EXISTING_IDS = []
        with patch('builtins.open', mock_open(read_data="")):
            yield
        db.close()
        globals.NOTE_DB = None

    def test_marks_synced_for_regex_notes(self):
        db = globals.NOTE_DB
        db.upsert_note(uuid="u1", anki_id=None, file_path="a.md", line_number=1,
                       note_type="Basic", field_1="q", field_2="a",
                       image_paths=[], tags=[], deck_name="Default")
        with patch('src.obsidian_to_anki.file.os.path.abspath', return_value="/mock/a.md"):
            f = File("a.md")
        f.regex_id_indexes = [10]
        f.uuid_for_regex_add = ["u1"]
        f.note_ids = [999]
        f.update_db_anki_ids()
        row = db.get_note("u1")
        assert row["anki_id"] == 999

    def test_no_db_is_noop(self):
        globals.NOTE_DB = None
        with patch('src.obsidian_to_anki.file.os.path.abspath', return_value="/mock/a.md"):
            f = File("a.md")
        f.regex_id_indexes = []
        f.uuid_for_regex_add = []
        f.note_ids = []
        f.update_db_anki_ids()  # should not raise

    def test_no_note_ids_attr_is_noop(self):
        with patch('src.obsidian_to_anki.file.os.path.abspath', return_value="/mock/a.md"):
            f = File("a.md")
        f.update_db_anki_ids()  # should not raise


class TestAtomicStateFlow:

    @pytest.fixture(autouse=True)
    def setup(self):
        globals.CONFIG_DATA = {
            "Vault": "",
            "DECK_LINE": "Deck",
            "TAG_LINE": "Tags",
            "Comment": False,
            "ATOMICS": {}
        }
        globals.VAULT_PATH_REGEXP = re.compile(r"VaultName/(.*)")
        globals.DECK_REGEXP = re.compile(r"^Deck(?:\n|: )(.*)", re.MULTILINE)
        globals.TAG_REGEXP = re.compile(r"^Tags(?:\n|: )(.*)", re.MULTILINE)
        globals.OBS_INLINE_MATH_REGEXP = re.compile(r"(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)", re.DOTALL)
        globals.OBS_DISPLAY_MATH_REGEXP = re.compile(r"\$\$(.*?)\$\$", re.DOTALL)
        globals.OBS_CODE_REGEXP = re.compile(r"(?<!`)`(?!`)(.*?)(?<!`)`(?!`)", re.DOTALL)
        globals.OBS_DISPLAY_CODE_REGEXP = re.compile(r"```[\s\S]*?```")
        globals.NOTE_DICT_TEMPLATE = {"tags": [], "deckName": "Default"}
        globals.FIELDS_DICT = {}
        globals.ID_PREFIX = "ID: "
        globals.TAG_SEP = " "
        globals.EXISTING_IDS = []
        db = NoteDB(":memory:")
        globals.NOTE_DB = db
        with patch('builtins.open', mock_open(read_data="")):
            with patch('src.obsidian_to_anki.file.os.path.abspath', return_value="/mock/a.md"):
                self.file = File("a.md")
        self.file.pending_review = []
        self.db = db
        yield
        db.close()
        globals.NOTE_DB = None
        globals.EXISTING_IDS = []

    def _parsed(self, anki_id=None, model="Basic", f1="<p>Q</p>", f2="<p>A</p>", deck="Default"):
        note = {
            "modelName": model,
            "fields": {"Front": f1, "Back": f2},
            "tags": [],
            "deckName": deck,
            "audio": [],
        }
        return globals.Note_and_id(note=note, id=anki_id)

    def _insert_vault_note(self, uuid="u1", anki_id=None, f1="<p>Q</p>", f2="<p>A</p>",
                           model="Basic", deck="Default"):
        self.db.upsert_note(
            uuid=uuid, anki_id=anki_id, file_path="deck/a.md", line_number=1,
            note_type=model, field_1=f1, field_2=f2,
            image_paths=[], tags=[], deck_name=deck,
        )

    def _insert_anki_snap(self, anki_id=42, note_type="Basic", f1="<p>Q</p>",
                          f2="<p>A</p>", deck="Default"):
        self.db.upsert_anki_note(
            anki_id=anki_id, note_type=note_type, field_1=f1, field_2=f2,
            tags=[], deck_name=deck, mod_timestamp=None,
        )

    # --- DB=None / uuid=None fallbacks ---

    def test_db_none_has_id_in_existing_ids_returns_edit(self):
        globals.NOTE_DB = None
        globals.EXISTING_IDS = [42]
        parsed = self._parsed(anki_id=42)
        result = self.file._atomic_state_flow(parsed, "deck/a.md", 1, None)
        assert result == 'edit'

    def test_db_none_no_id_returns_add(self):
        globals.NOTE_DB = None
        parsed = self._parsed(anki_id=None)
        result = self.file._atomic_state_flow(parsed, "deck/a.md", 1, None)
        assert result == 'add'

    def test_uuid_none_has_id_in_existing_ids_returns_edit(self):
        globals.EXISTING_IDS = [42]
        parsed = self._parsed(anki_id=42)
        result = self.file._atomic_state_flow(parsed, "deck/a.md", 1, None)
        assert result == 'edit'

    def test_uuid_none_no_id_returns_add(self):
        parsed = self._parsed(anki_id=None)
        result = self.file._atomic_state_flow(parsed, "deck/a.md", 1, None)
        assert result == 'add'

    # --- stale_id branch (parsed.id not in EXISTING_IDS) ---

    def test_stale_id_no_candidates_returns_review(self):
        self._insert_vault_note(anki_id=42)
        globals.EXISTING_IDS = []
        parsed = self._parsed(anki_id=42)
        result = self.file._atomic_state_flow(parsed, "deck/a.md", 1, "u1")
        assert result == 'review'
        row = self.db.get_note("u1")
        assert row["state"] == "stale_id"
        assert row["recommended_action"] == "review"
        assert len(self.file.pending_review) == 1

    def test_stale_id_one_candidate_returns_link(self):
        self._insert_vault_note(anki_id=42)
        globals.EXISTING_IDS = []
        self._insert_anki_snap(anki_id=99, f1="<p>Q</p>", f2="<p>A</p>")
        parsed = self._parsed(anki_id=42)
        result = self.file._atomic_state_flow(parsed, "deck/a.md", 1, "u1")
        assert result == 'link'
        row = self.db.get_note("u1")
        assert row["state"] == "stale_id"
        assert row["recommended_action"] == "link"
        assert self.file.pending_review[0]["uuid"] == "u1"
        assert self.file.pending_review[0]["candidates"] == [99]

    def test_stale_id_multiple_candidates_returns_review(self):
        self._insert_vault_note(anki_id=42)
        globals.EXISTING_IDS = []
        self._insert_anki_snap(anki_id=91, f1="<p>Q</p>", f2="<p>A</p>")
        self._insert_anki_snap(anki_id=92, f1="<p>Q</p>", f2="<p>A</p>")
        parsed = self._parsed(anki_id=42)
        result = self.file._atomic_state_flow(parsed, "deck/a.md", 1, "u1")
        assert result == 'review'
        assert self.db.get_note("u1")["recommended_action"] == "review"

    # --- synced anki_id but no snap row ---

    def test_synced_id_no_snap_falls_back_to_edit(self):
        self._insert_vault_note(anki_id=42)
        globals.EXISTING_IDS = [42]
        parsed = self._parsed(anki_id=42)
        result = self.file._atomic_state_flow(parsed, "deck/a.md", 1, "u1")
        assert result == 'edit'

    # --- modify_type ---

    def test_type_changed_returns_retype(self):
        self._insert_vault_note(anki_id=42, model="Basic")
        self._insert_anki_snap(anki_id=42, note_type="Cloze")
        globals.EXISTING_IDS = [42]
        parsed = self._parsed(anki_id=42, model="Basic")
        result = self.file._atomic_state_flow(parsed, "deck/a.md", 1, "u1")
        assert result == 'retype'
        row = self.db.get_note("u1")
        assert row["state"] == "modify_type"
        assert row["recommended_action"] == "update_type"

    # --- field diff states ---

    def test_both_fields_changed_returns_edit_modify_fields(self):
        self._insert_vault_note(anki_id=42, f1="<p>Q</p>", f2="<p>A</p>")
        self._insert_anki_snap(anki_id=42, f1="<p>OLD</p>", f2="<p>OLD</p>")
        globals.EXISTING_IDS = [42]
        parsed = self._parsed(anki_id=42, f1="<p>Q</p>", f2="<p>A</p>")
        result = self.file._atomic_state_flow(parsed, "deck/a.md", 1, "u1")
        assert result == 'edit'
        row = self.db.get_note("u1")
        assert row["state"] == "modify_fields"
        assert row["recommended_action"] == "update_fields"

    def test_field_1_only_changed_returns_edit_modify_field_1(self):
        self._insert_vault_note(anki_id=42, f1="<p>New</p>", f2="<p>A</p>")
        self._insert_anki_snap(anki_id=42, f1="<p>Old</p>", f2="<p>A</p>")
        globals.EXISTING_IDS = [42]
        parsed = self._parsed(anki_id=42, f1="<p>New</p>", f2="<p>A</p>")
        result = self.file._atomic_state_flow(parsed, "deck/a.md", 1, "u1")
        assert result == 'edit'
        row = self.db.get_note("u1")
        assert row["state"] == "modify_field_1"
        assert row["recommended_action"] == "update_field_1"

    def test_field_2_only_changed_returns_edit_modify_field_2(self):
        self._insert_vault_note(anki_id=42, f1="<p>Q</p>", f2="<p>New</p>")
        self._insert_anki_snap(anki_id=42, f1="<p>Q</p>", f2="<p>Old</p>")
        globals.EXISTING_IDS = [42]
        parsed = self._parsed(anki_id=42, f1="<p>Q</p>", f2="<p>New</p>")
        result = self.file._atomic_state_flow(parsed, "deck/a.md", 1, "u1")
        assert result == 'edit'
        row = self.db.get_note("u1")
        assert row["state"] == "modify_field_2"
        assert row["recommended_action"] == "update_field_2"

    def test_deck_only_changed_returns_edit_modify_deck(self):
        self._insert_vault_note(anki_id=42, f1="<p>Q</p>", f2="<p>A</p>", deck="NewDeck")
        self._insert_anki_snap(anki_id=42, f1="<p>Q</p>", f2="<p>A</p>", deck="OldDeck")
        globals.EXISTING_IDS = [42]
        parsed = self._parsed(anki_id=42, f1="<p>Q</p>", f2="<p>A</p>", deck="NewDeck")
        result = self.file._atomic_state_flow(parsed, "deck/a.md", 1, "u1")
        assert result == 'edit'
        row = self.db.get_note("u1")
        assert row["state"] == "modify_deck"
        assert row["recommended_action"] == "update_deck"

    def test_all_match_returns_skip(self):
        self._insert_vault_note(anki_id=42, f1="<p>Q</p>", f2="<p>A</p>")
        self._insert_anki_snap(anki_id=42, f1="<p>Q</p>", f2="<p>A</p>")
        globals.EXISTING_IDS = [42]
        parsed = self._parsed(anki_id=42, f1="<p>Q</p>", f2="<p>A</p>")
        result = self.file._atomic_state_flow(parsed, "deck/a.md", 1, "u1")
        assert result == 'skip'
        row = self.db.get_note("u1")
        assert row["state"] == "synced"
        assert row["recommended_action"] == "none"

    def test_stem_suffix_treated_as_synced(self):
        """field_1 with stem suffix compares equal to stored field without suffix."""
        self._insert_vault_note(anki_id=42, f1="<p>Q</p>", f2="<p>A</p>")
        self._insert_anki_snap(anki_id=42, f1="<p>Q</p>", f2="<p>A</p>")
        globals.EXISTING_IDS = [42]
        parsed = self._parsed(anki_id=42, f1="<p>Q</p><br><b>note-stem</b>", f2="<p>A</p>")
        result = self.file._atomic_state_flow(parsed, "deck/a.md", 1, "u1")
        assert result == 'skip'

    # --- no anki_id branch ---

    def test_no_anki_id_no_candidates_returns_add(self):
        self._insert_vault_note(anki_id=None)
        parsed = self._parsed(anki_id=None)
        result = self.file._atomic_state_flow(parsed, "deck/a.md", 1, "u1")
        assert result == 'add'
        row = self.db.get_note("u1")
        assert row["state"] == "not_in_anki"
        assert row["recommended_action"] == "add"

    def test_no_anki_id_one_candidate_returns_link(self):
        self._insert_vault_note(anki_id=None)
        self._insert_anki_snap(anki_id=77, f1="<p>Q</p>", f2="<p>A</p>")
        parsed = self._parsed(anki_id=None)
        result = self.file._atomic_state_flow(parsed, "deck/a.md", 1, "u1")
        assert result == 'link'
        row = self.db.get_note("u1")
        assert row["state"] == "not_in_anki"
        assert row["recommended_action"] == "link"
        assert self.file.pending_review[0]["candidates"] == [77]

    def test_no_anki_id_multiple_candidates_returns_review(self):
        self._insert_vault_note(anki_id=None)
        self._insert_anki_snap(anki_id=81, f1="<p>Q</p>", f2="<p>A</p>")
        self._insert_anki_snap(anki_id=82, f1="<p>Q</p>", f2="<p>A</p>")
        parsed = self._parsed(anki_id=None)
        result = self.file._atomic_state_flow(parsed, "deck/a.md", 1, "u1")
        assert result == 'review'
        row = self.db.get_note("u1")
        assert row["state"] == "not_in_anki"
        assert row["recommended_action"] == "review"
        assert len(self.file.pending_review) == 1
