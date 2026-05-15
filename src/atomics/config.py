"""Deals with saving and loading the configuration file."""

import configparser
import os
import re

from .anki_connect import AnkiConnect
from .note import RegexNote
from . import globals

class Config:
    """Deals with saving and loading the configuration file."""

    # FIXME: Won't initialize, has errors
    def __init__(self):
        self.CONFIG_PATH = os.path.normpath(os.path.expanduser(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "..",
                "..",
                "obsidian_to_anki_config.ini"
            )
        ))

    def setup_syntax(self, config):
        """Sets up default syntax in the config object."""
        config.setdefault("Syntax", dict())
        config["Syntax"].setdefault(
            "Begin Note", "START"
        )
        config["Syntax"].setdefault(
            "End Note", "END"
        )
        config["Syntax"].setdefault(
            "Begin Inline Note", "STARTI"
        )
        config["Syntax"].setdefault(
            "End Inline Note", "ENDI"
        )
        config["Syntax"].setdefault(
            "Target Deck Line", "TARGET DECK"
        )
        config["Syntax"].setdefault(
            "File Tags Line", "FILE TAGS"
        )
        config["Syntax"].setdefault(
            "Delete Note Line", "DELETE"
        )
        config["Syntax"].setdefault(
            "Frozen Fields Line", "FROZEN"
        )

    def setup_defaults(self, config):
        """Sets up default values in the config file, not to do with syntax."""
        config.setdefault("Obsidian", dict())
        config["Obsidian"].setdefault("Vault path", "")
        config["Obsidian"].setdefault("Vault name", "")
        config["Obsidian"].setdefault("Add file link", "False")
        config["DEFAULT"] = dict()  # Removes DEFAULT if it's there.
        config.setdefault("Defaults", dict())
        config["Defaults"].setdefault(
            "Tag", "Obsidian_to_Anki"
        )
        config["Defaults"].setdefault(
            "Deck", "Default"
        )
        config["Defaults"].setdefault(
            "CurlyCloze", "False"
        )
        config["Defaults"].setdefault(
            "Regex", "False"
        )
        config["Defaults"].setdefault(
            "ID Comments", "True"
        )
        config["Defaults"].setdefault(
            "Anki Path", ""
        )
        config["Defaults"].setdefault(
            "Anki Profile", ""
        )
        config.setdefault("Folder Decks", dict())

    def update_config(self):
        """Update config with new notes."""
        print("Updating configuration file...")
        config = configparser.ConfigParser()
        config.optionxform = str
        if os.path.exists(self.CONFIG_PATH):
            print("Config file exists, reading...")
            config.read(self.CONFIG_PATH, encoding='utf-8-sig')
        note_types = AnkiConnect.invoke("modelNames")
        config.setdefault("Atomics", dict())
        for note in note_types:
            config["Atomics"].setdefault(note, "")
        config.setdefault("File Stem Notes", dict())
        for note in note_types:
            config["File Stem Notes"].setdefault(note, "False")
        self.setup_syntax(config)
        self.setup_defaults(config)
        with open(self.CONFIG_PATH, "w", encoding='utf_8') as configfile:
            config.write(configfile)
        print("Configuration file updated!")

    def load_syntax(self, config):
        """Reads and loads syntax from the config object."""
        def syn(key, default):
            return re.escape(config.get("Syntax", key, fallback=default))

        globals.CONFIG_DATA["NOTE_PREFIX"]  = syn("Begin Note", "START")
        globals.CONFIG_DATA["NOTE_SUFFIX"]  = syn("End Note", "END")
        globals.CONFIG_DATA["INLINE_PREFIX"] = syn("Begin Inline Note", "STARTI")
        globals.CONFIG_DATA["INLINE_SUFFIX"] = syn("End Inline Note", "ENDI")
        globals.CONFIG_DATA["DECK_LINE"]    = syn("Target Deck Line", "TARGET DECK")
        globals.CONFIG_DATA["TAG_LINE"]     = syn("File Tags Line", "FILE TAGS")
        globals.CONFIG_DATA["FROZEN_LINE"]  = syn("Frozen Fields Line", "FROZEN")
        delete_line = re.escape(config.get("Syntax", "Delete Note Line", fallback="DELETE"))
        globals.EMPTY_REGEXP = re.compile(delete_line + RegexNote.ID_REGEXP_STR)
        globals.CONFIG_DATA["EMPTY_REGEXP"] = re.compile(delete_line + RegexNote.ID_REGEXP_STR)

    def load_defaults(self, config):
        """Loads default values not to do with syntax from config object."""
        globals.NOTE_DICT_TEMPLATE["tags"] = [
            config.get("Defaults", "Tag", fallback="Obsidian_to_Anki")
        ]
        globals.NOTE_DICT_TEMPLATE["deckName"] = config.get("Defaults", "Deck", fallback="Default")
        globals.CONFIG_DATA["CurlyCloze"] = config.getboolean("Defaults", "CurlyCloze", fallback=False)
        globals.CONFIG_DATA["Regex"]      = config.getboolean("Defaults", "Regex", fallback=False)
        globals.CONFIG_DATA["Comment"]    = config.getboolean("Defaults", "ID Comments", fallback=True)
        globals.CONFIG_DATA["Path"]       = config.get("Defaults", "Anki Path", fallback="")
        globals.CONFIG_DATA["Profile"]    = config.get("Defaults", "Anki Profile", fallback="")
        globals.CONFIG_DATA["Vault"]      = config.get("Obsidian", "Vault path", fallback="")
        globals.CONFIG_DATA["Vault name"] = config.get("Obsidian", "Vault name", fallback="")
        globals.CONFIG_DATA["Add file link"] = config.getboolean("Obsidian", "Add file link", fallback=False)

    def load_folder_decks(self, config):
        """Compile folder-to-deck regex mappings from [Folder Decks] config section."""
        folder_decks = []
        if "Folder Decks" in config:
            for pattern, deck_name in config["Folder Decks"].items():
                if pattern and deck_name:
                    folder_decks.append((re.compile(pattern), deck_name))
        globals.CONFIG_DATA["FOLDER_DECKS"] = folder_decks

    def load_config(self):
        """Load from an existing config file (assuming it exists)."""
        print("Loading configuration file...")
        config = configparser.ConfigParser()
        config.optionxform = str  # Allows for case sensitivity
        config.read(self.CONFIG_PATH, encoding='utf-8-sig')
        self.load_syntax(config)
        self.load_defaults(config)
        self.load_folder_decks(config)
        globals.CONFIG_DATA["ATOMICS"] = config["Atomics"]
        globals.CONFIG_DATA["FILE_STEM_NOTES"] = {
            k: config.getboolean("File Stem Notes", k, fallback=False)
            for k in config.options("File Stem Notes")
        } if "File Stem Notes" in config else {}
        print("Loaded successfully!")
