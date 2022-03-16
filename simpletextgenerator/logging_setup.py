import logging
import os
import sys


def setup_logging(logger, log_file_name, previous_log_file_name, level=logging.DEBUG):
    """Configures passed in logger and handles archiving previous log file."""
    logger.setLevel(level)
    _archive_last_log(log_file_name, previous_log_file_name)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.setLevel(level)
    stdout_handler = logging.StreamHandler(stream=sys.stdout)
    logger.addHandler(stdout_handler)
    file_handler = logging.FileHandler(filename=log_file_name, mode="w")
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def _archive_last_log(log_file_name, previous_log_file_name):
    if os.path.exists(log_file_name):
        if os.path.exists(previous_log_file_name):
            os.remove(previous_log_file_name)
        os.rename(log_file_name, previous_log_file_name)
