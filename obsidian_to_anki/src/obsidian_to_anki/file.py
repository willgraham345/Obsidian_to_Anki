"""Class for performing script operations at the file-level."""

import json
import os
import re
import hashlib
import logging
import uuid as uuid_module

# Cache compiled regex variants for RegexFile.search() keyed by base pattern string
_regex_cache: dict[str, tuple] = {}

from . import globals
from .note import Note, InlineNote, RegexNote
from .utils import string_insert, write_safe, findignore, spans
from .anki_connect import AnkiConnect

_IMG_SRC_RE = re.compile(r'<img[^>]+src="([^"]+)"')


def _extract_images(fields: dict) -> list:
    """Return image basenames found in formatted HTML fields."""
    imgs = []
    for html in fields.values():
        imgs += _IMG_SRC_RE.findall(html)
    return imgs


def _db_upsert_note(parsed, file_path: str, line_number: int) -> str:
    """Upsert parsed note into DB; return the UUID. Returns None if DB not set."""
    db = globals.NOTE_DB
    if db is None:
        return None
    field_names = list(parsed.note["fields"].keys())
    field_1 = parsed.note["fields"].get(field_names[0]) if field_names else None
    field_2 = parsed.note["fields"].get(field_names[1]) if len(field_names) > 1 else None
    images = _extract_images(parsed.note["fields"])
    existing = db.get_note_by_location(file_path, line_number, parsed.note["modelName"])
    note_uuid = existing["id"] if existing else str(uuid_module.uuid4())
    db.upsert_note(
        uuid=note_uuid,
        anki_id=parsed.id,
        file_path=file_path,
        line_number=line_number,
        note_type=parsed.note["modelName"],
        field_1=field_1,
        field_2=field_2,
        image_paths=images,
        tags=parsed.note["tags"],
        deck_name=parsed.note["deckName"],
    )
    return note_uuid

