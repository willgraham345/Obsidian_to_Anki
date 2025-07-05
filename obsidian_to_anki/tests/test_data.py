import pytest
from unittest.mock import patch, mock_open
import os
import json

from src.obsidian_to_anki.data import Data
from src.obsidian_to_anki import globals

class TestData:

    @pytest.fixture(autouse=True)
    def setup(self):
        # Reset globals before each test to ensure isolation
        globals.ADDED_MEDIA = []
        globals.FILE_HASHES = {}

    def test_init(self):
        data_instance = Data()
        expected_path_suffix = os.path.join("obsidian_to_anki", "obsidian_to_anki_data.json")
        assert data_instance.DATA_PATH.endswith(expected_path_suffix)
        assert os.path.isabs(data_instance.DATA_PATH)

    @patch('builtins.open', new_callable=mock_open)
    @patch('json.dump')
    def test_create_data_file(self, mock_json_dump, mock_file_open):
        data_instance = Data()
        data_instance.create_data_file()

        mock_file_open.assert_called_once_with(data_instance.DATA_PATH, "w")
        mock_json_dump.assert_called_once_with(dict(), mock_file_open())

    @patch('builtins.open', new_callable=mock_open)
    @patch('json.dump')
    def test_update_data_file(self, mock_json_dump, mock_file_open):
        data_instance = Data()
        test_data = {"key": "value"}
        data_instance.update_data_file(test_data)

        mock_file_open.assert_called_once_with(data_instance.DATA_PATH, "w")
        mock_json_dump.assert_called_once_with(test_data, mock_file_open())

    @patch('builtins.open', new_callable=mock_open)
    @patch('json.load')
    def test_load_data_file(self, mock_json_load, mock_file_open):
        mock_json_load.return_value = {
            "Added Media": ["media1", "media2"],
            "File Hashes": {"file1": "hash1"}
        }
        data_instance = Data()
        data_instance.load_data_file()

        mock_file_open.assert_called_once_with(data_instance.DATA_PATH, "r")
        mock_json_load.assert_called_once_with(mock_file_open())
        assert globals.ADDED_MEDIA == ["media1", "media2"]
        assert globals.FILE_HASHES == {"file1": "hash1"}

    @patch('builtins.open', new_callable=mock_open)
    @patch('json.load')
    def test_load_data_file_missing_keys(self, mock_json_load, mock_file_open):
        mock_json_load.return_value = {}
        data_instance = Data()
        data_instance.load_data_file()

        assert globals.ADDED_MEDIA == []
        assert globals.FILE_HASHES == {}
