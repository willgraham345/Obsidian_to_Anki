"""Class for managing a directory of files at a time."""

import os
import re
import logging

from . import globals
from .file import File, RegexFile
from .anki_connect import AnkiConnect
from .app import App

class Directory:
    """Class for managing a directory of files at a time.

    This class handles scanning a directory for supported files, processing them,
    and generating AnkiConnect requests for adding, updating, and deleting notes.
    """

    def __init__(self, abspath: str, regex: bool = False, onefile: str = None):
        """Initializes a Directory object and scans for relevant files.

        It identifies files based on supported extensions, handles single file processing,
        and skips files that haven't changed since the last scan.

        :param abspath: The absolute path to the directory to scan.
        :type abspath: str
        :param regex: A boolean indicating whether to use RegexFile for processing.
        :type regex: bool
        :param onefile: Optional. If provided, only this single file will be processed.
        :type onefile: str, optional
        """
        self.path = abspath
        self.parent = os.getcwd()
        if regex:
            self.file_class = RegexFile
        else:
            self.file_class = File
        os.chdir(self.path)
        if onefile:
            # Hence, just one file to do
            self.files = [self.file_class(onefile)]
        else:
            with os.scandir() as it:
                self.files = sorted(
                    [
                        self.file_class(entry.path)
                        for entry in it
                        if entry.is_file() and os.path.splitext(
                            entry.path
                        )[1] in globals.SUPPORTED_EXTS
                    ], key=lambda file: [
                        int(part) if part.isdigit() else part.lower()
                        for part in re.split(r'(\d+)', file.filename)]
                )
        files_changed = []
        for file in self.files:
            if file.filename in globals.FILE_HASHES and (
                file.hash == globals.FILE_HASHES[file.filename]
            ):
                # Indicates we've seen this in a scan before,
                # And that it hasn't changed.
                # So, we don't need to do anything with it!
                print("Skipping", file.filename, "as we've scanned it before.")
            else:
                file.scan_file()
                files_changed.append(file)
        self.files = files_changed
        os.chdir(self.parent)

    def requests_1(self) -> dict:
        """Generates the first set of AnkiConnect requests for the files in this directory.

        This includes requests for adding new notes, getting information about notes to be edited,
        updating existing notes, and deleting notes.

        :returns: A dictionary representing the AnkiConnect 'multi' action request containing all first-stage requests.
        :rtype: dict
        """
        logging.info("Forming request 1 for directory" + self.path)
        requests = list()
        logging.info("Adding notes into Anki...")
        requests.append(
            AnkiConnect.request(
                "multi",
                actions=[
                    file.get_add_notes()
                    for file in self.files
                ]
            )
        )
        logging.info("Getting card IDs of notes to be edited...")
        requests.append(
            AnkiConnect.request(
                "multi",
                actions=[
                    file.get_note_info()
                    for file in self.files
                ]
            )
        )
        logging.info("Updating fields of existing notes...")
        requests.append(
            AnkiConnect.request(
                "multi",
                actions=[
                    file.get_update_fields()
                    for file in self.files
                ]
            )
        )
        logging.info("Removing empty notes...")
        requests.append(
            AnkiConnect.request(
                "multi",
                actions=[
                    file.get_delete_notes()
                    for file in self.files
                ]
            )
        )
        return AnkiConnect.request(
            "multi",
            actions=requests
        )

    def parse_requests_1(self, requests_1_response: list, tags: list):
        """Parses the responses from the first set of AnkiConnect requests.

        This method updates file objects with note and card IDs and triggers
        further processing like writing IDs back to files and removing empty notes.

        :param requests_1_response: The raw response from the first 'multi' AnkiConnect request.
        :type requests_1_response: list
        :param tags: A list of tags to be applied to the notes.
        :type tags: list
        """
        response = requests_1_response
        notes_ids = AnkiConnect.parse(response[0])
        cards_ids = AnkiConnect.parse(response[1])
        for note_ids, file in zip(notes_ids, self.files):
            file.note_ids = [
                AnkiConnect.parse(response)
                for response in AnkiConnect.parse(note_ids)
            ]
        for card_ids, file in zip(cards_ids, self.files):
            file.card_ids = AnkiConnect.parse(card_ids)
        for file in self.files:
            file.tags = tags
        os.chdir(self.path)
        for file in self.files:
            file.get_cards()
            file.write_ids()
            logging.info("Removing empty notes for file " + file.filename)
            file.remove_empties()
            file.write_file()
        os.chdir(self.parent)

    def requests_2(self) -> dict:
        """Generates the second set of AnkiConnect requests for the files in this directory.

        This includes requests for changing note decks and managing tags.

        :returns: A dictionary representing the AnkiConnect 'multi' action request containing all second-stage requests.
        :rtype: dict
        """
        logging.info("Forming request 2 for directory " + self.path)
        requests = list()
        logging.info("Moving cards to target deck...")
        requests.append(
            AnkiConnect.request(
                "multi",
                actions=[
                    file.get_change_decks()
                    for file in self.files
                ]
            )
        )
        logging.info("Replacing tags...")
        requests.append(
            AnkiConnect.request(
                "multi",
                actions=[
                    file.get_clear_tags()
                    for file in self.files
                ]
            )
        )
        requests.append(
            AnkiConnect.request(
                "multi",
                actions=[
                    file.get_add_tags()
                    for file in self.files
                ]
            )
        )
        return AnkiConnect.request(
            "multi",
            actions=requests
        )

    def hashes(self) -> dict:
        """Returns a dictionary of filenames to their corresponding file hashes.

        :returns: A dictionary where keys are filenames and values are their SHA256 hashes.
        :rtype: dict
        """
        return {file.filename: file.hash for file in self.files}
