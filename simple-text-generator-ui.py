import hashlib
import logging
import os
import pathlib
import subprocess
import sys

from simpletextgenerator.logging_setup import setup_logging
from simpletextgenerator.ui.menu import draw_main_menu

version = "0.3.0"
logger = logging.getLogger("ui")


def get_git_revision_hash():
    return subprocess.check_output(['git', 'rev-parse', 'HEAD'])


def get_exe_hashes() -> str:
    try:
        hash1 = get_simple_text_generator_ui_exe_hash()
        hash2 = get_run_training_exe_hash()
    except Exception as e:
        logger.debug(e)
        return ""

    return f"simple-text-generator md5sum: {hash1}; run_training.exe: {hash2}"


def get_simple_text_generator_ui_exe_hash() -> str:
    return hashlib.md5(open('simple-text-generator-ui.exe', 'rb').read()).hexdigest()


def get_run_training_exe_hash() -> str:
    return hashlib.md5(open('run_training.exe', 'rb').read()).hexdigest()


def get_git_hash_or_empty() -> str:
    try:
        return f"git hash: {get_git_revision_hash()}"
    except Exception as e:
        logger.debug(e)
        return ""


def create_dir_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def log_environment():
    logger.info(sys.version)
    logger.info(f"Platform: {sys.platform}")
    logger.info(f"simple-text-generator code version: {version}")
    commit = get_git_hash_or_empty()
    if commit != "":
        logger.info(f"commit: {commit}")
    hashes = get_exe_hashes()
    if hashes != "":
        logger.info(f"{hashes}")


if __name__ == "__main__":
    pathlib.Path('logs').mkdir(exist_ok=True)
    log_file_name = "logs/simple-text-generator-ui.log"
    previous_log_file_name = "logs/simple-text-generator-ui_previous.log"
    setup_logging(logger, log_file_name, previous_log_file_name)
    log_environment()
    create_dir_if_not_exists("projects")
    create_dir_if_not_exists("projects/archive")
    try:
        window_manager = draw_main_menu()
    except Exception as e:
        logger.error(e)
        raise e
