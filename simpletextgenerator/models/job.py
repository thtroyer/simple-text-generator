import logging

from simpletextgenerator.models import config, state

logger = logging.getLogger("ui")


class Job:
    def __init__(self, config_data, state_data, project_root_dir, job_name, input_folder, output_folder):
        self.config = config.create_config(config_data, project_root_dir, job_name, input_folder, output_folder)
        self.state = state.create_state(state_data)
