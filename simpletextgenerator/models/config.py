import logging
from dataclasses import dataclass
from typing import IO

import chevron

logger = logging.getLogger("ui")


@dataclass
class Config:
    # todo: Figure out what to do with derived values used by training
    training_file: str
    output_file: str  # derived
    output_dir: str  # derived
    num_loops: str
    priority: str
    temperatures_to_generate: list
    project_root_dir: str
    job_name: str
    input_folder: str
    output_folder: str
    items_to_generate_each_generation: str
    items_to_generate_at_end: str
    generate_every_n_generations: str
    save_model_every_n_generations: str
    dropout: str
    training_data_percent: str
    initial_model_to_load: str

    def render(self, mustache_file: IO) -> str:
        return (chevron.render(mustache_file, {
            'priority': 0,
            'training_file': self.training_file,
            'number_of_iterations': self.num_loops,
            'dropout': self.dropout,
            'training_data_percent': self.training_data_percent,
            'temperatures': self.temperatures_to_generate,
            'items_to_generate_between_iterations': self.items_to_generate_each_generation,
            'generate_every_n_generations': self.generate_every_n_generations,
            'save_model_every_n_generations': self.save_model_every_n_generations,
            'items_to_generate_at_end': self.items_to_generate_at_end,
            'model_to_load': f"m_{self.initial_model_to_load}"
        }))


def create_config(config_data, project_root_dir, job_name, input_folder, output_folder) -> Config:
    """Factory method to help create a Config object, used by training code """
    training_file = project_root_dir + '/' + job_name + '/' + config_data['file']['training_file']
    output_file = project_root_dir + "/" + job_name + "/output.txt"
    output_dir = project_root_dir + "/"
    num_loops = config_data['training']['num_loops']
    priority = config_data['priority']
    temperatures_to_generate = config_data['output']['temperatures_to_generate']
    project_root_dir = project_root_dir
    job_name = job_name
    input_folder = input_folder
    output_folder = output_folder
    items_to_generate_each_generation = config_data['output']['items_to_generate_between_generations']
    items_to_generate_at_end = config_data['output']['items_to_generate_at_end']
    generate_every_n_generations = config_data['output']['generate_every_n_generations']
    save_model_every_n_generations = config_data['output']['save_model_every_n_generations']
    dropout = config_data['training']['dropout']
    training_data_percent = config_data['training']['training_data_percent']
    initial_model_to_load = config_data['file']['initial_model_to_load']

    return Config(training_file, output_file, output_dir, num_loops, priority, temperatures_to_generate,
                  project_root_dir, job_name, input_folder, output_folder, items_to_generate_each_generation,
                  items_to_generate_at_end, generate_every_n_generations, save_model_every_n_generations, dropout,
                  training_data_percent, initial_model_to_load)
