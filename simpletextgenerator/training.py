import os

from textgenrnn import textgenrnn


class Train:
    #todo add model export
    #todo capture texgenrnn output (loss, etc) for logging
    #todo run until options (iterations? loss? time?)
    def __init__(self, job):
        self.job = job
        self.textgen = textgenrnn()

    def save_lines_to_file(self, iteration, temperature, data):
        self.create_dir(self.job.output_dir)
        file_handle = open(self.job.output_file, "a")
        file_handle.write("Iteration: " + str(iteration) + "\n")
        file_handle.write("Temperature : " + str(temperature) + "\n")
        for item in data:
            file_handle.write(item)
            file_handle.write("\n")
        file_handle.write("\n")
        file_handle.write("____________________________\n")
        file_handle.close()

    def create_dir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def run(self):
        for i in range(0, self.job.num_loops // self.job.generate_every_n_generations):
            self.textgen.train_from_file(
                self.job.training_file,
                num_epochs=self.job.generate_every_n_generations,
                train_size=self.job.training_data_percent,
                dropout=self.job.dropout
            )

            for temp in self.job.temperatures_to_generate:
                generated = self.textgen.generate(n=self.job.items_to_generate_each_generation, return_as_list=True, temperature=temp)
                self.save_lines_to_file(i * self.job.generate_every_n_generations, temp, generated)

        generated = self.textgen.generate(n=self.job.items_to_generate_at_end, return_as_list=True, temperature=temp)
        self.save_lines_to_file(i * self.job.generate_every_n_generations, temp, generated)


class Job:
    def __init__(self, config_data, project_root_dir, job_name, input_folder, output_folder):
        self.training_file = project_root_dir + '/' + output_folder + '/' + job_name + '/' + config_data['file']['training_file']
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
        self.dropout = config_data['training']['dropout']
        self.training_data_percent = config_data['training']['training_data_percent']

