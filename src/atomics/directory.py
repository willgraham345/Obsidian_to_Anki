"""Class for managing a directory of files at a time."""

import os
import re
import logging

from . import globals
from .file import File
from .anki_connect import AnkiConnect, Action


def _natural_sort_key(file):
    return [int(p) if p.isdigit() else p.lower() for p in re.split(r'(\d+)', file.filename)]


class Directory:
    """Class for managing a directory of files at a time.

    This class handles scanning a directory for supported files, processing them,
    and generating AnkiConnect requests for adding, updating, and deleting notes.
    """

    def __init__(self, abspath: str, onefile: str = None):
        """Initializes a Directory object and scans for relevant files.

        It identifies files based on supported extensions, handles single file processing,
        and skips files that haven't changed since the last scan.

        :param abspath: The absolute path to the directory to scan.
        :type abspath: str
        :param onefile: Optional. If provided, only this single file will be processed.
        :type onefile: str, optional
        """
        self.path = abspath
        self.parent = os.getcwd()
        os.chdir(self.path)
        if onefile:
            # Hence, just one file to do
            self.files = [File(onefile)]
        else:
            with os.scandir() as it:
                self.files = sorted(
                    [File(entry.path) for entry in it if entry.is_file()],
                    key=_natural_sort_key
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
                Action.MULTI,
                actions=[file.get_add_notes() for file in self.files]
            )
        )
        logging.info("Getting card IDs of notes to be edited...")
        requests.append(
            AnkiConnect.request(
                Action.MULTI,
                actions=[file.get_note_info() for file in self.files]
            )
        )
        logging.info("Updating fields and tags of existing notes...")
        requests.append(
            AnkiConnect.request(
                Action.MULTI,
                actions=[file.get_update_notes() for file in self.files]
            )
        )
        logging.info("Removing empty notes...")
        requests.append(
            AnkiConnect.request(
                Action.MULTI,
                actions=[file.get_delete_notes() for file in self.files]
            )
        )
        return AnkiConnect.request(
            Action.MULTI,
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
        os.chdir(self.parent)

    def requests_2(self) -> dict:
        """Generates the second set of AnkiConnect requests for the files in this directory.

        Tags are now handled atomically in stage 1 via updateNote; this stage
        only moves cards to their target deck.

        :returns: A dictionary representing the AnkiConnect 'multi' action request containing all second-stage requests.
        :rtype: dict
        """
        logging.info("Forming request 2 for directory " + self.path)
        logging.info("Moving cards to target deck...")
        return AnkiConnect.request(
            Action.MULTI,
            actions=[file.get_change_decks() for file in self.files]
        )

    def hashes(self) -> dict:
        """Returns a dictionary of filenames to their corresponding file hashes.

        :returns: A dictionary where keys are filenames and values are their SHA256 hashes.
        :rtype: dict
        """
        return {file.filename: file.hash for file in self.files}
