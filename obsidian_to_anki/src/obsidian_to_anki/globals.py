"""Global variables and shared objects for the obsidian_to_anki package."""

import collections
import markdown
import re

MEDIA = dict()

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

ANKI_CLOZE_REGEXP = re.compile(r'{{c\\d+::[\\s\\S]+?}}')