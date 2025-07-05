import pytest
from unittest.mock import patch, MagicMock, call
import re
import os
import urllib.parse
import html
import markdown

from src.obsidian_to_anki.format_converter import FormatConverter
from src.obsidian_to_anki import globals

class TestFormatConverter:

    @pytest.fixture(autouse=True)
    def setup(self):
        # Reset globals before each test to ensure isolation
        globals.MEDIA = {}
        globals.ADDED_MEDIA = []
        globals.md_parser = markdown.Markdown()
        FormatConverter.CLOZE_UNSET_NUM = 1 # Reset for cloze tests

    def test_regex_patterns(self):
        # Test OBS_INLINE_MATH_REGEXP
        assert FormatConverter.OBS_INLINE_MATH_REGEXP.search("$a+b$") is not None
        assert FormatConverter.OBS_INLINE_MATH_REGEXP.search("$$a+b$$") is None

        # Test OBS_DISPLAY_MATH_REGEXP
        assert FormatConverter.OBS_DISPLAY_MATH_REGEXP.search("$$a+b$$") is not None
        assert FormatConverter.OBS_DISPLAY_MATH_REGEXP.search("$a+b$") is None

        # Test OBS_CODE_REGEXP
        assert FormatConverter.OBS_CODE_REGEXP.search("`code`") is not None
        assert FormatConverter.OBS_CODE_REGEXP.search("```code```") is None

        # Test OBS_DISPLAY_CODE_REGEXP
        assert FormatConverter.OBS_DISPLAY_CODE_REGEXP.search("```code```") is not None
        assert FormatConverter.OBS_DISPLAY_CODE_REGEXP.search("`code`") is None

        # Test ANKI_MATH_REGEXP
        assert FormatConverter.ANKI_MATH_REGEXP.search("\\(a+b\\)") is not None
        assert FormatConverter.ANKI_MATH_REGEXP.search("\\[a+b\\]") is not None

        # Test IMAGE_REGEXP
        assert FormatConverter.IMAGE_REGEXP.search('<img alt="" src="image.png">') is not None

        # Test SOUND_REGEXP
        assert FormatConverter.SOUND_REGEXP.search('[sound:audio.mp3]') is not None

        # Test CLOZE_REGEXP
        assert FormatConverter.CLOZE_REGEXP.search('{c1::text}') is not None
        assert FormatConverter.CLOZE_REGEXP.search('{text}') is not None

        # Test URL_REGEXP
        assert FormatConverter.URL_REGEXP.search('https://example.com') is not None
        assert FormatConverter.URL_REGEXP.search('http://example.com') is not None

    def test_format_note_with_url(self):
        note = {"fields": {"Front": "Hello", "Back": "World"}}
        url = "obsidian://vault/my_vault/my_note"
        FormatConverter.format_note_with_url(note, url)
        assert note["fields"]["Front"] == 'Hello<br><a href="obsidian://vault/my_vault/my_note" class="obsidian-link">Obsidian</a>'
        assert note["fields"]["Back"] == "World"

    def test_format_note_with_frozen_fields(self):
        note = {"modelName": "Basic", "fields": {"Front": "", "Back": ""}}
        frozen_fields_dict = {"Basic": {"Front": "FrozenFront", "Back": "FrozenBack"}}
        FormatConverter.format_note_with_frozen_fields(note, frozen_fields_dict)
        assert note["fields"]["Front"] == "FrozenFront"
        assert note["fields"]["Back"] == "FrozenBack"

    def test_inline_anki_repl(self):
        match = MagicMock()
        match.group.return_value = "$a+b$"
        result = FormatConverter.inline_anki_repl(match)
        assert result == "\\(a+b\\)"

    def test_display_anki_repl(self):
        match = MagicMock()
        match.group.return_value = "$$a+b$$"
        result = FormatConverter.display_anki_repl(match)
        assert result == "\\[a+b\\]"

    def test_obsidian_to_anki_math(self):
        text = "This is inline $a+b$ and this is display $$c+d$$"
        result = FormatConverter.obsidian_to_anki_math(text)
        assert result == "This is inline \\(a+b\\) and this is display \\[c+d\\]"

    def test_cloze_repl_unset_num(self):
        match = MagicMock()
        match.group.side_effect = [None, "text"]
        result = FormatConverter.cloze_repl(match)
        assert result == "{{c1::text}}"
        assert FormatConverter.CLOZE_UNSET_NUM == 2

    def test_cloze_repl_with_num(self):
        match = MagicMock()
        match.group.side_effect = ["1", "text"]
        result = FormatConverter.cloze_repl(match)
        assert result == "{{c1::text}}"

    def test_curly_to_cloze(self):
        text = "{text1} {c2::text2} {text3}"
        result = FormatConverter.curly_to_cloze(text)
        assert result == "{{c1::text1}} {{c2::text2}} {{c2::text3}}" # CLOZE_UNSET_NUM resets
        assert FormatConverter.CLOZE_UNSET_NUM == 1

    def test_markdown_parse(self):
        text = "# Heading\n\n* List item"
        result = FormatConverter.markdown_parse(text)
        assert "<h1>Heading</h1>" in result
        assert "<li>List item</li>" in result

    def test_is_url(self):
        assert FormatConverter.is_url("https://example.com") is True
        assert FormatConverter.is_url("http://example.com") is True
        assert FormatConverter.is_url("file.png") is False

    @patch('src.obsidian_to_anki.format_converter.file_encode', return_value="base64data")
    @patch('src.obsidian_to_anki.format_converter.os.path.basename', return_value="image.png")
    @patch('src.obsidian_to_anki.format_converter.urllib.parse.unquote', return_value="image.png")
    def test_get_images(self, mock_unquote, mock_basename, mock_file_encode):
        html_text = '<img alt="" src="image.png">\n<img alt="" src="https://example.com/remote.jpg">\n<img alt="" src="existing.gif">\n'
        globals.ADDED_MEDIA = ["existing.gif"]
        FormatConverter.get_images(html_text)
        assert globals.MEDIA == {"image.png": "base64data"}
        mock_file_encode.assert_called_once_with("image.png")

    @patch('src.obsidian_to_anki.format_converter.file_encode', return_value="base64audio")
    @patch('src.obsidian_to_anki.format_converter.os.path.basename', return_value="audio.mp3")
    def test_get_audio(self, mock_basename, mock_file_encode):
        html_text = '[sound:audio.mp3][sound:existing.wav]'
        globals.ADDED_MEDIA = ["existing.wav"]
        FormatConverter.get_audio(html_text)
        assert globals.MEDIA == {"audio.mp3": "base64audio"}
        mock_file_encode.assert_called_once_with("audio.mp3")

    def test_path_to_filename(self):
        match = MagicMock()
        match.group.side_effect = ['<img alt="" src="path/to/image.png">', 'path/to/image.png']
        result = FormatConverter.path_to_filename(match)
        assert result == '<img alt="" src="image.png">'

        match.group.side_effect = ['<img alt="" src="https://example.com/image.png">', 'https://example.com/image.png']
        result = FormatConverter.path_to_filename(match)
        assert result == '<img alt="" src="https://example.com/image.png">'

    def test_fix_image_src(self):
        html_text = '<img alt="" src="path/to/image.png">\n<img alt="" src="https://example.com/remote.jpg">\n'
        with patch('src.obsidian_to_anki.format_converter.FormatConverter.path_to_filename') as mock_path_to_filename:
            mock_path_to_filename.side_effect = [
                '<img alt="" src="image.png">', '<img alt="" src="https://example.com/remote.jpg">'
            ]
            result = FormatConverter.fix_image_src(html_text)
            assert result == '<img alt="" src="image.png">\n<img alt="" src="https://example.com/remote.jpg">\n'

    def test_fix_audio_src(self):
        html_text = '[sound:path/to/audio.mp3][sound:remote.wav]'
        with patch('src.obsidian_to_anki.format_converter.FormatConverter.path_to_filename') as mock_path_to_filename:
            mock_path_to_filename.side_effect = [
                '[sound:audio.mp3]', '[sound:remote.wav]'
            ]
            result = FormatConverter.fix_audio_src(html_text)
            assert result == '[sound:audio.mp3][sound:remote.wav]'

    @patch('src.obsidian_to_anki.format_converter.FormatConverter.obsidian_to_anki_math', side_effect=lambda x: x.replace("$a$", "\\(a\\)"))
    @patch('src.obsidian_to_anki.format_converter.FormatConverter.curly_to_cloze', side_effect=lambda x: x.replace("{cloze}", "{{c1::cloze}}"))
    @patch('src.obsidian_to_anki.format_converter.FormatConverter.markdown_parse', side_effect=lambda x: x.replace("# Heading", "<h1>Heading</h1>"))
    @patch('src.obsidian_to_anki.format_converter.FormatConverter.get_images')
    @patch('src.obsidian_to_anki.format_converter.FormatConverter.get_audio')
    @patch('src.obsidian_to_anki.format_converter.FormatConverter.fix_image_src', side_effect=lambda x: x.replace("local.png", "image.png"))
    @patch('src.obsidian_to_anki.format_converter.FormatConverter.fix_audio_src', side_effect=lambda x: x.replace("local.mp3", "audio.mp3"))
    def test_format(self, mock_fix_audio_src, mock_fix_image_src, mock_get_audio, mock_get_images, mock_markdown_parse, mock_curly_to_cloze, mock_obsidian_to_anki_math):
        text = "# Heading\nThis is $a$ math and {cloze} text. Also an image local.png and audio local.mp3"
        result = FormatConverter.format(text, cloze=True)

        mock_obsidian_to_anki_math.assert_called_once()
        mock_curly_to_cloze.assert_called_once()
        mock_markdown_parse.assert_called_once()
        mock_get_images.assert_called_once()
        mock_get_audio.assert_called_once()
        mock_fix_image_src.assert_called_once()
        mock_fix_audio_src.assert_called_once()

        assert "<h1>Heading</h1>" in result
        assert "\\(a\\)" in result
        assert "{{c1::cloze}}" in result
        assert "image.png" in result
        assert "audio.mp3" in result
        assert result.strip() == "<h1>Heading</h1>\nThis is \\(a\\) math and {{c1::cloze}} text. Also an image image.png and audio audio.mp3"

    def test_format_removes_paragraph_tags(self):
        text = "<p>Only content</p>"
        result = FormatConverter.format(text)
        assert result == "Only content"

        text = "<p>Content with <br> line break</p>"
        result = FormatConverter.format(text)
        assert result == "Content with <br> line break"

        text = "<p>Multiple paragraphs</p><p>Second paragraph</p>"
        result = FormatConverter.format(text)
        assert result == "<p>Multiple paragraphs</p><p>Second paragraph</p>"
