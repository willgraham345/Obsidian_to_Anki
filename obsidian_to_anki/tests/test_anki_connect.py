import pytest
from unittest.mock import patch, MagicMock
import os
import urllib.request

from src.obsidian_to_anki.anki_connect import AnkiConnect

@pytest.fixture
def anki_connect_instance():
    """Provides a default instance of AnkiConnect for testing."""
    return AnkiConnect()

class TestAnkiConnect:

    def test_request(self, anki_connect_instance):
        action = "testAction"
        params = {"param1": "value1", "param2": 123}
        expected_request = {
            'action': action,
            'params': params,
            'version': 6
        }
        assert anki_connect_instance.request(action, **params) == expected_request

    def test_parse_valid_response(self, anki_connect_instance):
        response = {"result": "success", "error": None}
        assert anki_connect_instance.parse(response) == "success"

    def test_parse_error_in_response(self, anki_connect_instance):
        response = {"result": None, "error": "An error occurred"}
        with pytest.raises(Exception, match="An error occurred"):
            anki_connect_instance.parse(response)

    def test_parse_missing_error_field(self, anki_connect_instance):
        response = {"result": "success"}
        with pytest.raises(Exception, match="response is missing required error field"):
            anki_connect_instance.parse(response)

    def test_parse_missing_result_field(self, anki_connect_instance):
        response = {"error": None}
        with pytest.raises(Exception, match="response is missing required result field"):
            anki_connect_instance.parse(response)

    def test_parse_unexpected_fields(self, anki_connect_instance):
        response = {"result": "success", "error": None, "extra": "field"}
        with pytest.raises(Exception, match="response has an unexpected number of fields"):
            anki_connect_instance.parse(response)

    @patch('src.obsidian_to_anki.anki_connect.urllib.request.urlopen')
    @patch('src.obsidian_to_anki.anki_connect.json.load')
    def test_invoke(self, mock_json_load, mock_urlopen, anki_connect_instance):
        mock_urlopen.return_value = MagicMock()
        mock_json_load.return_value = {"result": "invoke_success", "error": None}

        action = "testAction"
        params = {"key": "value"}
        result = anki_connect_instance.invoke(action, **params)

        mock_urlopen.assert_called_once()
        assert result == "invoke_success"

    def test_wsl_host_detection(self):
        with patch.dict(os.environ, {'WSL_DISTRO_NAME': 'Ubuntu'}, clear=True):
            anki_connect = AnkiConnect()
            assert anki_connect.host == "127.0.0.1"

    def test_default_host_non_wsl(self):
        with patch.dict(os.environ, clear=True):
            anki_connect = AnkiConnect()
            assert anki_connect.host == "localhost"

    def test_custom_port(self):
        custom_port = 12345
        anki_connect = AnkiConnect(port=custom_port)
        assert anki_connect.port == custom_port

    @patch('src.obsidian_to_anki.anki_connect.json.load')
    @patch('src.obsidian_to_anki.anki_connect.urllib.request.urlopen')
    def test_invoke_url_construction(self, mock_urlopen, mock_json_load):
        mock_urlopen.return_value = MagicMock()
        mock_json_load.return_value = {"result": "ok", "error": None}

        # Default port, non-WSL
        with patch.dict(os.environ, {}, clear=True):
            anki_connect_default = AnkiConnect()
            anki_connect_default.invoke("test")
            req = mock_urlopen.call_args[0][0]
            assert "localhost" in req.full_url
            assert "8765" in req.full_url

        # Custom port
        anki_connect_custom = AnkiConnect(port=9999)
        anki_connect_custom.invoke("test")
        req = mock_urlopen.call_args[0][0]
        assert "9999" in req.full_url

        # WSL environment
        with patch.dict(os.environ, {'WSL_DISTRO_NAME': 'Debian'}, clear=True):
            anki_connect_wsl = AnkiConnect()
            anki_connect_wsl.invoke("test")
            req = mock_urlopen.call_args[0][0]
            assert "127.0.0.1" in req.full_url
