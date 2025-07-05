import pytest
from unittest.mock import patch, MagicMock, call
import re

from src.obsidian_to_anki.note import Note, InlineNote, RegexNote
from src.obsidian_to_anki import globals
from src.obsidian_to_anki.format_converter import FormatConverter
from src.obsidian_to_anki.utils import note_has_clozes

class TestNote:

    @pytest.fixture(autouse=True)
    def setup(self):
        # Reset globals before each test to ensure isolation
        globals.ID_PREFIX = "ID: "
        globals.TAG_PREFIX = "Tags: "
        globals.TAG_SEP = " "
        globals.FIELDS_DICT = {"Basic": ["Front", "Back"], "Cloze": ["Text"]}
        globals.CONFIG_DATA = {"CurlyCloze": False, "Add file link": False, "Vault": ""}
        globals.NOTE_DICT_TEMPLATE = {
            "deckName": "Default",
            "modelName": "",
            "fields": {},
            "options": {"allowDuplicate": False, "duplicateScope": "deck"},
            "tags": ["Obsidian_to_Anki"],
            "audio": []
        }
        # Recompile ID_REGEXP for Note class after globals.ID_PREFIX might change
        Note.ID_REGEXP = re.compile(r"(?:<!--)?" + globals.ID_PREFIX + r"(\d+)")

    def test_note_init_with_id_and_tags(self):
        note_text = "Basic\nFront: content\nBack: content\nTags: tag1 tag2\nID: 123"
        note = Note(note_text)
        assert note.identifier == 123
        assert note.tags == ["tag1", "tag2"]
        assert note.note_type == "Basic"
        assert note.lines == ["Basic", "Front: content", "Back: content"]

    def test_note_init_no_id_no_tags(self):
        note_text = "Basic\nFront: content\nBack: content"
        note = Note(note_text)
        assert note.identifier is None
        assert note.tags == []
        assert note.note_type == "Basic"
        assert note.lines == ["Basic", "Front: content", "Back: content"]

    def test_field_from_line(self):
        note = Note("Basic\nFront: content") # Dummy init
        note.field_names = ["Front", "Back"]
        note.current_field = "Front"

        line, field = note.field_from_line("Front: some text")
        assert line == " some text"
        assert field == "Front"

        line, field = note.field_from_line("just some text")
        assert line == "just some text"
        assert field == "Front" # Should remain current_field

    @patch('src.obsidian_to_anki.note.FormatConverter.format', side_effect=lambda text, cloze: text.strip())
    def test_fields_property_basic(self, mock_format):
        note_text = "Basic\nFront: Front Content\nBack: Back Content"
        note = Note(note_text)
        fields = note.fields
        assert fields == {"Front": "Front Content", "Back": "Back Content"}
        mock_format.assert_has_calls([
            call("Front Content", cloze=False),
            call("Back Content", cloze=False)
        ], any_order=True)

    @patch('src.obsidian_to_anki.note.FormatConverter.format', side_effect=lambda text, cloze: f"formatted({text}, {cloze})")
    def test_fields_property_with_cloze(self, mock_format):
        globals.CONFIG_DATA["CurlyCloze"] = True
        note_text = "Cloze\nText: {c1::cloze text}"
        note = Note(note_text)
        fields = note.fields
        assert fields == {"Text": "formatted({c1::cloze text}, True)"}
        mock_format.assert_called_once_with("{c1::cloze text}", cloze=True)

    @patch('src.obsidian_to_anki.note.FormatConverter.format')
    @patch('src.obsidian_to_anki.note.FormatConverter.format_note_with_url')
    @patch('src.obsidian_to_anki.note.FormatConverter.format_note_with_frozen_fields')
    def test_parse_basic(self, mock_format_frozen, mock_format_url, mock_format_field):
        mock_format_field.side_effect = lambda text, cloze: text.strip()
        note_text = "Basic\nFront: F\nBack: B"
        note = Note(note_text)
        parsed_note_and_id = note.parse("MyDeck")

        assert parsed_note_and_id.id is None
        assert parsed_note_and_id.note["modelName"] == "Basic"
        assert parsed_note_and_id.note["deckName"] == "MyDeck"
        assert parsed_note_and_id.note["fields"] == {"Front": "F", "Back": "B"}
        assert "Obsidian_to_Anki" in parsed_note_and_id.note["tags"]
        mock_format_url.assert_not_called()
        mock_format_frozen.assert_not_called()

    @patch('src.obsidian_to_anki.note.FormatConverter.format', side_effect=lambda text, cloze: text.strip())
    @patch('src.obsidian_to_anki.note.FormatConverter.format_note_with_url')
    def test_parse_with_url(self, mock_format_url, mock_format_field):
        globals.CONFIG_DATA["Add file link"] = True
        globals.CONFIG_DATA["Vault"] = "MyVault"
        note_text = "Basic\nFront: F"
        note = Note(note_text)
        note.parse("MyDeck", url="mock_url")
        mock_format_url.assert_called_once()

    @patch('src.obsidian_to_anki.note.FormatConverter.format', side_effect=lambda text, cloze: text.strip())
    @patch('src.obsidian_to_anki.note.FormatConverter.format_note_with_frozen_fields')
    def test_parse_with_frozen_fields(self, mock_format_frozen, mock_format_field):
        note_text = "Basic\nFront: F"
        note = Note(note_text)
        frozen_fields = {"Basic": {"Front": "FrozenF"}}
        note.parse("MyDeck", frozen_fields_dict=frozen_fields)
        mock_format_frozen.assert_called_once()


