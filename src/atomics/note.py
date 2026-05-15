"""Manages parsing notes into a dictionary formatted for AnkiConnect."""

import re

from . import globals
from .format_converter import FormatConverter
from .utils import note_has_clozes


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

    def parse(self, deck, url=None, frozen_fields_dict=None, file_stem=None):
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
        if file_stem and globals.CONFIG_DATA.get("FILE_STEM_NOTES", {}).get(self.note_type):
            FormatConverter.format_note_with_file_stem(template, file_stem)
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
