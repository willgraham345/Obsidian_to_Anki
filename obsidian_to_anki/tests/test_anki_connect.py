import pytest
from unittest.mock import patch, MagicMock
import json
import urllib.request

from src.obsidian_to_anki.anki_connect import AnkiConnect

class TestAnkiConnect:

    def test_request(self):
        action = "testAction"
        params = {"param1": "value1", "param2": 123}
        expected_request = {
            'action': action,
            'params': params,
            'version': 6
        }
        assert AnkiConnect.request(action, **params) == expected_request

    def test_parse_valid_response(self):
        response = {"result": "success", "error": None}
        assert AnkiConnect.parse(response) == "success"

    def test_parse_error_in_response(self):
        response = {"result": None, "error": "An error occurred"}
        with pytest.raises(Exception, match="An error occurred"):
            AnkiConnect.parse(response)

    def test_parse_missing_error_field(self):
        response = {"result": "success"}
        with pytest.raises(Exception, match="response is missing required error field"):
            AnkiConnect.parse(response)

    def test_parse_missing_result_field(self):
        response = {"error": None}
        with pytest.raises(Exception, match="response is missing required result field"):
            AnkiConnect.parse(response)

    def test_parse_unexpected_fields(self):
        response = {"result": "success", "error": None, "extra": "field"}
        with pytest.raises(Exception, match="response has an unexpected number of fields"):
            AnkiConnect.parse(response)

    @patch('src.obsidian_to_anki.anki_connect.urllib.request.urlopen')
    @patch('src.obsidian_to_anki.anki_connect.json.load')
    @patch('src.obsidian_to_anki.anki_connect.AnkiConnect.parse')
    @patch('src.obsidian_to_anki.anki_connect.AnkiConnect.request')
    def test_invoke(self, mock_request, mock_parse, mock_json_load, mock_urlopen):
        mock_request.return_value = {"action": "test", "params": {}, "version": 6}
        mock_urlopen.return_value = MagicMock() # Mock the file-like object returned by urlopen
        mock_json_load.return_value = {"result": "invoke_success", "error": None}
        mock_parse.return_value = "invoke_success"

        action = "testAction"
        params = {"key": "value"}
        result = AnkiConnect.invoke(action, **params)

        mock_request.assert_called_once_with(action, **params)
        mock_urlopen.assert_called_once() # Check that urlopen was called
        mock_json_load.assert_called_once_with(mock_urlopen.return_value) # Check json.load was called with the urlopen result
        mock_parse.assert_called_once_with({"result": "invoke_success", "error": None})
        assert result == "invoke_success"