class TestInlineNote:

    @pytest.fixture(autouse=True)
    def setup(self):
        globals.ID_PREFIX = "ID: "
        globals.TAG_PREFIX = "Tags: "
        globals.TAG_SEP = " "
        globals.FIELDS_DICT = {"Basic": ["Front", "Back"], "Cloze": ["Text"]}
        globals.CONFIG_DATA = {"CurlyCloze": False, "Add file link": False, "Vault": ""}
        globals.NOTE_DICT_TEMPLATE = {
            "deckName": "Default",
            "modelName": "",
            "fields": {},
            "options": {"allowDuplicate": False, "duplicateScope": "deck"},
            "tags": ["Obsidian_to_Anki"],
            "audio": []
        }
        # Recompile regexps for InlineNote class after globals might change
        InlineNote.ID_REGEXP = re.compile(r"(?:<!--)?" + globals.ID_PREFIX + r"(\d+)")
        InlineNote.TAG_REGEXP = re.compile(globals.TAG_PREFIX + r"(.*)")

    def test_inlinenote_init_with_id_and_tags(self):
        note_text = "[Basic] Front: content Tags: tag1 ID: 123"
        note = InlineNote(note_text)
        assert note.identifier == 123
        assert note.tags == ["tag1"]
        assert note.note_type == "Basic"
        assert note.text == "Front: content "

    def test_inlinenote_init_no_id_no_tags(self):
        note_text = "[Basic] Front: content"
        note = InlineNote(note_text)
        assert note.identifier is None
        assert note.tags == []
        assert note.note_type == "Basic"
        assert note.text == "Front: content"

    @patch('src.obsidian_to_anki.note.FormatConverter.format', side_effect=lambda text, cloze: text.strip())
    def test_inlinenote_fields_property(self, mock_format):
        note_text = "[Basic] Front: Front Content Back: Back Content"
        note = InlineNote(note_text)
        fields = note.fields
        assert fields == {"Front": "Front Content", "Back": "Back Content"}
        mock_format.assert_has_calls([
            call("Front Content", cloze=False),
            call("Back Content", cloze=False)
        ], any_order=True)

    @patch('src.obsidian_to_anki.note.FormatConverter.format')
    @patch('src.obsidian_to_anki.note.FormatConverter.format_note_with_url')
    @patch('src.obsidian_to_anki.note.FormatConverter.format_note_with_frozen_fields')
    def test_inlinenote_parse(self, mock_format_frozen, mock_format_url, mock_format_field):
        mock_format_field.side_effect = lambda text, cloze: text.strip()
        note_text = "[Basic] Front: F"
        note = InlineNote(note_text)
        parsed_note_and_id = note.parse("MyDeck")

        assert parsed_note_and_id.id is None
        assert parsed_note_and_id.note["modelName"] == "Basic"
        assert parsed_note_and_id.note["deckName"] == "MyDeck"
        assert parsed_note_and_id.note["fields"] == {"Front": "F", "Back": ""}
        assert "Obsidian_to_Anki" in parsed_note_and_id.note["tags"]
        mock_format_url.assert_not_called()
        mock_format_frozen.assert_not_called()


