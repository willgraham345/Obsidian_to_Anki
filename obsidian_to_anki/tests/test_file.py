import pytest
from unittest.mock import patch, MagicMock, mock_open, call
import os
import re
import hashlib

from src.obsidian_to_anki.file import File
from src.obsidian_to_anki.note import Note, InlineNote, RegexNote
from src.obsidian_to_anki.anki_connect import AnkiConnect
from src.obsidian_to_anki import globals
from src.obsidian_to_anki.utils import findignore, spans


class TestFile:

    @pytest.fixture(autouse=True)
    def setup(self):
        globals.CONFIG_DATA = {
            "Vault": "",
            "NOTE_PREFIX": re.escape("## "),
            "NOTE_SUFFIX": re.escape("## "),
            "DECK_LINE": "Deck",
            "TAG_LINE": "Tags",
            "INLINE_PREFIX": re.escape("{{"),
            "INLINE_SUFFIX": re.escape("}}"),
            "FROZEN_LINE": "Frozen",
            "Comment": False,
            "CUSTOM_REGEXPS": {}
        }
        globals.VAULT_PATH_REGEXP = re.compile(r"VaultName/(.*)")
        globals.NOTE_REGEXP = re.compile(r"## (.+?)\n(.*?)\n## ", re.DOTALL)
        globals.INLINE_REGEXP = re.compile(r"\{\{(.*?)\}\}")
        globals.EMPTY_REGEXP = re.compile(r"^## \n(?:<!--)?ID: (\d+)[\s\S]*?\n## ", re.MULTILINE)
        globals.DECK_REGEXP = re.compile(r"^Deck(?:\n|: )(.*)", re.MULTILINE)
        globals.TAG_REGEXP = re.compile(r"^Tags(?:\n|: )(.*)", re.MULTILINE)
        globals.FROZEN_REGEXP = re.compile(r"Frozen - (.*?):\n((?:[^\n][\n]?)+)")
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
        file_instance.file = """Frozen - NoteType1:\nField1: Value1\nField2: Value2"""
        globals.FIELDS_DICT = {"NoteType1": ["Field1", "Field2"], "NoteType2": ["FieldA"]}

        with patch('src.obsidian_to_anki.file.Note') as MockNote:
            mock_note_instance = MockNote.return_value
            mock_note_instance.fields = {"Field1": "Value1", "Field2": "Value2"}
            file_instance.setup_frozen_fields_dict()
            assert file_instance.frozen_fields_dict == {
                "NoteType1": {"Field1": "Value1", "Field2": "Value2"},
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
        assert file_instance.target_deck == globals.NOTE_DICT_TEMPLATE["deckName"]

    def test_setup_global_tags(self):
        file_instance = File("dummy.md")
        file_instance.file = "Tags: tag1 tag2"
        file_instance.setup_global_tags()
        assert file_instance.global_tags == "tag1 tag2"

        file_instance.file = "No Tags Line"
        file_instance.setup_global_tags()
        assert file_instance.global_tags == ""

    @patch('src.obsidian_to_anki.file.File.setup_frozen_fields_dict')
    @patch('src.obsidian_to_anki.file.File.setup_target_deck')
    @patch('src.obsidian_to_anki.file.File.setup_global_tags')
    @patch('src.obsidian_to_anki.file.Note')
    @patch('src.obsidian_to_anki.file.InlineNote')
    def test_scan_file(self, MockInlineNote, MockNote, mock_setup_global_tags, mock_setup_target_deck, mock_setup_frozen_fields_dict):
        file_content = (
            "\n## Note to Add\ncontent\n## \n"
            "{{Inline Note to Add}}\n"
            "## Note to Edit\ncontent\n## \n"
            "## \nID: 67890\n## \n"
        )
        file_instance = File("dummy.md")
        file_instance.file = file_content
        file_instance.url = "mock_url"
        file_instance.frozen_fields_dict = {}
        globals.EXISTING_IDS = [12345]

        # Mock Note and InlineNote parsing
        mock_note_to_add = MagicMock(id=None, note={"tags": []})
        mock_note_to_edit = MagicMock(id=12345, note={"tags": []})
        mock_inline_note_to_add = MagicMock(id=None, note={"tags": []})

        MockNote.return_value.parse.side_effect = [mock_note_to_add, mock_note_to_edit]
        MockInlineNote.return_value.parse.return_value = mock_inline_note_to_add

        file_instance.target_deck = "Default"
        file_instance.global_tags = ""
        file_instance.scan_file()

        assert len(file_instance.notes_to_add) == 1
        assert len(file_instance.inline_notes_to_add) == 1
        assert len(file_instance.notes_to_edit) == 1
        assert len(file_instance.notes_to_delete) == 1 # From <!--id:67890-->
        assert file_instance.notes_to_add[0] == mock_note_to_add.note
        assert file_instance.inline_notes_to_add[0] == mock_inline_note_to_add.note
        assert file_instance.notes_to_edit[0] == mock_note_to_edit
        assert file_instance.notes_to_delete[0] == 67890

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
    def test_scan_file_calls_search_for_custom_regexps(self, mock_search, mock_add_spans, *_):
        globals.CONFIG_DATA["CUSTOM_REGEXPS"] = {"MyNoteType": "MY_REGEX"}
        file_content = "## \nID: 12345\n## "
        file_instance = File("dummy.md")
        file_instance.file = file_content
        globals.EXISTING_IDS = [12345]

        file_instance.scan_file()

        mock_add_spans.assert_called_once()
        mock_search.assert_called_once_with("MyNoteType", "MY_REGEX")
        assert file_instance.notes_to_delete == [12345]

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
        file_instance.notes_to_add = [{"note": "add1"}]
        file_instance.inline_notes_to_add = [{"note": "inline_add1"}]
        result = file_instance.get_add_notes()
        mock_anki_request.assert_has_calls([
            call("addNote", note={"note": "add1"}),
            call("addNote", note={"note": "inline_add1"}),
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
