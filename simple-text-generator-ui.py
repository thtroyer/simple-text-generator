import hashlib
import logging
import subprocess
import sys
import os

from simpletextgenerator.ui.menu import draw_main_menu

log_file_name = "simple-text-generator-ui.log"
previous_log_file_name = "simple-text-generator-ui_previous.log"
version = "0.2_unreleased"
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


def archive_last_log():
    if os.path.exists(log_file_name):
        if os.path.exists(previous_log_file_name):
            os.remove(previous_log_file_name)
        os.rename(log_file_name, previous_log_file_name)


def setup_logging():
    global logger
    logger.setLevel(logging.DEBUG)
    archive_last_log()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # logging.basicConfig(filename=log_file_name, filemode='w', formatter=formatter)
    logger = logging.getLogger("ui")
    logger.setLevel(logging.DEBUG)
    stdout_handler = logging.StreamHandler(stream=sys.stdout)
    logger.addHandler(stdout_handler)
    file_handler = logging.FileHandler(filename=log_file_name, mode="w")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


def log_environment():
    logger.info(sys.version)
    logger.info(f"Platform: {sys.platform}")
    logger.info(f"simple-text-generator code version: {version}")
    commit = get_git_hash_or_empty()
    if commit is not "":
        logger.info(f"commit: {commit}")
    hashes = get_exe_hashes()
    if hashes is not "":
        logger.info(f"{hashes}")


if __name__ == "__main__":
    setup_logging()
    log_environment()
    create_dir_if_not_exists("projects")
    create_dir_if_not_exists("projects/archive")
    try:
        window_manager = draw_main_menu()
        window_manager.draw_main_window()
    except Exception as e:
        logger.error(e)
        raise e
