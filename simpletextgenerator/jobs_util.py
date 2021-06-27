import os
import sys

import yaml

from simpletextgenerator.models import job

import logging
logger = logging.getLogger("ui")

# moved helper method out of run_training.py to make it available to the UI without pulling in
# the textgenrnn dependencies when building a pyinstaller exe

def create_job(project, project_dir="./projects") -> job.Job:
    project_root_path = os.path.abspath(project_dir)
    project_name = os.path.basename(project)
    config_data, state_data = None, None

    if project.split("/")[-1] == "archive":
        raise RuntimeError("skip archive")
    if project.split("\\")[-1] == "archive":
        raise RuntimeError("skip archive")

    try:
        with open(f"{project_dir}/{project}/config.yaml", 'r') as config:
            config_data = yaml.safe_load(config)
    except FileNotFoundError as e:
        print(f"Missing config.yaml. Unable to build {project} job.")
        raise e

    try:
        with open(f"{project_dir}/{project}/state.yaml", 'r') as state:
            state_data = yaml.safe_load(state)
    except FileNotFoundError as e:
        print(f"Missing state.yaml. Unable to build {project} job.")
        raise e

    return job.Job(config_data, state_data, project_root_path, project_name, "_", "_")


def resource_path(relative_path):
    try:
        # for pyinstaller
        base_path = sys._MEIPASS
    except Exception as e:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
