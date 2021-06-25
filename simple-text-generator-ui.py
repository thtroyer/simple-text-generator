import logging
import sys

from simpletextgenerator.ui.menu import draw_main_menu

logging.basicConfig(filename='simple-text-generator-ui.log', filemode='w')
logger = logging.getLogger("ui")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)

if __name__ == "__main__":
    try:
        window_manager = draw_main_menu()
        window_manager.draw_main_window()
    except Exception as e:
        logger.error(e)
        raise e