class TestRegexNote:

    @pytest.fixture(autouse=True)
    def setup(self):
        globals.ID_PREFIX = "ID: "
        globals.TAG_PREFIX = "Tags: "
        globals.TAG_SEP = " "
        globals.FIELDS_DICT = {"Basic": ["Field1", "Field2"], "Cloze": ["Text"]}
        globals.CONFIG_DATA = {"CurlyCloze": False, "Add file link": False, "Vault": ""}
        globals.NOTE_DICT_TEMPLATE = {
            "deckName": "Default",
            "modelName": "",
            "fields": {},
            "options": {"allowDuplicate": False, "duplicateScope": "deck"},
            "tags": ["Obsidian_to_Anki"],
            "audio": []
        }
        # Recompile regexps for RegexNote class after globals might change
        RegexNote.ID_REGEXP_STR = r"\n?(?:<!--)?(?:" + globals.ID_PREFIX + r"(\d+).*)"
        RegexNote.TAG_REGEXP_STR = r"(" + globals.TAG_PREFIX + r".*)"

    def test_regexnote_init_with_id_and_tags(self):
        mock_match = MagicMock()
        mock_match.groups.return_value = ("Group1", "Group2", "Tags: tag1 tag2", "123")
        note = RegexNote(mock_match, "Basic", tags=True, id=True)
        assert note.identifier == 123
        assert note.tags == ["tag1", "tag2"]
        assert note.note_type == "Basic"
        assert note.groups == ["Group1", "Group2"]

    def test_regexnote_init_no_id_no_tags(self):
        mock_match = MagicMock()
        mock_match.groups.return_value = ("Group1", "Group2")
        note = RegexNote(mock_match, "Basic", tags=False, id=False)
        assert note.identifier is None
        assert note.tags == []
        assert note.note_type == "Basic"
        assert note.groups == ["Group1", "Group2"]

    @patch('src.obsidian_to_anki.note.FormatConverter.format', side_effect=lambda text, cloze: text.strip())
    def test_regexnote_fields_property(self, mock_format):
        mock_match = MagicMock()
        mock_match.groups.return_value = ("Content1", "Content2")
        note = RegexNote(mock_match, "Basic")
        fields = note.fields
        assert fields == {"Field1": "Content1", "Field2": "Content2"}
        mock_format.assert_has_calls([
            call("Content1", cloze=False),
            call("Content2", cloze=False)
        ], any_order=True)

    @patch('src.obsidian_to_anki.note.FormatConverter.format')
    @patch('src.obsidian_to_anki.note.FormatConverter.format_note_with_url')
    @patch('src.obsidian_to_anki.note.FormatConverter.format_note_with_frozen_fields')
    def test_regexnote_parse(self, mock_format_frozen, mock_format_url, mock_format_field):
        mock_format_field.side_effect = lambda text, cloze: text.strip()
        mock_match = MagicMock()
        mock_match.groups.return_value = ("Content1",)
        note = RegexNote(mock_match, "Basic")
        parsed_note_and_id = note.parse("MyDeck")

        assert parsed_note_and_id.id is None
        assert parsed_note_and_id.note["modelName"] == "Basic"
        assert parsed_note_and_id.note["deckName"] == "MyDeck"
        assert parsed_note_and_id.note["fields"] == {"Field1": "Content1", "Field2": ""}
        assert "Obsidian_to_Anki" in parsed_note_and_id.note["tags"]
        mock_format_url.assert_not_called()
        mock_format_frozen.assert_not_called()

    @patch('src.obsidian_to_anki.note.FormatConverter.format', side_effect=lambda text, cloze: text.strip())
    def test_regexnote_parse_cloze_error(self, mock_format_field):
        globals.CONFIG_DATA["CurlyCloze"] = True
        mock_match = MagicMock()
        mock_match.groups.return_value = ("No cloze here",)
        note = RegexNote(mock_match, "Cloze")
        result = note.parse("MyDeck")
        assert result == 1 # Error code
