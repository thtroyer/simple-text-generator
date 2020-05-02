
class Job:
    def __init__(self, config_data, project_root_dir, job_name, input_folder, output_folder):
        self.training_file = project_root_dir + '/' + output_folder + '/' + job_name + '/' \
                             + config_data['file']['training_file']
        self.output_file = project_root_dir + "/" + output_folder + '/' + job_name + '/' + "/output.txt"
        self.output_dir = project_root_dir + "/" + output_folder
        self.num_loops = config_data['training']['num_loops']
        self.priority = config_data['priority']
        self.temperatures_to_generate = config_data['output']['temperatures_to_generate']
        self.project_root_dir = project_root_dir
        self.job_name = job_name
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.items_to_generate_each_generation = config_data['output']['items_to_generate_between_generations']
        self.items_to_generate_at_end = config_data['output']['items_to_generate_at_end']
        self.generate_every_n_generations = config_data['output']['generate_every_n_generations']
        self.save_model_every_n_generations = config_data['output']['save_model_every_n_generations']
        self.dropout = config_data['training']['dropout']
        self.training_data_percent = config_data['training']['training_data_percent']