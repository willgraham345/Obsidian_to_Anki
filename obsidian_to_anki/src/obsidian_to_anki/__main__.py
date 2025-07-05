"""Main entry point for the obsidian_to_anki package."""

from . import main, wait_for_port, load_anki, ANKI_PORT
from .config import Config

def main_entry_point():
    print("Attempting to connect to Anki...")
    config = Config()
    try:
        wait_for_port(ANKI_PORT)
    except TimeoutError:
        print("Couldn't connect to Anki, attempting to open Anki...")
        if load_anki(config, ANKI_PORT):
            main()
    else:
        print("Connected!")
        main()

if __name__ == "__main__":
    main_entry_point()