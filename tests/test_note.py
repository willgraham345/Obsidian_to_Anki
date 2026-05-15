import pytest
from unittest.mock import patch, MagicMock, call
import re

from src.obsidian_to_anki.note import RegexNote
from src.obsidian_to_anki import globals
from src.obsidian_to_anki.format_converter import FormatConverter
from src.obsidian_to_anki.utils import note_has_clozes


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
        assert result == 1  # Error code
