"""Class for performing script operations at the file-level."""

import json
import logging
import os
import re
import hashlib
import uuid as uuid_module
import urllib.parse

# Cache compiled regex variants for search() keyed by base pattern string
_regex_cache: dict[str, tuple] = {}

from . import globals
from .globals import NoteAction, NoteState
from .note import RegexNote
from .utils import findignore, spans
from .anki_connect import AnkiConnect, Action

_IMG_SRC_RE = re.compile(r'<img[^>]+src="([^"]+)"')
_STEM_RE = re.compile(r'<br><b>.*?</b>\s*$', re.DOTALL)


def _strip_stem(text: str | None) -> str | None:
    if text is None:
        return None
    return _STEM_RE.sub('', text)


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
    if existing is None:
        existing = db.get_note_by_content(
            file_path, parsed.note["modelName"], field_1, field_2, parsed.note["deckName"]
        )
    if existing is None:
        # field_2 changed AND line shifted → locate by stripped field_1 alone
        f1_core = field_1 or ""
        idx = f1_core.find('<br><b>')
        f1_core = f1_core[:idx] if idx >= 0 else f1_core
        idx = f1_core.find('<br><a href="obsidian://')
        f1_core = f1_core[:idx] if idx >= 0 else f1_core
        existing = db.get_note_by_field_1_stripped(
            file_path, parsed.note["modelName"], f1_core
        )
    note_uuid = existing["id"] if existing else str(uuid_module.uuid4())
    existing_anki_id = existing["anki_id"] if existing else None
    # Recover anki_id from the Anki snapshot when the DB record has none.
    # Covers both genuinely new records and cascade-corrupted false positives
    # whose existing DB entry was created without an anki_id.
    recovered_anki_id: int | None = None
    if existing_anki_id is None:
        recovered_anki_id = db.find_anki_note_by_content(
            parsed.note["modelName"], field_1, field_2
        )
    db.upsert_note(
        uuid=note_uuid,
        anki_id=parsed.id if parsed.id is not None else (
            existing_anki_id if existing_anki_id is not None else recovered_anki_id
        ),
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
        self.file_stem = os.path.splitext(os.path.basename(self.path))[0]
        if globals.CONFIG_DATA["Vault"] and globals.VAULT_PATH_REGEXP.search(self.path):
            vault_rel = globals.VAULT_PATH_REGEXP.search(self.path).group(1).replace("\\", "/")
            vault_name = globals.CONFIG_DATA.get("Vault name") or os.path.basename(globals.CONFIG_DATA["Vault"])
            self.url = (
                "obsidian://open?vault="
                + urllib.parse.quote(vault_name, safe="")
                + "&amp;file="
                + urllib.parse.quote(vault_rel, safe="/")
            )
        else:
            self.url = ""
        with open(self.filename, encoding='utf_8') as f:
            self.file = f.read()

    def _setup_scan(self):
        """Initialize lists for scan_file()."""
        self.setup_frozen_fields_dict()
        self.setup_target_deck()
        self.setup_global_tags()
        self.notes_to_add = []
        self.regex_id_indexes = []
        self.notes_to_edit = []
        self.notes_to_delete = []
        self.uuid_for_regex_add = []
        self.pending_review = []
        self.notes_skipped = []
        self.scanned_uuids: set[str] = set()

    def setup_frozen_fields_dict(self):
        self.frozen_fields_dict = {
            note_type: dict.fromkeys(fields, "")
            for note_type, fields in globals.FIELDS_DICT.items()
        }

    def setup_target_deck(self):
        result = globals.DECK_REGEXP.search(self.file)
        if result is not None:
            self.target_deck = result.group(1)
            return
        if globals.CONFIG_DATA.get("Vault") and globals.CONFIG_DATA.get("FOLDER_DECKS"):
            vault_rel = self._vault_rel_path().replace("\\", "/")
            for pattern, deck_name in globals.CONFIG_DATA["FOLDER_DECKS"]:
                if pattern.search(vault_rel):
                    self.target_deck = deck_name
                    return
            self.target_deck = globals.UNMATCHED_DECK
            return
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

    def add_spans_to_ignore(self):
        """Mark math and code sections as regions to skip during regex search."""
        self.ignore_spans += spans(globals.OBS_INLINE_MATH_REGEXP, self.file)
        self.ignore_spans += spans(globals.OBS_DISPLAY_MATH_REGEXP, self.file)
        self.ignore_spans += spans(globals.OBS_CODE_REGEXP, self.file)
        self.ignore_spans += spans(globals.OBS_DISPLAY_CODE_REGEXP, self.file)

    def _apply_change_detection(self, parsed, file_path: str, line_no: int):
        """If DB record has a valid anki_id and content changed, route to edit."""
        db = globals.NOTE_DB
        if db is None or parsed.id is not None:
            return parsed
        existing = db.get_note_by_location(file_path, line_no, parsed.note["modelName"])
        if not existing or not existing.get("anki_id"):
            return parsed
        if existing["anki_id"] not in globals.EXISTING_IDS:
            return parsed

        field_names = list(parsed.note["fields"].keys())
        new_f1 = _strip_stem(parsed.note["fields"].get(field_names[0]) if field_names else None)
        new_f2 = parsed.note["fields"].get(field_names[1]) if len(field_names) > 1 else None
        if _strip_stem(existing["field_1"]) != new_f1 or existing["field_2"] != new_f2:
            return globals.Note_and_id(note=parsed.note, id=existing["anki_id"])
        return parsed

    def _atomic_state_flow(
        self,
        parsed,
        file_path: str,
        line_no: int,
        note_uuid: str | None,
    ) -> NoteAction:
        """Compute diff state and recommended action for an atomic note.

        Returns routing: NoteAction.ADD/EDIT/RETYPE/LINK/REVIEW/SKIP.
        Writes state + recommended_action to DB. Appends to pending_review
        for LINK and REVIEW outcomes.
        """
        db = globals.NOTE_DB
        if db is None or note_uuid is None:
            if parsed.id is not None and parsed.id in globals.EXISTING_IDS:
                return NoteAction.EDIT
            return NoteAction.ADD

        field_names = list(parsed.note["fields"].keys())
        f1 = _strip_stem(parsed.note["fields"].get(field_names[0]) if field_names else None)
        f2 = parsed.note["fields"].get(field_names[1]) if len(field_names) > 1 else None

        # Prefer the file-embedded Anki ID; fall back to the DB record's anki_id.
        # This ensures notes recovered via snapshot matching (_recover_anki_ids /
        # find_anki_note_by_content) are not re-routed as false-positive adds.
        effective_id = parsed.id
        if effective_id is None:
            db_note = db.get_note(note_uuid)
            effective_id = db_note["anki_id"] if db_note else None

        if effective_id is not None:
            if effective_id not in globals.EXISTING_IDS:
                candidates = db.similarity_search(f1, f2, parsed.note["modelName"])
                action = NoteAction.LINK if len(candidates) == 1 else NoteAction.REVIEW
                db.set_state_and_action(note_uuid, NoteState.STALE_ID, action)
                self.pending_review.append({
                    "uuid": note_uuid, "parsed": parsed,
                    "candidates": candidates, "file_path": file_path, "line_no": line_no,
                })
                return action

            snap = db._conn.execute(
                "SELECT * FROM anki_notes WHERE anki_id = ?", (effective_id,)
            ).fetchone()
            if snap is None:
                return NoteAction.EDIT

            f1_anki = _strip_stem(snap["field_1"])
            f2_anki = snap["field_2"]
            f1_diff = f1 != f1_anki
            f2_diff = f2 != f2_anki

            if parsed.note["modelName"] != snap["note_type"]:
                db.set_state_and_action(note_uuid, NoteState.MODIFY_TYPE, NoteAction.UPDATE_TYPE)
                return NoteAction.RETYPE
            elif f1_diff and f2_diff:
                db.set_state_and_action(note_uuid, NoteState.MODIFY_FIELDS, NoteAction.UPDATE_FIELDS)
            elif f1_diff:
                db.set_state_and_action(note_uuid, NoteState.MODIFY_FIELD_1, NoteAction.UPDATE_FIELD_1)
            elif f2_diff:
                db.set_state_and_action(note_uuid, NoteState.MODIFY_FIELD_2, NoteAction.UPDATE_FIELD_2)
            elif parsed.note["deckName"] != snap["deck_name"]:
                db.set_state_and_action(note_uuid, NoteState.MODIFY_DECK, NoteAction.UPDATE_DECK)
            else:
                db.set_state_and_action(note_uuid, NoteState.SYNCED, NoteAction.NONE)
                return NoteAction.SKIP
            return NoteAction.EDIT

        candidates = db.similarity_search(f1, f2, parsed.note["modelName"])
        if len(candidates) == 0:
            db.set_state_and_action(note_uuid, NoteState.NOT_IN_ANKI, NoteAction.ADD)
            return NoteAction.ADD
        action = NoteAction.LINK if len(candidates) == 1 else NoteAction.REVIEW
        db.set_state_and_action(note_uuid, NoteState.NOT_IN_ANKI, action)
        self.pending_review.append({
            "uuid": note_uuid, "parsed": parsed,
            "candidates": candidates, "file_path": file_path, "line_no": line_no,
        })
        return action

    def _route_atomic(self, routing: NoteAction, parsed, note_uuid: str | None, match_end: int) -> None:
        """Route an atomic to the appropriate list based on _atomic_state_flow result."""
        if routing == NoteAction.ADD:
            self.notes_to_add.append(parsed.note)
            self.regex_id_indexes.append(match_end)
            self.uuid_for_regex_add.append(note_uuid)
        elif routing == NoteAction.RETYPE:
            self.notes_to_delete.append(parsed.id)
            self.notes_to_add.append(parsed.note)
            self.regex_id_indexes.append(match_end)
            self.uuid_for_regex_add.append(note_uuid)
        elif routing == NoteAction.EDIT:
            self.notes_to_edit.append(parsed)
        elif routing == NoteAction.SKIP:
            self.notes_skipped.append(parsed)
        # LINK, REVIEW → pending_review only (handled in Phase 4 interactive prompt)

    def scan_file(self):
        """Scan file for atomic (regex) notes and route to add/edit lists."""
        logging.info("Scanning file %s for notes...", self.filename)
        self._setup_scan()
        self.ignore_spans = []
        self.add_spans_to_ignore()
        for note_type, regexp in globals.CONFIG_DATA.get("ATOMICS", {}).items():
            if regexp:
                self.search(note_type, regexp)

    def search(self, note_type, regexp):
        """Search the file for atomic regex matches and route via _atomic_state_flow."""
        if regexp not in _regex_cache:
            # Anchor the plain pattern to EOL so trailing non-greedy groups
            # (e.g. `(.*?)`) expand to capture the full field instead of
            # matching zero characters.
            plain_pat = regexp if regexp.endswith('$') else regexp + '$'
            _regex_cache[regexp] = (
                re.compile(regexp + RegexNote.TAG_REGEXP_STR + RegexNote.ID_REGEXP_STR, re.MULTILINE),
                re.compile(regexp + RegexNote.ID_REGEXP_STR, re.MULTILINE),
                re.compile(regexp + RegexNote.TAG_REGEXP_STR, re.MULTILINE),
                re.compile(plain_pat, re.MULTILINE),
            )
        regexp_tags_id, regexp_id, regexp_tags, regexp_plain = _regex_cache[regexp]

        for match in findignore(regexp_tags_id, self.file, self.ignore_spans):
            self.ignore_spans.append(match.span())
            parsed = RegexNote(match, note_type, tags=True, id=True).parse(
                self.target_deck, url=self.url,
                frozen_fields_dict=self.frozen_fields_dict, file_stem=self.file_stem,
            )
            file_path = self._vault_rel_path()
            line_no = self._line_of(match.start())
            note_uuid = _db_upsert_note(parsed, file_path, line_no)
            if note_uuid is not None:
                self.scanned_uuids.add(note_uuid)
            if globals.NOTE_DB is not None and note_uuid is None:
                logging.warning("DB write failed for atomic at %s:%d — skipping", file_path, line_no)
                continue
            routing = self._atomic_state_flow(parsed, file_path, line_no, note_uuid)
            self._route_atomic(routing, parsed, note_uuid, match.end())

        for match in findignore(regexp_id, self.file, self.ignore_spans):
            self.ignore_spans.append(match.span())
            parsed = RegexNote(match, note_type, tags=False, id=True).parse(
                self.target_deck, url=self.url,
                frozen_fields_dict=self.frozen_fields_dict, file_stem=self.file_stem,
            )
            file_path = self._vault_rel_path()
            line_no = self._line_of(match.start())
            note_uuid = _db_upsert_note(parsed, file_path, line_no)
            if note_uuid is not None:
                self.scanned_uuids.add(note_uuid)
            if globals.NOTE_DB is not None and note_uuid is None:
                logging.warning("DB write failed for atomic at %s:%d — skipping", file_path, line_no)
                continue
            routing = self._atomic_state_flow(parsed, file_path, line_no, note_uuid)
            self._route_atomic(routing, parsed, note_uuid, match.end())

        for match in findignore(regexp_tags, self.file, self.ignore_spans):
            self.ignore_spans.append(match.span())
            parsed = RegexNote(match, note_type, tags=True, id=False).parse(
                self.target_deck, url=self.url,
                frozen_fields_dict=self.frozen_fields_dict, file_stem=self.file_stem,
            )
            if parsed == 1:
                continue
            if self.global_tags.strip():
                parsed.note["tags"] += [t for t in self.global_tags.split(globals.TAG_SEP) if t]
            file_path = self._vault_rel_path()
            line_no = self._line_of(match.start())
            note_uuid = _db_upsert_note(parsed, file_path, line_no)
            if note_uuid is not None:
                self.scanned_uuids.add(note_uuid)
            if globals.NOTE_DB is not None and note_uuid is None:
                logging.warning("DB write failed for atomic at %s:%d — skipping", file_path, line_no)
                continue
            routing = self._atomic_state_flow(parsed, file_path, line_no, note_uuid)
            self._route_atomic(routing, parsed, note_uuid, match.end())

        for match in findignore(regexp_plain, self.file, self.ignore_spans):
            self.ignore_spans.append(match.span())
            parsed = RegexNote(match, note_type, tags=False, id=False).parse(
                self.target_deck, url=self.url,
                frozen_fields_dict=self.frozen_fields_dict, file_stem=self.file_stem,
            )
            if parsed == 1:
                continue
            if self.global_tags.strip():
                parsed.note["tags"] += [t for t in self.global_tags.split(globals.TAG_SEP) if t]
            file_path = self._vault_rel_path()
            line_no = self._line_of(match.start())
            note_uuid = _db_upsert_note(parsed, file_path, line_no)
            if note_uuid is not None:
                self.scanned_uuids.add(note_uuid)
            if globals.NOTE_DB is not None and note_uuid is None:
                logging.warning("DB write failed for atomic at %s:%d — skipping", file_path, line_no)
                continue
            routing = self._atomic_state_flow(parsed, file_path, line_no, note_uuid)
            self._route_atomic(routing, parsed, note_uuid, match.end())

    def update_db_anki_ids(self):
        """After addNote returns IDs, persist them in the DB."""
        db = globals.NOTE_DB
        if db is None or not hasattr(self, 'note_ids'):
            return
        for note_uuid, anki_id in zip(self.uuid_for_regex_add, self.note_ids):
            if note_uuid and anki_id is not None:
                db.mark_synced(note_uuid, anki_id)

    def get_add_notes(self):
        """Get the AnkiConnect-formatted request to add notes."""
        return AnkiConnect.request(
            Action.MULTI,
            actions=[
                AnkiConnect.request(Action.ADD_NOTE, note=note)
                for note in self.notes_to_add
            ]
        )

    def get_delete_notes(self):
        """Get the AnkiConnect-formatted request to delete notes."""
        return AnkiConnect.request(
            Action.DELETE_NOTES,
            notes=self.notes_to_delete
        )

    def get_update_notes(self):
        """Get the AnkiConnect-formatted request to atomically update fields and tags."""
        return AnkiConnect.request(
            Action.MULTI,
            actions=[
                AnkiConnect.request(
                    Action.UPDATE_NOTE, note={
                        "id": parsed.id,
                        "fields": parsed.note["fields"],
                        "tags": parsed.note["tags"] + [
                            t for t in self.global_tags.split(globals.TAG_SEP) if t
                        ],
                        "audio": parsed.note["audio"],
                    }
                )
                for parsed in self.notes_to_edit
            ]
        )

    def get_note_info(self):
        """Get the AnkiConnect-formatted request to get note info."""
        return AnkiConnect.request(
            Action.NOTES_INFO,
            notes=[parsed.id for parsed in self.notes_to_edit]
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
            Action.CHANGE_DECK,
            cards=self.cards,
            deck=self.target_deck
        )
