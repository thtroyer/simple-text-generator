import logging
import sys
import os

from pathlib import Path
from simpletextgenerator.ui.menu import draw_main_menu

logging.basicConfig(filename='simple-text-generator-ui.log', filemode='w')
logger = logging.getLogger("ui")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)


def create_dir_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


if __name__ == "__main__":
    create_dir_if_not_exists("projects")
    create_dir_if_not_exists("projects/archive")
    try:
        window_manager = draw_main_menu()
        window_manager.draw_main_window()
    except Exception as e:
        logger.error(e)
        raise e
