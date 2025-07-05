import pytest
from unittest.mock import MagicMock, patch
import os
import argparse

from src.obsidian_to_anki.app import App
from src.obsidian_to_anki.config import Config
from src.obsidian_to_anki.data import Data
from src.obsidian_to_anki.anki_connect import AnkiConnect
from src.obsidian_to_anki import globals

class TestApp:

    @pytest.fixture(autouse=True)
    def setup(self):
        # Reset globals before each test to ensure isolation
        globals.CONFIG_DATA = {
            "GUI": False,
            "Regex": False,
            "NOTE_PREFIX": "## ",
            "NOTE_SUFFIX": "## ",
            "DECK_LINE": "Deck",
            "TAG_LINE": "Tags",
            "INLINE_PREFIX": "{{",
            "INLINE_SUFFIX": "}}",
            "Vault": "",
            "FROZEN_LINE": "Frozen"
        }
        globals.MEDIA = {}
        globals.ADDED_MEDIA = []
        globals.FILE_HASHES = {}
        globals.FIELDS_DICT = {}
        globals.EXISTING_IDS = []
        globals.ID_PREFIX = "<!--id:"

    @patch('src.obsidian_to_anki.config.Config.load_config')
    @patch('src.obsidian_to_anki.config.Config.update_config')
    @patch('src.obsidian_to_anki.data.Data.load_data_file')
    @patch('src.obsidian_to_anki.data.Data.create_data_file')
    @patch('src.obsidian_to_anki.anki_connect.AnkiConnect.invoke')
    @patch('src.obsidian_to_anki.anki_connect.AnkiConnect.request')
    @patch('src.obsidian_to_anki.app.App.setup_cli_parser')
    @patch('src.obsidian_to_anki.app.App.setup_gui_parser')
    @patch('src.obsidian_to_anki.app.App.gen_regexp')
    @patch('src.obsidian_to_anki.app.App.get_fields')
    @patch('src.obsidian_to_anki.app.App.get_ids')
    @patch('argparse.ArgumentParser.parse_args')
    def test_app_init_cli_no_args(self, mock_parse_args, mock_get_ids, mock_get_fields, mock_gen_regexp, mock_setup_gui_parser, mock_setup_cli_parser, mock_anki_request, mock_anki_invoke, mock_create_data_file, mock_load_data_file, mock_update_config, mock_load_config):
        mock_parse_args.return_value = MagicMock(update=False, mediaupdate=False, config=False, path=False)
        mock_load_config.return_value = None
        mock_load_data_file.return_value = None

        app = App(Config())

        mock_load_config.assert_called_once()
        mock_load_data_file.assert_called_once()
        mock_get_fields.assert_called_once()
        mock_get_ids.assert_called_once()
        mock_setup_cli_parser.assert_called_once()
        mock_setup_gui_parser.assert_not_called()
        mock_gen_regexp.assert_called_once()
        app.parser.print_help.assert_called_once() # Assuming print_help is called when no args

    @patch('src.obsidian_to_anki.app.argparse.ArgumentParser')
    def test_setup_cli_parser(self, MockArgumentParser):
        mock_parser_instance = MockArgumentParser.return_value
        app = App(Config())
        app.setup_cli_parser()
        MockArgumentParser.assert_called_once_with(description="Add cards to Anki from a markdown or text file.")
        mock_parser_instance.add_argument.assert_any_call("path", default=False, nargs="?", help="Path to the file or directory you want to scan.")
        # TODO: Test setup_parser_optionals is called and its arguments are added

    def test_gen_regexp(self):
        app = App(Config())
        app.gen_regexp()

        assert globals.NOTE_REGEXP is not None
        assert globals.DECK_REGEXP is not None
        assert globals.EMPTY_REGEXP is not None
        assert globals.TAG_REGEXP is not None
        assert globals.INLINE_REGEXP is not None
        assert globals.INLINE_EMPTY_REGEXP is not None
        assert globals.VAULT_PATH_REGEXP is not None
        assert globals.FROZEN_REGEXP is not None

        # Test a simple match for one of the regexps
        test_note_content = "## My Note\nSome content\n## "
        match = globals.NOTE_REGEXP.search(test_note_content)
        assert match is not None
        assert match.group(1) == "Some content\n"

    @patch('src.obsidian_to_anki.anki_connect.AnkiConnect.request')
    def test_get_add_media(self, mock_anki_request):
        globals.MEDIA = {"image1.png": "base64data1", "image2.jpg": "base64data2"}
        app = App(Config())
        result = app.get_add_media()

        mock_anki_request.assert_any_call("storeMediaFile", filename="image1.png", data="base64data1")
        mock_anki_request.assert_any_call("storeMediaFile", filename="image2.jpg", data="base64data2")
        mock_anki_request.assert_called_with("multi", actions=[mock_anki_request.return_value, mock_anki_request.return_value])
        assert result == mock_anki_request.return_value

    @patch('src.obsidian_to_anki.anki_connect.AnkiConnect.invoke')
    @patch('src.obsidian_to_anki.anki_connect.AnkiConnect.parse')
    @patch('src.obsidian_to_anki.anki_connect.AnkiConnect.request')
    def test_get_fields(self, mock_anki_request, mock_anki_parse, mock_anki_invoke):
        mock_anki_invoke.side_effect = [["NoteType1", "NoteType2"], ["result1", "result2"]]
        mock_anki_parse.side_effect = [["Field1", "Field2"], ["FieldA", "FieldB"]]

        app = App(Config())
        app.get_fields()

        mock_anki_invoke.assert_any_call("modelNames")
        mock_anki_request.assert_any_call("modelFieldNames", modelName="NoteType1")
        mock_anki_request.assert_any_call("modelFieldNames", modelName="NoteType2")
        mock_anki_invoke.assert_any_call("multi", actions=[mock_anki_request.return_value, mock_anki_request.return_value])
        assert globals.FIELDS_DICT == {"NoteType1": ["Field1", "Field2"], "NoteType2": ["FieldA", "FieldB"]}

    @patch('src.obsidian_to_anki.anki_connect.AnkiConnect.invoke')
    def test_get_ids(self, mock_anki_invoke):
        mock_anki_invoke.return_value = ["id1", "id2"]

        app = App(Config())
        app.get_ids()

        mock_anki_invoke.assert_called_once_with("findNotes", query="")
        assert globals.EXISTING_IDS == ["id1", "id2"]

    # TODO: Add tests for setup_parser_optionals
    # TODO: Add tests for App.__init__ with different argument combinations (update, mediaupdate, config, path, recurse)
    # TODO: Add tests for App.__init__ error handling for config and data loading
    # TODO: Add tests for GUI related methods if GOOEY is ever enabled and testable
