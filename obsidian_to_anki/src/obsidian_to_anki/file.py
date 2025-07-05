"""Class for performing script operations at the file-level."""

import os
import re
import hashlib
import logging

from . import globals
from .note import Note, InlineNote, RegexNote
from .utils import string_insert, write_safe, findignore, spans
from .anki_connect import AnkiConnect

class File:
    """Class for performing script operations at the file-level. Requires config to be set."""

    def __init__(self, filepath):
        """Perform initial file reading and attribute setting."""
        self.filename = filepath
        self.path = os.path.abspath(filepath)
        if globals.CONFIG_DATA["Vault"] and globals.VAULT_PATH_REGEXP.search(self.path):
            self.url = "obsidian://vault/{}".format(
                globals.VAULT_PATH_REGEXP.search(self.path).group()
            ).replace("\\", "/")
        else:
            self.url = ""
        with open(self.filename, encoding='utf_8') as f:
            self.file = f.read()
            self.original_file = self.file

    def setup_frozen_fields_dict(self):
        self.frozen_fields_dict = {
            note_type: dict.fromkeys(fields, "")
            for note_type, fields in globals.FIELDS_DICT.items()
        }
        for match in globals.FROZEN_REGEXP.finditer(self.file):
            note_type, fields = match.group(1), match.group(2)
            virtual_note = note_type + "\n" + fields
            parsed_fields = Note(virtual_note).fields
            self.frozen_fields_dict[note_type] = parsed_fields

    def setup_target_deck(self):
        result = globals.DECK_REGEXP.search(self.file)
        if result is not None:
            self.target_deck = result.group(1)
        else:
            self.target_deck = globals.NOTE_DICT_TEMPLATE["deckName"]

    def setup_global_tags(self):
        result = globals.TAG_REGEXP.search(self.file)
        if result is not None:
            self.global_tags = result.group(1)
        else:
            self.global_tags = ""

    @property
    def hash(self):
        return hashlib.sha256(self.file.encode('utf-8')).hexdigest()

    def scan_file(self):
        """Sort notes from file into adding vs editing."""
        logging.info("Scanning file " + self.filename + " for notes...")
        self.setup_frozen_fields_dict()
        self.setup_target_deck()
        self.setup_global_tags()
        self.notes_to_add = list()
        self.id_indexes = list()
        self.notes_to_edit = list()
        self.notes_to_delete = list()
        self.inline_notes_to_add = list()
        self.inline_id_indexes = list()
        for note_match in globals.NOTE_REGEXP.finditer(self.file):
            note, position = note_match.group(1), note_match.end(1)
            parsed = Note(note).parse(
                self.target_deck,
                url=self.url,
                frozen_fields_dict=self.frozen_fields_dict
            )
            if parsed.id is None:
                # Need to make sure global_tags get added.
                parsed.note["tags"] += self.global_tags.split(globals.TAG_SEP)
                self.notes_to_add.append(parsed.note)
                self.id_indexes.append(position)
            elif parsed.id not in globals.EXISTING_IDS:
                print(
                    "Warning! Note with id ",
                    parsed.id,
                    " in file ",
                    self.filename,
                    " does not exist in Anki!"
                )
            else:
                self.notes_to_edit.append(parsed)
        for inline_note_match in globals.INLINE_REGEXP.finditer(self.file):
            note = inline_note_match.group(1)
            position = inline_note_match.end(1)
            parsed = InlineNote(note).parse(
                self.target_deck,
                url=self.url,
                frozen_fields_dict=self.frozen_fields_dict
            )
            if parsed.id is None:
                # Need to make sure global_tags get added.
                parsed.note["tags"] += self.global_tags.split(globals.TAG_SEP)
                self.inline_notes_to_add.append(parsed.note)
                self.inline_id_indexes.append(position)
            elif parsed.id not in globals.EXISTING_IDS:
                print(
                    "Warning! Note with id ",
                    parsed.id,
                    " in file ",
                    self.filename,
                    " does not exist in Anki!"
                )
            else:
                self.notes_to_edit.append(parsed)
        # Finally, scan for deleting notes
        for match in globals.EMPTY_REGEXP.finditer(self.file):
            self.notes_to_delete.append(
                int(match.group(1))
            )

    @staticmethod
    def id_to_str(id, inline=False, comment=False):
        """Get the string repr of id."""
        result = globals.ID_PREFIX + str(id)
        if comment:
            result = "<!--" + result + "-->"
        if inline:
            result += " "
        else:
            result += "\n"
        return result

    def write_ids(self):
        """Write the identifiers to self.file."""
        logging.info("Writing new note IDs to file," + self.filename + "...")
        self.file = string_insert(
            self.file, list(
                zip(
                    self.id_indexes, [
                        self.id_to_str(id, comment=globals.CONFIG_DATA["Comment"])
                        for id in self.note_ids[:len(self.notes_to_add)]
                        if id is not None
                    ]
                )
            ) + list(
                zip(
                    self.inline_id_indexes, [
                        self.id_to_str(
                            id, inline=True,
                            comment=globals.CONFIG_DATA["Comment"]
                        )
                        for id in self.note_ids[len(self.notes_to_add):]
                        if id is not None
                    ]
                )
            )
        )

    def remove_empties(self):
        """Remove empty notes from self.file."""
        self.file = globals.EMPTY_REGEXP.sub(
            "", self.file
        )

    def write_file(self):
        """Write to the actual os file"""
        if self.file != self.original_file:
            write_safe(self.filename, self.file)

    def get_add_notes(self):
        """Get the AnkiConnect-formatted request to add notes."""
        return AnkiConnect.request(
            "multi",
            actions=[
                AnkiConnect.request(
                    "addNote",
                    note=note
                )
                for note in self.notes_to_add + self.inline_notes_to_add
            ]
        )

    def get_delete_notes(self):
        """Get the AnkiConnect-formatted request to delete a note."""
        return AnkiConnect.request(
            "deleteNotes",
            notes=self.notes_to_delete
        )

    def get_update_fields(self):
        """Get the AnkiConnect-formatted request to update fields."""
        return AnkiConnect.request(
            "multi",
            actions=[
                AnkiConnect.request(
                    "updateNoteFields", note={
                        "id": parsed.id,
                        "fields": parsed.note["fields"],
                        "audio": parsed.note["audio"]
                    }
                )
                for parsed in self.notes_to_edit
            ]
        )

    def get_note_info(self):
        """Get the AnkiConnect-formatted request to get note info."""
        return AnkiConnect.request(
            "notesInfo",
            notes=[
                parsed.id for parsed in self.notes_to_edit
            ]
        )

    def get_cards(self):
        """Get the card IDs for all notes that need to be edited."""
        logging.info("Getting card IDs")
        self.cards = list()
        for info in self.card_ids:
            self.cards += info["cards"]

    def get_change_decks(self):
        """Get the AnkiConnect-formatted request to change decks."""
        return AnkiConnect.request(
            "changeDeck",
            cards=self.cards,
            deck=self.target_deck
        )

    def get_clear_tags(self):
        """Get the AnkiConnect-formatted request to clear tags."""
        return AnkiConnect.request(
            "removeTags",
            notes=[parsed.id for parsed in self.notes_to_edit],
            tags=" ".join(self.tags)
        )

    def get_add_tags(self):
        """Get the AnkiConnect-formatted request to add tags."""
        return AnkiConnect.request(
            "multi",
            actions=[
                AnkiConnect.request(
                    "addTags",
                    notes=[parsed.id],
                    tags=" ".join(parsed.note["tags"]) + " " + self.global_tags
                )
                for parsed in self.notes_to_edit
            ]
        )


