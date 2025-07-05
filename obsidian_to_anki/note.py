"""Manages parsing notes into a dictionary formatted for AnkiConnect."""

import re

from . import globals
from .format_converter import FormatConverter
from .utils import note_has_clozes

class Note:
    """Manages parsing notes into a dictionary formatted for AnkiConnect.

    Input must be the note text.
    Does NOT deal with finding the note in the file.
    """

    ID_REGEXP = re.compile(
        r"(?:<!--)?" + globals.ID_PREFIX + r"(\d+)"
    )

    def __init__(self, note_text):
        """Set up useful variables."""
        self.text = note_text
        self.lines = self.text.splitlines()
        self.current_field_num = 0
        if Note.ID_REGEXP.match(self.lines[-1]):
            self.identifier = int(
                Note.ID_REGEXP.match(self.lines.pop()).group(1)
            )
            # The above removes the identifier line, for convenience of parsing
        else:
            self.identifier = None
        if self.lines[-1].startswith(globals.TAG_PREFIX):
            self.tags = self.lines.pop()[len(globals.TAG_PREFIX):].split(
                globals.TAG_SEP
            )
        else:
            self.tags = list()
        self.note_type = self.lines[0]
        self.field_names = globals.FIELDS_DICT[self.note_type]
        self.current_field = self.field_names[0]

    def field_from_line(self, line):
        """From a given line, determine the next field to add text into.

        Then, return the stripped line, and the field."""
        for field in self.field_names:
            if line.startswith(field + ":"):
                return (line[len(field + ":"):], field)
        return (line, self.current_field)

    @property
    def fields(self):
        """Get the fields of the note into a dictionary."""
        fields = {field: "" for field in self.field_names}
        for line in self.lines[1:]:
            line, self.current_field = self.field_from_line(line)
            fields[self.current_field] += line + "\n"
        fields = {
            key: FormatConverter.format(
                value.strip(),
                cloze=(
                    "Cloze" in self.note_type
                    and globals.CONFIG_DATA["CurlyCloze"]
                )
            )
            for key, value in fields.items()
        }
        return {key: value.strip() for key, value in fields.items()}

    def parse(self, deck, url=None, frozen_fields_dict=None):
        """Get a properly formatted dictionary of the note."""
        template = globals.NOTE_DICT_TEMPLATE.copy()
        template["modelName"] = self.note_type
        template["fields"] = self.fields
        if all([
            globals.CONFIG_DATA["Add file link"],
            globals.CONFIG_DATA["Vault"],
            url
        ]):
            FormatConverter.format_note_with_url(template, url)
        if frozen_fields_dict:
            FormatConverter.format_note_with_frozen_fields(
                template, frozen_fields_dict
            )
        template["tags"] = template["tags"] + self.tags
        template["deckName"] = deck
        return globals.Note_and_id(note=template, id=self.identifier)


class InlineNote:

    ID_REGEXP = re.compile(r"(?:<!--)?" + globals.ID_PREFIX + r"(\d+)")
    TAG_REGEXP = re.compile(globals.TAG_PREFIX + r"(.*)")
    TYPE_REGEXP = re.compile(r"\[(.*?)\]")  # So e.g. [Basic]

    def __init__(self, note_text):
        self.text = note_text.strip()
        self.current_field_num = 0
        ID = InlineNote.ID_REGEXP.search(self.text)
        if ID is not None:
            self.identifier = int(ID.group(1))
            self.text = self.text[:ID.start()]  # Removes identifier
        else:
            self.identifier = None
        TAGS = InlineNote.TAG_REGEXP.search(self.text)
        if TAGS is not None:
            self.tags = TAGS.group(1).split(globals.TAG_SEP)
            self.text = self.text[:TAGS.start()]
        else:
            self.tags = list()
        TYPE = InlineNote.TYPE_REGEXP.search(self.text)
        self.note_type = TYPE.group(1)
        self.text = self.text[TYPE.end():]
        self.field_names = globals.FIELDS_DICT[self.note_type]
        self.current_field = self.field_names[0]

    @property
    def fields(self):
        """Get the fields of the note into a dictionary."""
        fields = {field: "" for field in self.field_names}
        for word in self.text.split(" "):
            for field in self.field_names:
                if word == field + ":":
                    self.current_field = field
                    word = ""
            fields[self.current_field] += word + " "
        fields = {
            key: FormatConverter.format(
                value,
                cloze=(
                    "Cloze" in self.note_type
                    and globals.CONFIG_DATA["CurlyCloze"]
                )
            )
            for key, value in fields.items()
        }
        return {key: value.strip() for key, value in fields.items()}


class RegexNote:
    ID_REGEXP_STR = r"\n?(?:<!--)?(?:" + globals.ID_PREFIX + r"(\d+).*)"
    TAG_REGEXP_STR = r"(" + globals.TAG_PREFIX + r".*)"

    def __init__(self, matchobject, note_type, tags=False, id=False):
        self.match = matchobject
        self.note_type = note_type
        self.groups = list(self.match.groups())
        self.group_num = len(self.groups)
        if id:
            # This means id is last group
            self.identifier = int(self.groups.pop())
        else:
            self.identifier = None
        if tags:
            # Even if id were present, tags is now last group
            self.tags = self.groups.pop()[len(globals.TAG_PREFIX):].split(
                globals.TAG_SEP
            )
        else:
            self.tags = list()
        self.field_names = globals.FIELDS_DICT[self.note_type]

    @property
    def fields(self):
        fields = dict.fromkeys(self.field_names, "")
        for name, match in zip(self.field_names, self.groups):
            if match:
                fields[name] = match
        fields = {
            key: FormatConverter.format(
                value,
                cloze=(
                    "Cloze" in self.note_type
                    and globals.CONFIG_DATA["CurlyCloze"]
                )
            )
            for key, value in fields.items()
        }
        return {key: value.strip() for key, value in fields.items()}

    def parse(self, deck, url=None, frozen_fields_dict=None):
        """Get a properly formatted dictionary of the note."""
        template = globals.NOTE_DICT_TEMPLATE.copy()
        template["modelName"] = self.note_type
        template["fields"] = self.fields
        if all([
            globals.CONFIG_DATA["Add file link"],
            globals.CONFIG_DATA["Vault"],
            url
        ]):
            FormatConverter.format_note_with_url(template, url)
        if frozen_fields_dict:
            FormatConverter.format_note_with_frozen_fields(
                template, frozen_fields_dict
            )
        template["tags"] = template["tags"] + self.tags
        template["deckName"] = deck
        if "Cloze" in self.note_type and globals.CONFIG_DATA[
            "CurlyCloze"
        ] and not note_has_clozes(template):
            return 1  # Like an error code, only for this note type
            # Since we can accidentally recognise { in the wrong places.
        return globals.Note_and_id(note=template, id=self.identifier)