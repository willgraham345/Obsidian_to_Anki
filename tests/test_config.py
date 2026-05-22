import pytest
from unittest.mock import patch, mock_open
import configparser
import os
import re

from src.atomics.config import Config
from src.atomics import globals

class TestConfig:

    @pytest.fixture(autouse=True)
    def setup(self):
        # Reset globals before each test to ensure isolation
        globals.CONFIG_DATA = {}
        globals.NOTE_DICT_TEMPLATE = {"tags": [], "deckName": ""}

    def test_init(self):
        config = Config()
        expected_path_suffix = "atomics_config.ini"
        assert config.CONFIG_PATH.endswith(expected_path_suffix)
        assert os.path.isabs(config.CONFIG_PATH)

    def test_setup_syntax(self):
        config_parser = configparser.ConfigParser()
        test_config = Config()
        test_config.setup_syntax(config_parser)

        assert config_parser["Syntax"]["Begin Note"] == "START"
        assert config_parser["Syntax"]["End Note"] == "END"
        assert config_parser["Syntax"]["Begin Inline Note"] == "STARTI"
        assert config_parser["Syntax"]["End Inline Note"] == "ENDI"
        assert config_parser["Syntax"]["Target Deck Line"] == "TARGET DECK"
        assert config_parser["Syntax"]["File Tags Line"] == "FILE TAGS"
        assert config_parser["Syntax"]["Delete Note Line"] == "DELETE"
        assert config_parser["Syntax"]["Frozen Fields Line"] == "FROZEN"

    def test_setup_defaults(self):
        config_parser = configparser.ConfigParser()
        test_config = Config()
        test_config.setup_defaults(config_parser)

        assert config_parser["Obsidian"]["Vault name"] == ""
        assert config_parser["Obsidian"]["Add file link"] == "False"
        assert config_parser["Defaults"]["Tag"] == "Obsidian_to_Anki"
        assert config_parser["Defaults"]["Deck"] == "Default"
        assert config_parser["Defaults"]["CurlyCloze"] == "False"
        assert config_parser["Defaults"]["Regex"] == "False"
        assert config_parser["Defaults"]["ID Comments"] == "True"
        assert config_parser["Defaults"]["Anki Path"] == ""
        assert config_parser["Defaults"]["Anki Profile"] == ""

    @patch('src.atomics.config.os.path.exists', return_value=True)
    @patch('src.atomics.config.configparser.ConfigParser')
    @patch('src.atomics.config.AnkiConnect.invoke', return_value=["NoteType1", "NoteType2"])
    @patch('builtins.open', new_callable=mock_open)
    def test_update_config_existing_file(self, mock_file_open, mock_anki_invoke, MockConfigParser, mock_exists):
        mock_config_instance = MockConfigParser.return_value
        mock_config_instance.read.return_value = None
        mock_config_instance.setdefault.side_effect = lambda key, value: mock_config_instance.__setitem__(key, value)
        mock_config_instance.__getitem__.side_effect = lambda key: {"Atomics": {}}.get(key, {})

        test_config = Config()
        test_config.update_config()

        mock_exists.assert_called_once_with(test_config.CONFIG_PATH)
        MockConfigParser.assert_called_once()
        mock_config_instance.read.assert_called_once_with(test_config.CONFIG_PATH, encoding='utf-8-sig')
        mock_anki_invoke.assert_called_once_with("modelNames")
        mock_config_instance.setdefault.assert_any_call("Atomics", {})
        mock_file_open.assert_called_once_with(test_config.CONFIG_PATH, "w", encoding='utf_8')
        mock_config_instance.write.assert_called_once_with(mock_file_open())

    @patch('src.atomics.config.os.path.exists', return_value=False)
    @patch('src.atomics.config.configparser.ConfigParser')
    @patch('src.atomics.config.AnkiConnect.invoke', return_value=["NoteType1"])
    @patch('builtins.open', new_callable=mock_open)
    def test_update_config_new_file(self, mock_file_open, mock_anki_invoke, MockConfigParser, mock_exists):
        mock_config_instance = MockConfigParser.return_value
        mock_config_instance.setdefault.side_effect = lambda key, value: mock_config_instance.__setitem__(key, value)
        mock_config_instance.__getitem__.side_effect = lambda key: {"Atomics": {}}.get(key, {})

        test_config = Config()
        test_config.update_config()

        mock_exists.assert_called_once_with(test_config.CONFIG_PATH)
        mock_config_instance.read.assert_not_called()
        mock_anki_invoke.assert_called_once_with("modelNames")
        mock_file_open.assert_called_once_with(test_config.CONFIG_PATH, "w", encoding='utf_8')
        mock_config_instance.write.assert_called_once_with(mock_file_open())

    def test_load_syntax(self):
        config_parser = configparser.ConfigParser()
        config_parser["Syntax"] = {
            "Begin Note": "## ",
            "End Note": "## ",
            "Begin Inline Note": "{{",
            "End Inline Note": "}}",
            "Target Deck Line": "Deck",
            "File Tags Line": "Tags",
            "Delete Note Line": "DELETE",
            "Frozen Fields Line": "Frozen"
        }
        test_config = Config()
        test_config.load_syntax(config_parser)

        assert globals.CONFIG_DATA["NOTE_PREFIX"] == re.escape("## ")
        assert globals.CONFIG_DATA["NOTE_SUFFIX"] == re.escape("## ")
        assert globals.CONFIG_DATA["INLINE_PREFIX"] == re.escape("{{")
        assert globals.CONFIG_DATA["INLINE_SUFFIX"] == re.escape("}}")
        assert globals.CONFIG_DATA["DECK_LINE"] == re.escape("Deck")
        assert globals.CONFIG_DATA["TAG_LINE"] == re.escape("Tags")
        assert globals.CONFIG_DATA["FROZEN_LINE"] == re.escape("Frozen")
        assert globals.CONFIG_DATA["EMPTY_REGEXP"] is not None

    def test_load_defaults(self):
        config_parser = configparser.ConfigParser()
        config_parser["Defaults"] = {
            "Tag": "MyTag",
            "Deck": "MyDeck",
            "CurlyCloze": "True",
            "Regex": "True",
            "ID Comments": "False",
            "Anki Path": "/path/to/anki",
            "Anki Profile": "MyProfile"
        }
        config_parser["Obsidian"] = {
            "Vault path": "/home/user/MyVault",
            "Vault name": "MyVault",
            "Add file link": "True"
        }
        test_config = Config()
        test_config.load_defaults(config_parser)

        assert globals.NOTE_DICT_TEMPLATE["tags"] == ["MyTag"]
        assert globals.NOTE_DICT_TEMPLATE["deckName"] == "MyDeck"
        assert globals.CONFIG_DATA["CurlyCloze"] is True
        assert globals.CONFIG_DATA["Regex"] is True
        assert globals.CONFIG_DATA["Comment"] is False
        assert globals.CONFIG_DATA["Path"] == "/path/to/anki"
        assert globals.CONFIG_DATA["Profile"] == "MyProfile"
        assert globals.CONFIG_DATA["Vault"] == "/home/user/MyVault"
        assert globals.CONFIG_DATA["Vault name"] == "MyVault"
        assert globals.CONFIG_DATA["Add file link"] is True

    @patch('src.atomics.config.configparser.ConfigParser')
    @patch('src.atomics.config.Config.load_syntax')
    @patch('src.atomics.config.Config.load_defaults')
    @patch('src.atomics.config.Config.load_folder_decks')
    def test_load_config(self, mock_load_folder_decks, mock_load_defaults, mock_load_syntax, MockConfigParser):
        mock_config_instance = MockConfigParser.return_value
        mock_config_instance.read.return_value = None
        mock_config_instance.__getitem__.side_effect = lambda key: {"Atomics": {"NoteType1": "regex1"}}.get(key, {})

        test_config = Config()
        test_config.load_config()

        MockConfigParser.assert_called_once()
        mock_config_instance.read.assert_called_once_with(test_config.CONFIG_PATH, encoding='utf-8-sig')
        mock_load_syntax.assert_called_once_with(mock_config_instance)
        mock_load_defaults.assert_called_once_with(mock_config_instance)
        mock_load_folder_decks.assert_called_once_with(mock_config_instance)
        assert globals.CONFIG_DATA["ATOMICS"] == {"NoteType1": "regex1"}

    def test_setup_folder_decks(self):
        config_parser = configparser.ConfigParser()
        test_config = Config()
        test_config.setup_defaults(config_parser)
        assert "Folder Decks" in config_parser
        assert dict(config_parser["Folder Decks"]) == {}

    def test_load_folder_decks_populated(self):
        config_parser = configparser.ConfigParser()
        config_parser.optionxform = str
        config_parser["Folder Decks"] = {
            "Docs/Programming_and_OS/Cpp": "Cpp",
            "Docs/Programming_and_OS/.*": "Programming",
        }
        test_config = Config()
        test_config.load_folder_decks(config_parser)
        result = globals.CONFIG_DATA["FOLDER_DECKS"]
        assert len(result) == 2
        pat0, deck0 = result[0]
        assert deck0 == "Cpp"
        assert pat0.search("Docs/Programming_and_OS/Cpp/templates.md") is not None
        pat1, deck1 = result[1]
        assert deck1 == "Programming"
        assert pat1.search("Docs/Programming_and_OS/Python/foo.md") is not None

    def test_load_folder_decks_empty_section(self):
        config_parser = configparser.ConfigParser()
        config_parser["Folder Decks"] = {}
        test_config = Config()
        test_config.load_folder_decks(config_parser)
        assert globals.CONFIG_DATA["FOLDER_DECKS"] == []

    def test_load_folder_decks_skips_blank_entries(self):
        config_parser = configparser.ConfigParser()
        config_parser.optionxform = str
        config_parser["Folder Decks"] = {
            "Docs/Cpp": "Cpp",
            "Docs/Empty": "",
        }
        test_config = Config()
        test_config.load_folder_decks(config_parser)
        assert len(globals.CONFIG_DATA["FOLDER_DECKS"]) == 1
        _, deck = globals.CONFIG_DATA["FOLDER_DECKS"][0]
        assert deck == "Cpp"

    def test_load_folder_decks_missing_section(self):
        config_parser = configparser.ConfigParser()
        test_config = Config()
        test_config.load_folder_decks(config_parser)
        assert globals.CONFIG_DATA["FOLDER_DECKS"] == []
