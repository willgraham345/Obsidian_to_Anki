"""Helper functions for obsidian_to_anki."""

import re
import os
import base64
import time
import socket
import subprocess

from . import globals

def has_clozes(text):
    """Checks whether text actually has cloze deletions."""
    return bool(globals.ANKI_CLOZE_REGEXP.search(text))


def note_has_clozes(note):
    """Checks whether a note has cloze deletions in any of its fields."""
    return any(has_clozes(field) for field in note["fields"].values())


def write_safe(filename, contents):
    """
    Write contents to filename while keeping a backup.

    If write fails, a backup 'filename.bak' will still exist.
    """
    with open(filename + ".tmp", "w", encoding='utf_8') as temp:
        temp.write(contents)
    os.rename(filename, filename + ".bak")
    os.rename(filename + ".tmp", filename)
    with open(filename, encoding='utf_8') as f:
        success = (f.read() == contents)
    if success:
        os.remove(filename + ".bak")


def string_insert(string, position_inserts):
    """
    Insert strings in position_inserts into string, at indices.

    position_inserts will look like:
    [(0, "hi"), (3, "hello"), (5, "beep")]
    """
    offset = 0
    position_inserts = sorted(list(position_inserts))
    for position, insert_str in position_inserts:
        string = "".join(
            [
                string[:position + offset],
                insert_str,
                string[position + offset:]
            ]
        )
        offset += len(insert_str)
    return string


def file_encode(filepath):
    """Encode the file as base 64."""
    with open(filepath, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')


def spans(pattern, string):
    """Return a list of span-tuples for matches of pattern in string."""
    return [match.span() for match in pattern.finditer(string)]


def contained_in(span, spans):
    """Return whether span is contained in spans (+- 1 leeway)"""
    return any(
        span[0] >= start - 1 and span[1] <= end + 1
        for start, end in spans
    )


def findignore(pattern, string, ignore_spans):
    """Yield all matches for pattern in string not in ignore_spans."""
    return (
        match
        for match in pattern.finditer(string)
        if not contained_in(match.span(), ignore_spans)
    )


def wait_for_port(port, host='localhost', timeout=5.0):
    """Wait until a port starts accepting TCP connections.
    Args:
        port (int): Port number.
        host (str): Host address on which the port should exist.
        timeout (float): In seconds. How long to wait before raising errors.
    Raises:
        TimeoutError: The port isn't accepting connection after time specified
        in `timeout`.
    """
    start_time = time.perf_counter()
    while True:
        try:
            with socket.create_connection((host, port), timeout=timeout):
                break
        except OSError as ex:
            time.sleep(0.01)
            if time.perf_counter() - start_time >= timeout:
                raise TimeoutError(
                    'Waited too long for the port {} on host {} to'
                    'start accepting connections.'.format(port, host)
                ) from ex


def load_anki(config, anki_port):
    """Attempt to load anki in the correct profile."""
    try:
        config.load_config()
    except Exception as e:
        print("Error when loading config:", e)
        print("Please open Anki before running script again.")
        return False
    if globals.CONFIG_DATA["Path"] and globals.CONFIG_DATA["Profile"]:
        print("Anki Path and Anki Profile provided.")
        print("Attempting to open Anki in selected profile...")
        subprocess.Popen(
            [globals.CONFIG_DATA["Path"], "-p", globals.CONFIG_DATA["Profile"]]
        )
        try:
            wait_for_port(anki_port)
        except TimeoutError:
            print(
                "Opened Anki, but can't connect! Is AnkiConnect working?"
            )
            return False
        else:
            print("Opened and connected to Anki successfully!")
            return True
    else:
        print(
            "Must provide both Anki Path and Anki Profile",
            "in order to open Anki automatically"
        )
        return False