class RegexFile(File):

    def add_spans_to_ignore(self):
        """Mark sections of the file as places not to expect a note."""
        self.ignore_spans += spans(globals.NOTE_REGEXP, self.file)
        self.ignore_spans += spans(globals.INLINE_REGEXP, self.file)
        self.ignore_spans += spans(
            globals.OBS_INLINE_MATH_REGEXP, self.file
        )
        self.ignore_spans += spans(
            globals.OBS_DISPLAY_MATH_REGEXP, self.file
        )
        self.ignore_spans += spans(
            globals.OBS_CODE_REGEXP, self.file
        )
        self.ignore_spans += spans(
            globals.OBS_DISPLAY_CODE_REGEXP, self.file
        )

    def scan_file(self):
        """Sort notes from file into adding vs editing."""
        logging.info("Scanning file" + self.filename + " for notes...")
        self.setup_frozen_fields_dict()
        self.setup_target_deck()
        self.setup_global_tags()
        self.ignore_spans = list()
        # The above ensures that the script won't match a RegexNote inside
        # a Note or InlineNote
        self.notes_to_add = list()
        self.id_indexes = list()
        self.notes_to_edit = list()
        self.notes_to_delete = list()
        self.inline_notes_to_add = list()  # To avoid overriding get_add_notes
        self.add_spans_to_ignore()
        for note_type, regexp in globals.CONFIG_DATA["CUSTOM_REGEXPS"].items():
            if regexp:
                self.search(note_type, regexp)
        # Finally, scan for deleting notes
        for match in globals.EMPTY_REGEXP.finditer(self.file):
            self.notes_to_delete.append(
                int(match.group(1))
            )

    def search(self, note_type, regexp):
        """
        Search the file for regex matches of this type,
        ignoring matches inside ignore_spans,
        and adding any matches to ignore_spans.
        """
        regexp_tags_id = re.compile(
            "".join(
                [
                    regexp,
                    RegexNote.TAG_REGEXP_STR,
                    RegexNote.ID_REGEXP_STR
                ]
            ), flags=re.MULTILINE
        )
        regexp_id = re.compile(
            regexp + RegexNote.ID_REGEXP_STR, flags=re.MULTILINE
        )
        regexp_tags = re.compile(
            regexp + RegexNote.TAG_REGEXP_STR, flags=re.MULTILINE
        )
        regexp = re.compile(
            regexp, flags=re.MULTILINE
        )
        for match in findignore(regexp_tags_id, self.file, self.ignore_spans):
            # This note has id, so we update it
            self.ignore_spans.append(match.span())
            parsed = RegexNote(match, note_type, tags=True, id=True).parse(
                self.target_deck,
                url=self.url,
                frozen_fields_dict=self.frozen_fields_dict
            )
            if parsed.id not in globals.EXISTING_IDS:
                print(
                    "Warning! Note with id ",
                    parsed.id,
                    " in file ",
                    self.filename,
                    " does not exist in Anki!"
                )
            else:
                self.notes_to_edit.append(parsed)
        for match in findignore(regexp_id, self.file, self.ignore_spans):
            # This note has id, so we update it
            self.ignore_spans.append(match.span())
            parsed = RegexNote(match, note_type, tags=False, id=True).parse(
                self.target_deck,
                url=self.url,
                frozen_fields_dict=self.frozen_fields_dict
            )
            if parsed.id not in globals.EXISTING_IDS:
                print(
                    "Warning! Note with id ",
                    parsed.id,
                    " in file ",
                    self.filename,
                    " does not exist in Anki!"
                )
            else:
                self.notes_to_edit.append(parsed)
        for match in findignore(regexp_tags, self.file, self.ignore_spans):
            # This note has no id, so we add it
            self.ignore_spans.append(match.span())
            parsed = RegexNote(match, note_type, tags=True, id=False).parse(
                self.target_deck,
                url=self.url,
                frozen_fields_dict=self.frozen_fields_dict
            )
            if parsed == 1:
                # Error code
                continue
            parsed.note["tags"] += self.global_tags.split(globals.TAG_SEP)
            self.notes_to_add.append(
                parsed.note
            )
            self.id_indexes.append(match.end())
        for match in findignore(regexp, self.file, self.ignore_spans):
            # This note has no id, so we update it
            self.ignore_spans.append(match.span())
            parsed = RegexNote(match, note_type, tags=False, id=False).parse(
                self.target_deck,
                url=self.url,
                frozen_fields_dict=self.frozen_fields_dict
            )
            if parsed == 1:
                # Error code
                continue
            parsed.note["tags"] += self.global_tags.split(globals.TAG_SEP)
            self.notes_to_add.append(
                parsed.note
            )
            self.id_indexes.append(match.end())

    def fix_newline_ids(self):
        """Removes double newline then ids from self.file."""
        double_regexp = re.compile(
            r"(\r\n|\r|\n){2}(?:<!--)?" + globals.ID_PREFIX + r"\d+"
        )
        self.file = double_regexp.sub(
            lambda x: x.group()[1:],
            self.file
        )

    def write_ids(self):
        """Write the identifiers to self.file."""
        logging.info("Writing new note IDs to file," + self.filename + "...")
        self.file = string_insert(
            self.file, zip(
                self.id_indexes, [
                    "\n" + File.id_to_str(id, comment=globals.CONFIG_DATA["Comment"])
                    for id in self.note_ids
                    if id is not None
                ]
            )
        )
        self.fix_newline_ids()

    def remove_empties(self):
        """Remove empty notes from self.file."""
        self.file = globals.EMPTY_REGEXP.sub(
            "", self.file
        )
