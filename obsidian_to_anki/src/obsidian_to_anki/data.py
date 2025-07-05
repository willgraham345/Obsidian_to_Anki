"""Class for managing the data file (not meant to be changed by users.)"""

import json
import os

from . import globals

class Data:
    """Class for managing the data file (not meant to be changed by users.)"""

    def __init__(self):
        self.DATA_PATH = os.path.expanduser(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "..",
                "obsidian_to_anki_data.json"
            )
        )

    def create_data_file(self):
        """Creates the data file for the script."""
        print("Creating data file...")
        with open(self.DATA_PATH, "w") as f:
            json.dump(dict(), f)

    def update_data_file(self, data):
        """Updates the data file for the script with the given data."""
        print("Updating data file...")
        with open(self.DATA_PATH, "w") as f:
            json.dump(data, f)

    def load_data_file(self):
        """Loads the data file into memory"""
        with open(self.DATA_PATH, "r") as f:
            data = json.load(f)
        globals.ADDED_MEDIA = data.get("Added Media", list())
        globals.FILE_HASHES = data.get("File Hashes", dict())