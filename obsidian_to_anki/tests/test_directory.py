import pytest
from unittest.mock import patch, MagicMock, call
import os
import re

from src.obsidian_to_anki.directory import Directory
from src.obsidian_to_anki.file import File, RegexFile
from src.obsidian_to_anki.anki_connect import AnkiConnect
from src.obsidian_to_anki.app import App
from src.obsidian_to_anki import globals

class TestDirectory:

    @pytest.fixture(autouse=True)
    def setup(self):
        # Reset globals before each test to ensure isolation
        globals.FILE_HASHES = {}
        # Mock App.SUPPORTED_EXTS as it's a class attribute used in Directory.__init__
        with patch.object(App, 'SUPPORTED_EXTS', [".md", ".txt"]):
            yield

    @patch('src.obsidian_to_anki.directory.os.getcwd', return_value="/mock/parent")
    @patch('src.obsidian_to_anki.directory.os.chdir')
    @patch('src.obsidian_to_anki.directory.os.path.isdir', return_value=True)
    @patch('src.obsidian_to_anki.directory.os.path.splitext', side_effect=lambda x: os.path.splitext(x))
    @patch('src.obsidian_to_anki.directory.os.scandir')
    @patch('src.obsidian_to_anki.directory.File')
    @patch('src.obsidian_to_anki.directory.RegexFile')
    def test_init_directory_scan(self, MockRegexFile, MockFile, mock_scandir, mock_splitext, mock_isdir, mock_chdir, mock_getcwd):
        # Mock scandir entries
        mock_entry1 = MagicMock(is_file=lambda: True, path="/mock/dir/file1.md")
        mock_entry2 = MagicMock(is_file=lambda: True, path="/mock/dir/file2.txt")
        mock_entry3 = MagicMock(is_file=lambda: False, path="/mock/dir/subdir")
        mock_entry4 = MagicMock(is_file=lambda: True, path="/mock/dir/image.png") # Unsupported extension
        mock_scandir.return_value.__enter__.return_value = [mock_entry1, mock_entry2, mock_entry3, mock_entry4]

        # Mock File instances
        mock_file1 = MagicMock(filename="file1.md", hash="hash1")
        mock_file2 = MagicMock(filename="file2.txt", hash="hash2")
        MockFile.side_effect = [mock_file1, mock_file2]

        directory_path = "/mock/dir"
        directory = Directory(directory_path)

        mock_getcwd.assert_called_once()
        mock_chdir.assert_has_calls([call(directory_path), call("/mock/parent")])
        mock_scandir.assert_called_once()
        assert len(directory.files) == 2
        assert directory.files[0] == mock_file1
        assert directory.files[1] == mock_file2
        mock_file1.scan_file.assert_called_once()
        mock_file2.scan_file.assert_called_once()
        MockFile.assert_has_calls([call("/mock/dir/file1.md"), call("/mock/dir/file2.txt")])
        MockRegexFile.assert_not_called()

    @patch('src.obsidian_to_anki.directory.os.getcwd', return_value="/mock/parent")
    @patch('src.obsidian_to_anki.directory.os.chdir')
    @patch('src.obsidian_to_anki.directory.os.path.isdir', return_value=False)
    @patch('src.obsidian_to_anki.directory.File')
    def test_init_onefile(self, MockFile, mock_isdir, mock_chdir, mock_getcwd):
        mock_file = MagicMock(filename="single.md", hash="hash_single")
        MockFile.return_value = mock_file

        file_path = "/mock/dir/single.md"
        directory = Directory("/mock/dir", onefile=file_path)

        mock_getcwd.assert_called_once()
        mock_chdir.assert_has_calls([call("/mock/dir"), call("/mock/parent")])
        assert len(directory.files) == 1
        assert directory.files[0] == mock_file
        mock_file.scan_file.assert_called_once()
        MockFile.assert_called_once_with(file_path)

    @patch('src.obsidian_to_anki.directory.os.getcwd', return_value="/mock/parent")
    @patch('src.obsidian_to_anki.directory.os.chdir')
    @patch('src.obsidian_to_anki.directory.os.path.isdir', return_value=True)
    @patch('src.obsidian_to_anki.directory.os.scandir')
    @patch('src.obsidian_to_anki.directory.File')
    def test_init_file_hashes_skip(self, MockFile, mock_scandir, mock_isdir, mock_chdir, mock_getcwd):
        mock_entry = MagicMock(is_file=lambda: True, path="/mock/dir/existing.md")
        mock_scandir.return_value.__enter__.return_value = [mock_entry]

        mock_file = MagicMock(filename="existing.md", hash="known_hash")
        MockFile.return_value = mock_file

        globals.FILE_HASHES = {"existing.md": "known_hash"}

        directory = Directory("/mock/dir")

        assert len(directory.files) == 0 # Should be skipped
        mock_file.scan_file.assert_not_called()

    @patch('src.obsidian_to_anki.directory.AnkiConnect.request')
    def test_requests_1(self, mock_anki_request):
        mock_file1 = MagicMock()
        mock_file1.get_add_notes.return_value = "add_notes_req1"
        mock_file1.get_note_info.return_value = "note_info_req1"
        mock_file1.get_update_fields.return_value = "update_fields_req1"
        mock_file1.get_delete_notes.return_value = "delete_notes_req1"

        mock_file2 = MagicMock()
        mock_file2.get_add_notes.return_value = "add_notes_req2"
        mock_file2.get_note_info.return_value = "note_info_req2"
        mock_file2.get_update_fields.return_value = "update_fields_req2"
        mock_file2.get_delete_notes.return_value = "delete_notes_req2"

        directory = Directory("/mock/dir")
        directory.files = [mock_file1, mock_file2]

        result = directory.requests_1()

        mock_anki_request.assert_has_calls([
            call("multi", actions=["add_notes_req1", "add_notes_req2"]),
            call("multi", actions=["note_info_req1", "note_info_req2"]),
            call("multi", actions=["update_fields_req1", "update_fields_req2"]),
            call("multi", actions=["delete_notes_req1", "delete_notes_req2"]),
            call("multi", actions=[mock_anki_request.return_value, mock_anki_request.return_value, mock_anki_request.return_value, mock_anki_request.return_value])
        ], any_order=True)
        assert result == mock_anki_request.return_value

    @patch('src.obsidian_to_anki.directory.os.chdir')
    @patch('src.obsidian_to_anki.directory.AnkiConnect.parse')
    def test_parse_requests_1(self, mock_anki_parse, mock_chdir):
        mock_file1 = MagicMock()
        mock_file2 = MagicMock()
        directory = Directory("/mock/dir")
        directory.files = [mock_file1, mock_file2]

        # Mock responses from AnkiConnect.parse
        mock_anki_parse.side_effect = [
            ["note_ids_response1", "note_ids_response2"], # For notes_ids
            ["card_ids_response1", "card_ids_response2"], # For cards_ids
            "parsed_note_id1", # For file1.note_ids
            "parsed_note_id2", # For file2.note_ids
        ]

        requests_1_response = [
            "raw_notes_ids_response",
            "raw_cards_ids_response",
            "raw_update_fields_response",
            "raw_delete_notes_response"
        ]
        tags = ["tag1", "tag2"]

        directory.parse_requests_1(requests_1_response, tags)

        mock_anki_parse.assert_has_calls([
            call("raw_notes_ids_response"),
            call("raw_cards_ids_response"),
            call("note_ids_response1"),
            call("note_ids_response2"),
        ])

        assert mock_file1.note_ids == ["parsed_note_id1"]
        assert mock_file2.note_ids == ["parsed_note_id2"]
        assert mock_file1.card_ids == "card_ids_response1"
        assert mock_file2.card_ids == "card_ids_response2"
        assert mock_file1.tags == tags
        assert mock_file2.tags == tags

        mock_file1.get_cards.assert_called_once()
        mock_file1.write_ids.assert_called_once()
        mock_file1.remove_empties.assert_called_once()
        mock_file1.write_file.assert_called_once()

        mock_file2.get_cards.assert_called_once()
        mock_file2.write_ids.assert_called_once()
        mock_file2.remove_empties.assert_called_once()
        mock_file2.write_file.assert_called_once()

        mock_chdir.assert_has_calls([call("/mock/dir"), call("/mock/parent")])

    @patch('src.obsidian_to_anki.directory.AnkiConnect.request')
    def test_requests_2(self, mock_anki_request):
        mock_file1 = MagicMock()
        mock_file1.get_change_decks.return_value = "change_decks_req1"
        mock_file1.get_clear_tags.return_value = "clear_tags_req1"
        mock_file1.get_add_tags.return_value = "add_tags_req1"

        mock_file2 = MagicMock()
        mock_file2.get_change_decks.return_value = "change_decks_req2"
        mock_file2.get_clear_tags.return_value = "clear_tags_req2"
        mock_file2.get_add_tags.return_value = "add_tags_req2"

        directory = Directory("/mock/dir")
        directory.files = [mock_file1, mock_file2]

        result = directory.requests_2()

        mock_anki_request.assert_has_calls([
            call("multi", actions=["change_decks_req1", "change_decks_req2"]),
            call("multi", actions=["clear_tags_req1", "clear_tags_req2"]),
            call("multi", actions=["add_tags_req1", "add_tags_req2"]),
            call("multi", actions=[mock_anki_request.return_value, mock_anki_request.return_value, mock_anki_request.return_value])
        ], any_order=True)
        assert result == mock_anki_request.return_value

    def test_hashes(self):
        mock_file1 = MagicMock(filename="file1.md", hash="hash1")
        mock_file2 = MagicMock(filename="file2.txt", hash="hash2")

        directory = Directory("/mock/dir")
        directory.files = [mock_file1, mock_file2]

        result = directory.hashes()
        assert result == {"file1.md": "hash1", "file2.txt": "hash2"}
