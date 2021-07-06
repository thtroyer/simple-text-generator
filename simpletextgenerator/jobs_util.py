import os
import sys
import yaml
import logging

from simpletextgenerator.models import job

logger = logging.getLogger("ui")


# moved helper method out of run_training.py to make it available to the UI without pulling in
# the textgenrnn dependencies when building a pyinstaller exe
def create_job(project) -> job.Job:
    project_root_path = os.path.abspath("projects")
    project_name = os.path.basename(project)
    config_data, state_data = None, None

    if project.split("/")[-1] == "archive":
        raise RuntimeError("skip archive")
    if project.split("\\")[-1] == "archive":
        raise RuntimeError("skip archive")

    try:
        config_file = f"{project}/config.yaml"
        logger.debug(f"Attempting to open {config_file}")
        logger.info("Config file " + config_file)
        with open(config_file, 'r') as config:
            config_data = yaml.safe_load(config)
    except FileNotFoundError as e:
        logger.error(f"Missing config.yaml. Unable to build {project} job.")
        raise e

    try:
        with open(f"{project}/state.yaml", 'r') as state:
            state_data = yaml.safe_load(state)
    except FileNotFoundError as e:
        logger.error(f"Missing state.yaml. Unable to build {project} job.")
        raise e

    return job.Job(config_data, state_data, project_root_path, project_name, "_", "_")


def resource_path(relative_path):
    try:
        # for pyinstaller
        base_path = sys._MEIPASS
    except Exception as e:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
