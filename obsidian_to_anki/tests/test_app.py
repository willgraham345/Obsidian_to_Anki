import pytest
from unittest.mock import MagicMock, patch
import os
import argparse
import re

from src.obsidian_to_anki.app import App
from src.obsidian_to_anki.config import Config
from src.obsidian_to_anki.data import Data
from src.obsidian_to_anki.anki_connect import AnkiConnect
from src.obsidian_to_anki import globals

# Shared parse_args mock — returns a namespace with no active flags
_NO_ARGS = MagicMock(update=False, mediaupdate=False, config=False, path=False, recurse=False, regex=False)


class TestApp:

    @pytest.fixture(autouse=True)
    def setup(self):
        globals.CONFIG_DATA = {
            "GUI": False,
            "Regex": False,
            "NOTE_PREFIX": re.escape("## "),
            "NOTE_SUFFIX": re.escape("## "),
            "DECK_LINE": "Deck",
            "TAG_LINE": "Tags",
            "INLINE_PREFIX": re.escape("{{"),
            "INLINE_SUFFIX": re.escape("}}"),
            "Vault": "",
            "FROZEN_LINE": "Frozen"
        }
        globals.MEDIA = {}
        globals.ADDED_MEDIA = []
        globals.FILE_HASHES = {}
        globals.FIELDS_DICT = {}
        globals.EXISTING_IDS = []
        globals.ID_PREFIX = "ID: "

    @patch('src.obsidian_to_anki.config.Config.load_config')
    @patch('src.obsidian_to_anki.config.Config.update_config')
    @patch('src.obsidian_to_anki.data.Data.load_data_file')
    @patch('src.obsidian_to_anki.data.Data.create_data_file')
    @patch('src.obsidian_to_anki.app.App.get_fields')
    @patch('src.obsidian_to_anki.app.App.get_ids')
    @patch('src.obsidian_to_anki.app.App.gen_regexp')
    @patch('argparse.ArgumentParser.parse_args', return_value=_NO_ARGS)
    @patch('src.obsidian_to_anki.app.argparse.ArgumentParser')
    def test_app_init_cli_no_args(self, MockArgumentParser, mock_parse_args, mock_gen_regexp, mock_get_ids, mock_get_fields, mock_create_data_file, mock_load_data_file, mock_update_config, mock_load_config):
        mock_parser = MockArgumentParser.return_value
        mock_parser.parse_args.return_value = _NO_ARGS
        app = App(Config())

        mock_load_config.assert_called_once()
        mock_load_data_file.assert_called_once()
        mock_get_fields.assert_called_once()
        mock_get_ids.assert_called_once()
        mock_gen_regexp.assert_called_once()
        mock_parser.print_help.assert_called_once()

    @patch('src.obsidian_to_anki.config.Config.load_config')
    @patch('src.obsidian_to_anki.data.Data.load_data_file')
    @patch('src.obsidian_to_anki.app.App.get_fields')
    @patch('src.obsidian_to_anki.app.App.get_ids')
    @patch('argparse.ArgumentParser.parse_args', return_value=_NO_ARGS)
    @patch('src.obsidian_to_anki.app.argparse.ArgumentParser')
    def test_setup_cli_parser(self, MockArgumentParser, mock_parse_args, mock_get_ids, mock_get_fields, mock_load_data_file, mock_load_config):
        mock_parser_instance = MockArgumentParser.return_value
        mock_parser_instance.parse_args.return_value = _NO_ARGS
        app = App(Config())
        app.setup_cli_parser()
        MockArgumentParser.assert_called_with(description="Add cards to Anki from a markdown or text file.")
        mock_parser_instance.add_argument.assert_any_call("path", default=False, nargs="?", help="Path to the file or directory you want to scan.")

    @patch('src.obsidian_to_anki.config.Config.load_config')
    @patch('src.obsidian_to_anki.data.Data.load_data_file')
    @patch('src.obsidian_to_anki.app.App.get_fields')
    @patch('src.obsidian_to_anki.app.App.get_ids')
    @patch('argparse.ArgumentParser.parse_args', return_value=_NO_ARGS)
    def test_gen_regexp(self, mock_parse_args, mock_get_ids, mock_get_fields, mock_load_data_file, mock_load_config):
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

        # NOTE_REGEXP format: prefix + title_line + newline + (content) + suffix
        test_note_content = "## My Note\nSome content\n## "
        match = globals.NOTE_REGEXP.search(test_note_content)
        assert match is not None
        assert "Some content" in match.group(1)

    @patch('src.obsidian_to_anki.config.Config.load_config')
    @patch('src.obsidian_to_anki.data.Data.load_data_file')
    @patch('src.obsidian_to_anki.app.App.get_fields')
    @patch('src.obsidian_to_anki.app.App.get_ids')
    @patch('argparse.ArgumentParser.parse_args', return_value=_NO_ARGS)
    @patch('src.obsidian_to_anki.anki_connect.AnkiConnect.request')
    def test_get_add_media(self, mock_anki_request, mock_parse_args, mock_get_ids, mock_get_fields, mock_load_data_file, mock_load_config):
        globals.MEDIA = {"image1.png": "base64data1", "image2.jpg": "base64data2"}
        app = App(Config())
        result = app.get_add_media()

        mock_anki_request.assert_any_call("storeMediaFile", filename="image1.png", data="base64data1")
        mock_anki_request.assert_any_call("storeMediaFile", filename="image2.jpg", data="base64data2")
        assert result == mock_anki_request.return_value

    @patch('src.obsidian_to_anki.config.Config.load_config')
    @patch('src.obsidian_to_anki.data.Data.load_data_file')
    @patch('src.obsidian_to_anki.app.App.get_ids')
    @patch('argparse.ArgumentParser.parse_args', return_value=_NO_ARGS)
    @patch('src.obsidian_to_anki.anki_connect.AnkiConnect.invoke')
    @patch('src.obsidian_to_anki.anki_connect.AnkiConnect.parse')
    @patch('src.obsidian_to_anki.anki_connect.AnkiConnect.request')
    def test_get_fields(self, mock_anki_request, mock_anki_parse, mock_anki_invoke, mock_parse_args, mock_get_ids, mock_load_data_file, mock_load_config):
        # Provide enough side_effect items for init's get_fields() call AND the explicit call
        mock_anki_invoke.side_effect = [
            ["NoteType1", "NoteType2"], ["result1", "result2"],  # init call
            ["NoteType1", "NoteType2"], ["result1", "result2"],  # explicit call
        ]
        mock_anki_parse.side_effect = [
            ["Field1", "Field2"], ["FieldA", "FieldB"],  # init call
            ["Field1", "Field2"], ["FieldA", "FieldB"],  # explicit call
        ]

        app = App(Config())
        app.get_fields()

        mock_anki_invoke.assert_any_call("modelNames")
        mock_anki_request.assert_any_call("modelFieldNames", modelName="NoteType1")
        mock_anki_request.assert_any_call("modelFieldNames", modelName="NoteType2")
        assert globals.FIELDS_DICT == {"NoteType1": ["Field1", "Field2"], "NoteType2": ["FieldA", "FieldB"]}

    @patch('src.obsidian_to_anki.config.Config.load_config')
    @patch('src.obsidian_to_anki.data.Data.load_data_file')
    @patch('src.obsidian_to_anki.app.App.get_fields')
    @patch('argparse.ArgumentParser.parse_args', return_value=_NO_ARGS)
    @patch('src.obsidian_to_anki.anki_connect.AnkiConnect.invoke')
    def test_get_ids(self, mock_anki_invoke, mock_parse_args, mock_get_fields, mock_load_data_file, mock_load_config):
        mock_anki_invoke.return_value = ["id1", "id2"]

        app = App(Config())
        app.get_ids()

        mock_anki_invoke.assert_called_with("findNotes", query="")
        assert globals.EXISTING_IDS == ["id1", "id2"]

    # TODO: Add tests for setup_parser_optionals
    # TODO: Add tests for App.__init__ with different argument combinations (update, mediaupdate, config, path, recurse)
    # TODO: Add tests for App.__init__ error handling for config and data loading
