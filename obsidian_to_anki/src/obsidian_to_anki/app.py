"""Master class that manages the application."""

import os
import re
import webbrowser
import argparse

from . import globals
from .config import Config
from .data import Data
from .directory import Directory
from .anki_connect import AnkiConnect

# Original code, I don't want to deal with the GUI. Leaving GOOEY=False as the default.
# try:
#     import gooey
#     GOOEY = True
# except ModuleNotFoundError:
#     print("Gooey not installed, switching to cli...")
#     GOOEY = False
GOOEY = False

class App:
    """Master class that manages the application."""

    SUPPORTED_EXTS = [".md", ".txt"]

    # FIXME: Won't initialize, has errors
    def __init__(self, config):
        """Execute the main functionality of the script."""
        self.config = config
        self.data = Data()
        try:
            self.config.load_config()
        except Exception as e:
            print("Error:", e)
            print("Attempting to fix config file...")
            self.config.update_config()
            self.config.load_config()
        try:
            self.data.load_data_file()
        except Exception as e:
            print("Error:", e)
            self.data.create_data_file()
            self.data.load_data_file()
        self.get_fields()
        self.get_ids()
        if globals.CONFIG_DATA["GUI"] and GOOEY:
            self.setup_gui_parser()
        else:
            self.setup_cli_parser()
        args = self.parser.parse_args()
        if globals.CONFIG_DATA["GUI"] and GOOEY:
            if args.directory:
                args.path = args.directory
            elif args.file:
                args.path = args.file
            else:
                args.path = False
        no_args = True
        if args.update:
            no_args = False
            self.config.update_config()
            self.config.load_config()
        if args.mediaupdate:
            no_args = False
            self.data.create_data_file()
        self.gen_regexp()
        if args.config:
            no_args = False
            webbrowser.open(self.config.CONFIG_PATH)
            return
        if args.path:
            no_args = False
            current = os.getcwd()
            self.path = args.path
            directories = list()
            if os.path.isdir(self.path):
                os.chdir(self.path)
                if args.recurse:
                    directories = list()
                    for root, dirs, files in os.walk(os.getcwd()):
                        directories.append(
                            Directory(root, regex=args.regex)
                        )
                        for dir in dirs:
                            if dir.startswith("."):
                                dirs.remove(dir)
                                # So, ignore . folders
                else:
                    directories = [
                        Directory(
                            os.getcwd(), regex=args.regex
                        )
                    ]
                os.chdir(current)
            else:
                # Still need to get to directory of file for image resolving
                # So, go to directory where file is (hopefully)
                # But, if just file name is given (e.g. cli), don't want to
                # Break anything.
                if os.path.dirname(self.path):
                    file_dir = os.path.dirname(self.path)
                else:
                    file_dir = current
                directories = [
                    Directory(
                        file_dir, regex=args.regex, onefile=self.path
                    )
                ]
            requests = list()
            print("Getting tag list")
            requests.append(
                AnkiConnect.request(
                    "getTags"
                )
            )
            print("Adding media with these filenames...")
            print(list(globals.MEDIA.keys()))
            requests.append(self.get_add_media())
            print("Adding directory requests...")
            for directory in directories:
                requests.append(directory.requests_1())
            result = AnkiConnect.invoke(
                "multi",
                actions=requests
            )
            tags = AnkiConnect.parse(result[0])
            directory_responses = result[2:]
            for directory, response in zip(directories, directory_responses):
                directory.parse_requests_1(AnkiConnect.parse(response), tags)
            requests = list()
            for directory in directories:
                requests.append(directory.requests_2())
            AnkiConnect.invoke(
                "multi",
                actions=requests
            )
            globals.ADDED_MEDIA = set(globals.ADDED_MEDIA)
            globals.ADDED_MEDIA.update(globals.MEDIA.keys())
            globals.ADDED_MEDIA = list(globals.ADDED_MEDIA)
            for directory in directories:
                globals.FILE_HASHES.update(directory.hashes())
            self.data.update_data_file(
                {
                    "Added Media": globals.ADDED_MEDIA,
                    "File Hashes": globals.FILE_HASHES
                }
            )
        if no_args:
            self.parser.print_help()

    def setup_parser_optionals(self):
        """Set up optional arguments for the parser."""
        self.parser.add_argument(
            "-c", "--config",
            action="store_true",
            dest="config",
            help="Open up config file for editing."
        )
        self.parser.add_argument(
            "-u", "--update",
            action="store_true",
            dest="update",
            help="Update config file."
        )
        self.parser.add_argument(
            "-r", "--regex",
            action="store_true",
            dest="regex",
            help="Use custom regex syntax.",
            default=globals.CONFIG_DATA["Regex"]
        )
        self.parser.add_argument(
            "-m", "--mediaupdate",
            action="store_true",
            dest="mediaupdate",
            help="Force addition of media files."
        )
        self.parser.add_argument(
            "-R", "--recurse",
            action="store_true",
            dest="recurse",
            help="Recursively scan subfolders."
        )

    if GOOEY:
        @ gooey.Gooey(use_cmd_args=True)
        def setup_gui_parser(self):
            """Set up the GUI argument parser."""
            self.parser = gooey.GooeyParser(
                description="Add cards to Anki from a markdown or text file."
            )
            path_group = self.parser.add_mutually_exclusive_group(
                required=False
            )
            path_group.add_argument(
                "-f", "--file",
                help="Choose a file to scan.",
                dest="file",
                widget='FileChooser'
            )
            path_group.add_argument(
                "-d", "--dir",
                help="Choose a directory to scan.",
                dest="directory",
                widget='DirChooser'
            )
            self.setup_parser_optionals()

    def setup_cli_parser(self):
        """Setup the command-line argument parser."""
        self.parser = argparse.ArgumentParser(
            description="Add cards to Anki from a markdown or text file."
        )
        self.parser.add_argument(
            "path",
            default=False,
            nargs="?",
            help="Path to the file or directory you want to scan."
        )
        self.setup_parser_optionals()

    def gen_regexp(self):
        """Generate the regular expressions used by the app."""
        globals.NOTE_REGEXP = re.compile(
            r"".join(
                [
                    r"^",
                    globals.CONFIG_DATA["NOTE_PREFIX"],
                    r"\n([\s\S]*?\n)",
                    globals.CONFIG_DATA["NOTE_SUFFIX"],
                    r"\n?"
                ]
            ), flags=re.MULTILINE
        )
        globals.DECK_REGEXP = re.compile(
            "".join(
                [
                    r"^",
                    globals.CONFIG_DATA["DECK_LINE"],
                    r"(?:\n|: )(.*)",
                ]
            ), flags=re.MULTILINE
        )
        globals.EMPTY_REGEXP = re.compile(
            "".join(
                [
                    r"^",
                    globals.CONFIG_DATA["NOTE_PREFIX"],
                    r"\n(?:<!--)?",
                    globals.ID_PREFIX,
                    r"[\s\S]*?\n",
                    globals.CONFIG_DATA["NOTE_SUFFIX"]
                ]
            ), flags=re.MULTILINE
        )
        globals.TAG_REGEXP = re.compile(
            r"^" + globals.CONFIG_DATA["TAG_LINE"] + r"(?:\n|: )(.*)",
            flags=re.MULTILINE
        )
        globals.INLINE_REGEXP = re.compile(
            "".join(
                [
                    globals.CONFIG_DATA["INLINE_PREFIX"],
                    r"(.*?)",
                    globals.CONFIG_DATA["INLINE_SUFFIX"]
                ]
            )
        )
        globals.INLINE_EMPTY_REGEXP = re.compile(
            "".join(
                [
                    globals.CONFIG_DATA["INLINE_PREFIX"],
                    r"\s+(?:<!--)?" + globals.ID_PREFIX + r".*?",
                    globals.CONFIG_DATA["INLINE_SUFFIX"]
                ]
            )
        )
        globals.VAULT_PATH_REGEXP = re.compile(
            globals.CONFIG_DATA["Vault"] + r".*"
        )
        globals.FROZEN_REGEXP = re.compile(
            globals.CONFIG_DATA["FROZEN_LINE"] + r" - (.*?):\n((?:[^\n][\n]?)+)"
        )

    def get_add_media(self):
        """Get the AnkiConnect-formatted add_media request."""
        return AnkiConnect.request(
            "multi",
            actions=[
                AnkiConnect.request(
                    "storeMediaFile",
                    filename=key,
                    data=value
                )
                for key, value in globals.MEDIA.items()
            ]
        )

    def get_fields(self):
        """Get the user's current note types and fields."""
        note_types = AnkiConnect.invoke("modelNames")
        fields_request = [
            AnkiConnect.request(
                "modelFieldNames", modelName=note
            )
            for note in note_types
        ]
        result = AnkiConnect.invoke(
            "multi", actions=fields_request
        )
        globals.FIELDS_DICT = {
            note_type: AnkiConnect.parse(fields)
            for note_type, fields in zip(
                note_types,
                result
            )
        }

    def get_ids(self):
        """Get a list of the currently used card IDs."""
        globals.EXISTING_IDS = AnkiConnect.invoke("findNotes", query="")
