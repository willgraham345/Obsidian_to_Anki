"""Deals with saving and loading the configuration file."""

import configparser
import os
import re

from .anki_connect import AnkiConnect
from .note import RegexNote
from . import globals

class Config:
    """Deals with saving and loading the configuration file."""

    def __init__(self):
        self.CONFIG_PATH = os.path.expanduser(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "..",
                "obsidian_to_anki_config.ini"
            )
        )

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
            "GUI", "True"
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

    def update_config(self):
        """Update config with new notes."""
        print("Updating configuration file...")
        config = configparser.ConfigParser()
        config.optionxform = str
        if os.path.exists(self.CONFIG_PATH):
            print("Config file exists, reading...")
            config.read(self.CONFIG_PATH, encoding='utf-8-sig')
        note_types = AnkiConnect.invoke("modelNames")
        config.setdefault("Custom Regexps", dict())
        for note in note_types:
            config["Custom Regexps"].setdefault(note, "")
        self.setup_syntax(config)
        self.setup_defaults(config)
        with open(self.CONFIG_PATH, "w", encoding='utf_8') as configfile:
            config.write(configfile)
        print("Configuration file updated!")

    def load_syntax(self, config):
        """Reads and loads syntax from the config object."""
        globals.CONFIG_DATA["NOTE_PREFIX"] = re.escape(
            config["Syntax"]["Begin Note"]
        )
        globals.CONFIG_DATA["NOTE_SUFFIX"] = re.escape(
            config["Syntax"]["End Note"]
        )
        globals.CONFIG_DATA["INLINE_PREFIX"] = re.escape(
            config["Syntax"]["Begin Inline Note"]
        )
        globals.CONFIG_DATA["INLINE_SUFFIX"] = re.escape(
            config["Syntax"]["End Inline Note"]
        )
        globals.CONFIG_DATA["DECK_LINE"] = re.escape(
            config["Syntax"]["Target Deck Line"]
        )
        globals.CONFIG_DATA["TAG_LINE"] = re.escape(
            config["Syntax"]["File Tags Line"]
        )
        globals.EMPTY_REGEXP = re.compile(
            re.escape(
                config["Syntax"]["Delete Note Line"]
            ) + RegexNote.ID_REGEXP_STR
        )
        globals.CONFIG_DATA["EMPTY_REGEXP"] = re.compile(
            re.escape(
                config["Syntax"]["Delete Note Line"]
            ) + RegexNote.ID_REGEXP_STR
        )
        globals.CONFIG_DATA["FROZEN_LINE"] = re.escape(
            config["Syntax"]["Frozen Fields Line"]
        )

    def load_defaults(self, config):
        """Loads default values not to do with syntax from config object."""
        globals.NOTE_DICT_TEMPLATE["tags"] = [config["Defaults"]["Tag"]]
        globals.NOTE_DICT_TEMPLATE["deckName"] = config["Defaults"]["Deck"]
        globals.CONFIG_DATA["CurlyCloze"] = config.getboolean(
            "Defaults", "CurlyCloze"
        )
        globals.CONFIG_DATA["GUI"] = config.getboolean(
            "Defaults", "GUI"
        )
        globals.CONFIG_DATA["Regex"] = config.getboolean(
            "Defaults", "Regex"
        )
        globals.CONFIG_DATA["Comment"] = config.getboolean(
            "Defaults", "ID Comments"
        )
        globals.CONFIG_DATA["Path"] = config["Defaults"]["Anki Path"]
        globals.CONFIG_DATA["Profile"] = config["Defaults"]["Anki Profile"]
        globals.CONFIG_DATA["Vault"] = config["Obsidian"]["Vault name"]
        globals.CONFIG_DATA["Add file link"] = config.getboolean(
            "Obsidian", "Add file link"
        )

    def load_config(self):
        """Load from an existing config file (assuming it exists)."""
        print("Loading configuration file...")
        config = configparser.ConfigParser()
        config.optionxform = str  # Allows for case sensitivity
        config.read(self.CONFIG_PATH, encoding='utf-8-sig')
        self.load_syntax(config)
        self.load_defaults(config)
        globals.CONFIG_DATA["CUSTOM_REGEXPS"] = config["Custom Regexps"]
        print("Loaded successfully!")