"""Script for adding cards to Anki from Obsidian."""

# import os
import logging
#
# from .app import App
# from .config import Config
# from .utils import wait_for_port, load_anki
# from .globals import ANKI_PORT

logging.basicConfig(
    filename='atomics.log',
    level=logging.DEBUG,
    format='%(asctime)s:::%(levelname)s:::%(funcName)s:::%(message)s'
)

# def main():
#     """Main functionality of script."""
#     config = Config()
#     if not os.path.exists(config.CONFIG_PATH):
#         config.update_config()
#     App(config)
