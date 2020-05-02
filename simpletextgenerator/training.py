import os

from textgenrnn import textgenrnn


class Train:
    # todo add model export
    # todo capture texgenrnn output (loss, etc) for logging
    # todo run until options (iterations? loss? time?)
    def __init__(self, job):
        self.job = job
        self.textgen = textgenrnn()

    def save_lines_to_file(self, iteration, temperature, data):
        self.create_dir(self.job.output_dir)
        file_handle = open(self.job.output_file, "a", encoding='utf-8')
        file_handle.write("Iteration: " + str(iteration) + "\n")
        file_handle.write("Temperature : " + str(temperature) + "\n")
        for item in data:
            string_to_write = item
            if isinstance(item, (bytes, bytearray)):
                string_to_write = item.decode(encoding='utf-8', errors='ignore')
            file_handle.write(string_to_write)
            file_handle.write("\n")
        file_handle.write("\n")
        file_handle.write("____________________________\n")
        file_handle.close()

    def create_dir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def run(self):
        for i in range(0, self.job.num_loops):
            self.textgen.train_from_file(
                self.job.training_file,
                num_epochs=1,
                train_size=self.job.training_data_percent,
                dropout=self.job.dropout
            )

            if self.job.generate_every_n_generations > 0:
                if (i % self.job.generate_every_n_generations) == 0:
                    for temperature in self.job.temperatures_to_generate:
                        generated = self.textgen.generate(n=self.job.items_to_generate_each_generation,
                                                          return_as_list=True, temperature=temperature)
                        self.save_lines_to_file(i * self.job.generate_every_n_generations, temperature, generated)

            if self.job.save_model_every_n_generations > 0:
                if (i % self.job.save_model_every_n_generations) == 0:
                    self.textgen.save(
                        self.job.project_root_dir + "/" + self.job.output_folder + "/" + self.job.job_name + "/model_" +
                        str((i + 1) * self.job.generate_every_n_generations) + ".hdf5"
                    )

        for temperature in self.job.temperatures_to_generate:
            generated = self.textgen.generate(n=self.job.items_to_generate_at_end, return_as_list=True,
                                              temperature=temperature)
            self.save_lines_to_file("last", temperature, generated)

        self.textgen.save(self.job.output_dir + "/model_" + str(self.job.num_loops) + ".hdf5")


