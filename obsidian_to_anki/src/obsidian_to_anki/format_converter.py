"""Converting Obsidian formatting to Anki formatting."""

import re
import os
import urllib.parse
import html
# import markdown

from .utils import file_encode
from . import globals

class FormatConverter:
    """Converting Obsidian formatting to Anki formatting."""

    OBS_INLINE_MATH_REGEXP = re.compile(
        r"(?<!$)\\(?=[\S])(?=[^$])[\s\S]*?\S$"
    )
    OBS_DISPLAY_MATH_REGEXP = re.compile(r"$$\s\S]*?$$")

    OBS_CODE_REGEXP = re.compile(
        r"(?<!`)(?=[^`])[\s\S]*?`"
    )
    OBS_DISPLAY_CODE_REGEXP = re.compile(
        r"```[\s\S]*?```"
    )

    ANKI_INLINE_START = r"\\("
    ANKI_INLINE_END = r"\\)"

    ANKI_DISPLAY_START = r"["
    ANKI_DISPLAY_END = r"]"

    ANKI_MATH_REGEXP = re.compile(r"(\[[\s\S]*?\])|(\([\s\S]*?\))")

    MATH_REPLACE = "OBSTOANKIMATH"
    INLINE_CODE_REPLACE = "OBSTOANKICODEINLINE"
    DISPLAY_CODE_REPLACE = "OBSTOANKICODEDISPLAY"

    IMAGE_REGEXP = re.compile(r'<img alt=".*?" src="(.*?)"')
    SOUND_REGEXP = re.compile(r'\[sound:(.+)\]')
    CLOZE_REGEXP = re.compile(
        r'(?:(?<!{){(?:c?(\d+)[:|])?(?!{))((?:[^\n][\n]?)+?)(?:(?<!})}(?!}))'
    )
    URL_REGEXP = re.compile(r'https?://')

    PARA_OPEN = "<p>"
    PARA_CLOSE = "</p>"

    CLOZE_UNSET_NUM = 1

    @staticmethod
    def format_note_with_url(note, url):
        for key in note["fields"]:
            note["fields"][key] += "<br>" + "".join([
                '<a',
                ' href="{}" class="obsidian-link">Obsidian</a>'.format(url)
            ])
            break  # So only does first field

    @staticmethod
    def format_note_with_frozen_fields(note, frozen_fields_dict):
        for field in note["fields"].keys():
            note["fields"][field] += frozen_fields_dict[
                note["modelName"]
            ][field]

    @staticmethod
    def inline_anki_repl(matchobject):
        """Get replacement string for Obsidian-formatted inline math."""
        found_string = matchobject.group(0)
        # Strip Obsidian formatting by removing first and last characters
        found_string = found_string[1:-1]
        # Add Anki formatting
        result = FormatConverter.ANKI_INLINE_START + found_string
        result += FormatConverter.ANKI_INLINE_END
        return result

    @staticmethod
    def display_anki_repl(matchobject):
        """Get replacement string for Obsidian-formatted display math."""
        found_string = matchobject.group(0)
        # Strip Obsidian formatting by removing first two and last two chars
        found_string = found_string[2:-2]
        # Add Anki formatting
        result = FormatConverter.ANKI_DISPLAY_START + found_string
        result += FormatConverter.ANKI_DISPLAY_END
        return result

    @staticmethod
    def obsidian_to_anki_math(note_text):
        """Convert Obsidian-formatted math to Anki-formatted math."""
        return FormatConverter.OBS_INLINE_MATH_REGEXP.sub(
            FormatConverter.inline_anki_repl,
            FormatConverter.OBS_DISPLAY_MATH_REGEXP.sub(
                FormatConverter.display_anki_repl, note_text
            )
        )

    @staticmethod
    def cloze_repl(match):
        id, content = match.group(1), match.group(2)
        if id is None:
            result = "{{{{c{!s}::{}}}}}".format(
                FormatConverter.CLOZE_UNSET_NUM,
                content
            )
            FormatConverter.CLOZE_UNSET_NUM += 1
            return result
        else:
            return "{{{{c{}::{}}}}}".format(id, content)

    @staticmethod
    def curly_to_cloze(text):
        """Change text in curly brackets to Anki-formatted cloze."""
        text = FormatConverter.CLOZE_REGEXP.sub(
            FormatConverter.cloze_repl,
            text
        )
        FormatConverter.CLOZE_UNSET_NUM = 1
        return text

    @staticmethod
    def markdown_parse(text):
        """Apply markdown conversions to text."""
        text = globals.md_parser.reset().convert(text)
        return text

    @staticmethod
    def is_url(text):
        """Check whether text looks like a url."""
        return bool(
            FormatConverter.URL_REGEXP.match(text)
        )

    @staticmethod
    def get_images(html_text):
        """Get all the images that need to be added."""
        for match in FormatConverter.IMAGE_REGEXP.finditer(html_text):
            path = match.group(1)
            if FormatConverter.is_url(path):
                continue  # Skips over images web-hosted.
            path = urllib.parse.unquote(path)
            filename = os.path.basename(path)
            if filename not in globals.ADDED_MEDIA and filename not in globals.MEDIA:
                globals.MEDIA[filename] = file_encode(path)
                # Adds the filename and data to media_names

    @staticmethod
    def get_audio(html_text):
        """Get all the audio that needs to be added."""
        for match in FormatConverter.SOUND_REGEXP.finditer(html_text):
            path = match.group(1)
            filename = os.path.basename(path)
            if filename not in globals.ADDED_MEDIA and filename not in globals.MEDIA:
                globals.MEDIA[filename] = file_encode(path)
                # Adds the filename and data to media_names

    @staticmethod
    def path_to_filename(matchobject):
        """Replace the src in matchobject appropriately."""
        found_string, found_path = matchobject.group(0), matchobject.group(1)
        if FormatConverter.is_url(found_path):
            return found_string  # So urls should not be altered.
        found_string = found_string.replace(
            found_path, os.path.basename(urllib.parse.unquote(found_path))
        )
        return found_string

    @staticmethod
    def fix_image_src(html_text):
        """Fix the src of the images so that it's relative to Anki."""
        return FormatConverter.IMAGE_REGEXP.sub(
            FormatConverter.path_to_filename,
            html_text
        )

    @staticmethod
    def fix_audio_src(html_text):
        """Fix the audio filenames so that it's relative to Anki."""
        return FormatConverter.SOUND_REGEXP.sub(
            FormatConverter.path_to_filename,
            html_text
        )

    @staticmethod
    def format(note_text, cloze=False):
        """Apply all format conversions to note_text."""
        note_text = FormatConverter.obsidian_to_anki_math(note_text)
        # Extract the parts that are anki math
        math_matches = [
            math_match.group(0)
            for math_match in FormatConverter.ANKI_MATH_REGEXP.finditer(
                note_text
            )
        ]
        # Replace them to be later added back, so they don't interfere
        # with markdown parsing
        note_text = FormatConverter.ANKI_MATH_REGEXP.sub(
            FormatConverter.MATH_REPLACE, note_text
        )
        # Now same with code!
        inline_code_matches = [
            code_match.group(0)
            for code_match in FormatConverter.OBS_CODE_REGEXP.finditer(
                note_text
            )
        ]
        note_text = FormatConverter.OBS_CODE_REGEXP.sub(
            FormatConverter.INLINE_CODE_REPLACE, note_text
        )
        display_code_matches = [
            code_match.group(0)
            for code_match in FormatConverter.OBS_DISPLAY_CODE_REGEXP.finditer(
                note_text
            )
        ]
        note_text = FormatConverter.OBS_DISPLAY_CODE_REGEXP.sub(
            FormatConverter.DISPLAY_CODE_REPLACE, note_text
        )
        if cloze:
            note_text = FormatConverter.curly_to_cloze(note_text)
        for code_match in inline_code_matches:
            note_text = note_text.replace(
                FormatConverter.INLINE_CODE_REPLACE,
                code_match,
                1
            )
        for code_match in display_code_matches:
            note_text = note_text.replace(
                FormatConverter.DISPLAY_CODE_REPLACE,
                code_match,
                1
            )
        note_text = FormatConverter.markdown_parse(note_text)
        # Add back the parts that are anki math
        for math_match in math_matches:
            note_text = note_text.replace(
                FormatConverter.MATH_REPLACE,
                html.escape(math_match),
                1
            )
        FormatConverter.get_images(note_text)
        FormatConverter.get_audio(note_text)
        note_text = FormatConverter.fix_image_src(note_text)
        note_text = FormatConverter.fix_audio_src(note_text)
        note_text = note_text.strip()
        # Remove unnecessary paragraph tag
        if note_text.startswith(
            FormatConverter.PARA_OPEN
        ) and note_text.endswith(
            FormatConverter.PARA_CLOSE
        ):
            note_text = note_text[len(FormatConverter.PARA_OPEN):]
            note_text = note_text[:-len(FormatConverter.PARA_CLOSE)]
        return note_text