class File:
    """Class for performing script operations at the file-level. Requires config to be set."""

    def __init__(self, filepath):
        """Perform initial file reading and attribute setting."""
        self.filename = filepath
        self.path = os.path.abspath(filepath)
        if globals.CONFIG_DATA["Vault"] and globals.VAULT_PATH_REGEXP.search(self.path):
            self.url = "obsidian://vault/{}".format(
                globals.VAULT_PATH_REGEXP.search(self.path).group(1)
            ).replace("\\", "/")
        else:
            self.url = ""
        with open(self.filename, encoding='utf_8') as f:
            self.file = f.read()
            self.original_file = self.file

    def _setup_scan(self):
        """Shared initialization for scan_file() in File and RegexFile."""
        self.setup_frozen_fields_dict()
        self.setup_target_deck()
        self.setup_global_tags()
        self.notes_to_add = []
        self.id_indexes = []
        self.notes_to_edit = []
        self.notes_to_delete = []
        self.inline_notes_to_add = []
        self.inline_id_indexes = []
        # Parallel list to notes_to_add tracking DB UUIDs (for mark_synced after addNote)
        self.uuid_for_add = []
        self.uuid_for_inline_add = []

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

    def _line_of(self, char_pos: int) -> int:
        """Return 1-based line number for a character position in self.file."""
        return self.file[:char_pos].count('\n') + 1

    def _vault_rel_path(self) -> str:
        """Return vault-relative path if vault configured, else absolute path."""
        if globals.CONFIG_DATA.get("Vault") and globals.VAULT_PATH_REGEXP.search(self.path):
            return globals.VAULT_PATH_REGEXP.search(self.path).group(1)
        return self.path

    @property
    def hash(self):
        return hashlib.sha256(self.file.encode('utf-8')).hexdigest()

    def _handle_block_note(self, note_match):
        """Parse a block note match and route to add/edit/DB."""
        note, position = note_match.group(1), note_match.end(1)
        parsed = Note(note).parse(
            self.target_deck,
            url=self.url,
            frozen_fields_dict=self.frozen_fields_dict
        )
        file_path = self._vault_rel_path()
        line_no = self._line_of(note_match.start(1))
        parsed = self._apply_change_detection(parsed, file_path, line_no)
        if parsed.id is None:
            parsed.note["tags"] += self.global_tags.split(globals.TAG_SEP)
            note_uuid = _db_upsert_note(parsed, file_path, line_no)
            self.notes_to_add.append(parsed.note)
            self.id_indexes.append(position)
            self.uuid_for_add.append(note_uuid)
        elif parsed.id not in globals.EXISTING_IDS:
            print(
                "Warning! Note with id ",
                parsed.id,
                " in file ",
                self.filename,
                " does not exist in Anki!"
            )
        else:
            _db_upsert_note(parsed, file_path, line_no)
            self.notes_to_edit.append(parsed)

    def _handle_inline_note(self, inline_note_match):
        """Parse an inline note match and route to add/edit/DB."""
        note = inline_note_match.group(1)
        position = inline_note_match.end(1)
        parsed = InlineNote(note).parse(
            self.target_deck,
            url=self.url,
            frozen_fields_dict=self.frozen_fields_dict
        )
        file_path = self._vault_rel_path()
        line_no = self._line_of(inline_note_match.start(1))
        parsed = self._apply_change_detection(parsed, file_path, line_no)
        if parsed.id is None:
            parsed.note["tags"] += self.global_tags.split(globals.TAG_SEP)
            note_uuid = _db_upsert_note(parsed, file_path, line_no)
            self.inline_notes_to_add.append(parsed.note)
            self.inline_id_indexes.append(position)
            self.uuid_for_inline_add.append(note_uuid)
        elif parsed.id not in globals.EXISTING_IDS:
            print(
                "Warning! Note with id ",
                parsed.id,
                " in file ",
                self.filename,
                " does not exist in Anki!"
            )
        else:
            _db_upsert_note(parsed, file_path, line_no)
            self.notes_to_edit.append(parsed)

    def _apply_change_detection(self, parsed, file_path: str, line_no: int):
        """If existing DB record has different content, queue old anki_id for deletion."""
        db = globals.NOTE_DB
        if db is None or parsed.id is not None:
            return parsed
        existing = db.get_note_by_location(file_path, line_no, parsed.note["modelName"])
        if existing and existing.get("anki_id"):
            field_names = list(parsed.note["fields"].keys())
            new_f1 = parsed.note["fields"].get(field_names[0]) if field_names else None
            new_f2 = parsed.note["fields"].get(field_names[1]) if len(field_names) > 1 else None
            if existing["field_1"] != new_f1 or existing["field_2"] != new_f2:
                # Content changed: delete old Anki card, re-add as new
                self.notes_to_delete.append(existing["anki_id"])
        return parsed

    def scan_file(self):
        """Sort notes from file into adding vs editing."""
        logging.info("Scanning file " + self.filename + " for notes...")
        self._setup_scan()
        for note_match in globals.NOTE_REGEXP.finditer(self.file):
            self._handle_block_note(note_match)
        for inline_note_match in globals.INLINE_REGEXP.finditer(self.file):
            self._handle_inline_note(inline_note_match)
        # Finally, scan for deleting notes
        for match in globals.EMPTY_REGEXP.finditer(self.file):
            self.notes_to_delete.append(int(match.group(1)))

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

    def update_db_anki_ids(self):
        """After addNote returns IDs, persist them in the DB."""
        db = globals.NOTE_DB
        if db is None or not hasattr(self, 'note_ids'):
            return
        block_ids = self.note_ids[:len(self.notes_to_add)]
        inline_ids = self.note_ids[len(self.notes_to_add):]
        for note_uuid, anki_id in zip(self.uuid_for_add, block_ids):
            if note_uuid and anki_id is not None:
                db.mark_synced(note_uuid, anki_id)
        for note_uuid, anki_id in zip(self.uuid_for_inline_add, inline_ids):
            if note_uuid and anki_id is not None:
                db.mark_synced(note_uuid, anki_id)

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

    _DOUBLE_NEWLINE_ID_REGEXP = re.compile(
        r"(\r\n|\r|\n){2}(?:<!--)?" + globals.ID_PREFIX + r"\d+"
    )

    @staticmethod
    def _drop_first_char(m):
        first_newline = m.group(1)
        return m.group()[len(first_newline):]

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
        self._setup_scan()
        self.ignore_spans = []
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
        if regexp not in _regex_cache:
            _regex_cache[regexp] = (
                re.compile(regexp + RegexNote.TAG_REGEXP_STR + RegexNote.ID_REGEXP_STR, re.MULTILINE),
                re.compile(regexp + RegexNote.ID_REGEXP_STR, re.MULTILINE),
                re.compile(regexp + RegexNote.TAG_REGEXP_STR, re.MULTILINE),
                re.compile(regexp, re.MULTILINE),
            )
        regexp_tags_id, regexp_id, regexp_tags, regexp = _regex_cache[regexp]
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
                _db_upsert_note(parsed, self._vault_rel_path(), self._line_of(match.start()))
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
                _db_upsert_note(parsed, self._vault_rel_path(), self._line_of(match.start()))
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
                continue
            file_path = self._vault_rel_path()
            line_no = self._line_of(match.start())
            parsed = self._apply_change_detection(parsed, file_path, line_no)
            parsed.note["tags"] += self.global_tags.split(globals.TAG_SEP)
            note_uuid = _db_upsert_note(parsed, file_path, line_no)
            self.notes_to_add.append(parsed.note)
            self.id_indexes.append(match.end())
            self.uuid_for_add.append(note_uuid)
        for match in findignore(regexp, self.file, self.ignore_spans):
            # This note has no id, so we add it
            self.ignore_spans.append(match.span())
            parsed = RegexNote(match, note_type, tags=False, id=False).parse(
                self.target_deck,
                url=self.url,
                frozen_fields_dict=self.frozen_fields_dict
            )
            if parsed == 1:
                continue
            file_path = self._vault_rel_path()
            line_no = self._line_of(match.start())
            parsed = self._apply_change_detection(parsed, file_path, line_no)
            parsed.note["tags"] += self.global_tags.split(globals.TAG_SEP)
            note_uuid = _db_upsert_note(parsed, file_path, line_no)
            self.notes_to_add.append(parsed.note)
            self.id_indexes.append(match.end())
            self.uuid_for_add.append(note_uuid)

    def fix_newline_ids(self):
        """Removes double newline then ids from self.file."""
        self.file = self._DOUBLE_NEWLINE_ID_REGEXP.sub(self._drop_first_char, self.file)

    def write_ids(self):
        """Write the identifiers to self.file."""
        logging.info("Writing new note IDs to file," + self.filename + "...")
        self.file = string_insert(
            self.file, list(zip(
                self.id_indexes, [
                    "\n" + File.id_to_str(id, comment=globals.CONFIG_DATA["Comment"])
                    for id in self.note_ids
                    if id is not None
                ]
            ))
        )
        self.fix_newline_ids()
