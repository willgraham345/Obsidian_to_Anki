import pytest
from unittest.mock import patch, mock_open, MagicMock, call
import os
import re
import base64
import time
import socket
import subprocess

from src.obsidian_to_anki.utils import (
    has_clozes,
    note_has_clozes,
    write_safe,
    string_insert,
    file_encode,
    spans,
    contained_in,
    findignore,
    wait_for_port,
    load_anki
)
from src.obsidian_to_anki import globals

class TestUtils:

    @pytest.fixture(autouse=True)
    def setup(self):
        # Reset globals before each test to ensure isolation
        globals.ANKI_CLOZE_REGEXP = re.compile(r'{{c\\d+::[\\s\\S]+?}}')
        globals.CONFIG_DATA = {
            "Path": "",
            "Profile": ""
        }

    def test_has_clozes(self):
        assert has_clozes("This is {{c1::cloze}} text.") is True
        assert has_clozes("This is normal text.") is False

    def test_note_has_clozes(self):
        note_with_cloze = {"fields": {"Front": "Hello {{c1::World}}", "Back": ""}}
        note_without_cloze = {"fields": {"Front": "Hello World", "Back": ""}}
        note_empty_fields = {"fields": {}}

        assert note_has_clozes(note_with_cloze) is True
        assert note_has_clozes(note_without_cloze) is False
        assert note_has_clozes(note_empty_fields) is False

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.rename')
    @patch('os.remove')
    def test_write_safe_success(self, mock_remove, mock_rename, mock_open_file):
        mock_open_file.side_effect = [
            mock_open(read_data="test content").return_value, # For writing .tmp
            mock_open(read_data="test content").return_value  # For reading back to verify
        ]
        write_safe("test.txt", "test content")

        mock_open_file.assert_has_calls([
            call("test.txt.tmp", "w", encoding='utf_8'),
            call("test.txt", encoding='utf_8')
        ])
        mock_open_file().write.assert_called_once_with("test content")
        mock_rename.assert_has_calls([
            call("test.txt", "test.txt.bak"),
            call("test.txt.tmp", "test.txt")
        ])
        mock_remove.assert_called_once_with("test.txt.bak")

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.rename')
    @patch('os.remove')
    def test_write_safe_failure(self, mock_remove, mock_rename, mock_open_file):
        mock_open_file.side_effect = [
            mock_open(read_data="test content").return_value, # For writing .tmp
            mock_open(read_data="different content").return_value # For reading back to verify
        ]
        write_safe("test.txt", "test content")

        mock_remove.assert_not_called()

    def test_string_insert(self):
        original_string = "abcdefg"
        inserts = [(0, "HI"), (3, "JK"), (7, "LM")]
        result = string_insert(original_string, inserts)
        assert result == "HIabcJKdefgLM"

        original_string = "test"
        inserts = []
        result = string_insert(original_string, inserts)
        assert result == "test"

    @patch('builtins.open', new_callable=mock_open, read_data=b'binary data')
    def test_file_encode(self, mock_open_file):
        result = file_encode("test.png")
        assert result == base64.b64encode(b'binary data').decode('utf-8')
        mock_open_file.assert_called_once_with("test.png", 'rb')

    def test_spans(self):
        pattern = re.compile(r"\d+")
        string = "abc123def456ghi"
        result = spans(pattern, string)
        assert result == [(3, 6), (9, 12)]

    def test_contained_in(self):
        spans_list = [(0, 10), (20, 30)]
        assert contained_in((1, 9), spans_list) is True
        assert contained_in((0, 10), spans_list) is True
        assert contained_in((10, 11), spans_list) is False # Not contained
        assert contained_in((9, 11), spans_list) is True # With leeway
        assert contained_in((19, 21), spans_list) is True # With leeway

    def test_findignore(self):
        pattern = re.compile(r"word")
        string = "This word is ignored. Another word here."
        ignore_spans = [(5, 9)] # Span for the first 'word'
        
        # Mock the finditer method of the compiled regex pattern
        mock_match1 = MagicMock(span=lambda: (5, 9), group=lambda: "word")
        mock_match2 = MagicMock(span=lambda: (25, 29), group=lambda: "word")
        
        with patch.object(re.Pattern, 'finditer', return_value=[mock_match1, mock_match2]):
            results = [match.group() for match in findignore(pattern, string, ignore_spans)]
            assert results == ["word"] # Only the second 'word' should be found

    @patch('src.obsidian_to_anki.utils.time.perf_counter', side_effect=[0, 1, 2, 5.1])
    @patch('src.obsidian_to_anki.utils.socket.create_connection')
    @patch('src.obsidian_to_anki.utils.time.sleep')
    def test_wait_for_port_success(self, mock_sleep, mock_create_connection, mock_perf_counter):
        mock_create_connection.side_effect = [socket.error, MagicMock()]
        wait_for_port(8080, timeout=5)
        mock_create_connection.assert_called_with(('localhost', 8080), timeout=5)
        assert mock_sleep.call_count == 1

    @patch('src.obsidian_to_anki.utils.time.perf_counter', side_effect=[0, 1, 2, 3, 4, 5.1])
    @patch('src.obsidian_to_anki.utils.socket.create_connection', side_effect=socket.error)
    @patch('src.obsidian_to_anki.utils.time.sleep')
    def test_wait_for_port_timeout(self, mock_sleep, mock_create_connection, mock_perf_counter):
        with pytest.raises(TimeoutError):
            wait_for_port(8080, timeout=5)
        assert mock_create_connection.call_count > 1
        assert mock_sleep.call_count > 1

    @patch('src.obsidian_to_anki.utils.Config')
    @patch('src.obsidian_to_anki.utils.subprocess.Popen')
    @patch('src.obsidian_to_anki.utils.wait_for_port')
    def test_load_anki_success(self, mock_wait_for_port, mock_popen, MockConfig):
        mock_config_instance = MockConfig.return_value
        mock_config_instance.load_config.return_value = None
        globals.CONFIG_DATA["Path"] = "/path/to/anki"
        globals.CONFIG_DATA["Profile"] = "MyProfile"

        result = load_anki(mock_config_instance, 8765)

        mock_config_instance.load_config.assert_called_once()
        mock_popen.assert_called_once_with(["/path/to/anki", "-p", "MyProfile"])
        mock_wait_for_port.assert_called_once_with(8765)
        assert result is True

    @patch('src.obsidian_to_anki.utils.Config')
    @patch('src.obsidian_to_anki.utils.subprocess.Popen')
    @patch('src.obsidian_to_anki.utils.wait_for_port', side_effect=TimeoutError)
    def test_load_anki_timeout(self, mock_wait_for_port, mock_popen, MockConfig):
        mock_config_instance = MockConfig.return_value
        mock_config_instance.load_config.return_value = None
        globals.CONFIG_DATA["Path"] = "/path/to/anki"
        globals.CONFIG_DATA["Profile"] = "MyProfile"

        result = load_anki(mock_config_instance, 8765)

        mock_wait_for_port.assert_called_once()
        assert result is False

    @patch('src.obsidian_to_anki.utils.Config')
    @patch('src.obsidian_to_anki.utils.subprocess.Popen')
    @patch('src.obsidian_to_anki.utils.wait_for_port')
    def test_load_anki_no_path_or_profile(self, mock_wait_for_port, mock_popen, MockConfig):
        mock_config_instance = MockConfig.return_value
        mock_config_instance.load_config.return_value = None
        globals.CONFIG_DATA["Path"] = ""
        globals.CONFIG_DATA["Profile"] = ""

        result = load_anki(mock_config_instance, 8765)

        mock_popen.assert_not_called()
        mock_wait_for_port.assert_not_called()
        assert result is False

    @patch('src.obsidian_to_anki.utils.Config')
    @patch('src.obsidian_to_anki.utils.subprocess.Popen')
    @patch('src.obsidian_to_anki.utils.wait_for_port')
    def test_load_anki_config_error(self, mock_wait_for_port, mock_popen, MockConfig):
        mock_config_instance = MockConfig.return_value
        mock_config_instance.load_config.side_effect = Exception("Config error")

        result = load_anki(mock_config_instance, 8765)

        mock_popen.assert_not_called()
        mock_wait_for_port.assert_not_called()
        assert result is False
