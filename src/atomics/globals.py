"""Global variables and shared objects for the atomics package."""

import collections
import markdown
import re
from enum import StrEnum


class NoteAction(StrEnum):
    ADD          = "add"
    EDIT         = "edit"
    RETYPE       = "retype"
    LINK         = "link"
    REVIEW       = "review"
    SKIP         = "skip"
    NONE         = "none"
    UPDATE_TYPE   = "update_type"
    UPDATE_FIELDS  = "update_fields"
    UPDATE_FIELD_1 = "update_field_1"
    UPDATE_FIELD_2 = "update_field_2"
    UPDATE_DECK   = "update_deck"


class NoteState(StrEnum):
    NOT_IN_ANKI    = "not_in_anki"
    STALE_ID       = "stale_id"
    SYNCED         = "synced"
    MODIFY_TYPE    = "modify_type"
    MODIFY_FIELDS  = "modify_fields"
    MODIFY_FIELD_1 = "modify_field_1"
    MODIFY_FIELD_2 = "modify_field_2"
    MODIFY_DECK    = "modify_deck"

MEDIA = dict()

NOTE_DB = None  # NoteDB instance, set by App.__init__()

ID_PREFIX = "ID: "
TAG_PREFIX = "Tags: "
TAG_SEP = " "
Note_and_id = collections.namedtuple('Note_and_id', ['note', 'id'])
NOTE_DICT_TEMPLATE = {
    "deckName": "",
    "modelName": "",
    "fields": dict(),
    "options": {
        "allowDuplicate": False,
        "duplicateScope": "deck"
    },
    "tags": ["Obsidian_to_Anki"],
    # ^So that you can see what was added automatically.
    "audio": list()
}

CONFIG_DATA = dict()

md_parser = markdown.Markdown(
    extensions=[
        'fenced_code',
        'footnotes',
        'md_in_html',
        'tables',
        'nl2br',
        'sane_lists'
    ]
)

# This will be populated by the App class
EXISTING_IDS = list()
# This will be populated by the App class
FIELDS_DICT = dict()
# This will be populated by the App class
ADDED_MEDIA = list()
# This will be populated by the App class
FILE_HASHES = dict()

ANKI_PORT = 8765

UNMATCHED_DECK = "Obsidian Unmatched Transfer"

ANKI_CLOZE_REGEXP = re.compile(r'{{c\d+::[\s\S]+?}}')

# Obsidian source patterns used by File.add_spans_to_ignore() to exclude non-note regions
OBS_INLINE_MATH_REGEXP = re.compile(r"(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)", re.DOTALL)
OBS_DISPLAY_MATH_REGEXP = re.compile(r"\$\$(.*?)\$\$", re.DOTALL)
OBS_CODE_REGEXP = re.compile(r"(?<!`)`(?!`)(.*?)(?<!`)`(?!`)", re.DOTALL)
OBS_DISPLAY_CODE_REGEXP = re.compile(r"```[\s\S]*?```")