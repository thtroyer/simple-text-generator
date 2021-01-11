import os
import chevron

from textgenrnn import textgenrnn

from simpletextgenerator.job import Job


class TrainingStatus:
    NEW = "NEW"
    NEW_LOAD_MODEL = "NEW_LOAD_MODEL"
    STARTED = "STARTED"
    FINISHED = "FINISHED"


class Train:
    # todo add model export
    # todo capture texgenrnn output (loss, etc) for logging
    # todo run until options (iterations? loss? time?)

    def __init__(self, job: Job):
        self.job = job
        self.status = job.status
        self.last_saved_model = job.latest_model_saved
        self.iterations_run = job.iterations_run
        self.textgen = textgenrnn()
        self.initial_model_to_load = job.initial_model_to_load

    @staticmethod
    def create_dir(path):
        if not os.path.exists(path):
            os.makedirs(path)

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

    def load_model(self, model_name):
        print("Loading model")
        path = f"{self.job.project_root_dir}/{self.job.job_name}/{model_name}"
        if path[-5:] != ".hdf5":
            path = f"{path}.hdf5"

        self.textgen.load(path)

    def run(self):
        print("")
        print("Loading project " + self.job.job_name)

        if self.status == TrainingStatus.FINISHED:
            print("Project already completed.")
            return

        if self.status == TrainingStatus.STARTED:
            self.load_model(self.last_saved_model)

        if self.status == TrainingStatus.NEW_LOAD_MODEL:
            self.load_model(self.initial_model_to_load)

        self.status = TrainingStatus.STARTED
        for i in range(0, self.job.num_loops):
            self.train_model()
            self.generate_text(i)
            self.save_model_iteration(i)
            self.save_model("current")
            self.iterations_run += 1
            self.update_state()

        self.generate_final_text()
        self.save_final_model()
        self.status = TrainingStatus.FINISHED
        self.update_state()

    def save_final_model(self):
        print("Saving final model")
        self.textgen.save(self.job.output_dir + "/model_" + str(self.job.num_loops) + ".hdf5")

    def generate_final_text(self):
        print("Generating final text")
        for temperature in self.job.temperatures_to_generate:
            generated = self.textgen.generate(
                n=self.job.items_to_generate_at_end, return_as_list=True, temperature=temperature
            )
            self.save_lines_to_file("last", temperature, generated)

    def save_model(self, model_name: str):
        print("Saving model current")
        model_file_name = "model_" + model_name
        self.last_saved_model = model_file_name
        self.textgen.save(
            self.job.project_root_dir + "/" + self.job.job_name
            + "/" + model_file_name + ".hdf5")

    def save_model_iteration(self, i):
        print("Saving model")
        if self.job.save_model_every_n_generations > 0:
            if (i % self.job.save_model_every_n_generations) == 0:
                self.save_model(
                    str((i + 1) * self.job.generate_every_n_generations)
                )

    def generate_text(self, i):
        print("Generating text to output file.")
        if self.job.generate_every_n_generations > 0:
            if (i % self.job.generate_every_n_generations) == 0:
                for temperature in self.job.temperatures_to_generate:
                    generated = self.textgen.generate(n=self.job.items_to_generate_each_generation,
                                                      return_as_list=True, temperature=temperature)
                    self.save_lines_to_file(i * self.job.generate_every_n_generations, temperature, generated)

    def train_model(self):
        self.textgen.train_from_file(
            self.job.training_file,
            num_epochs=1,
            train_size=self.job.training_data_percent,
            dropout=self.job.dropout
        )

    def update_state(self):
        print("Updating state")
        path = f"{self.job.project_root_dir}/{self.job.job_name}"
        with open(path + '/state.yaml', 'w') as f:
            f.write(self.render_state_file_text())

    def render_state_file_text(self):
        with open('templates/state.yml.mustache', 'r') as f:
            return (chevron.render(f, {
                'status': self.status,
                'iterations_run': self.iterations_run,
                'latest_model_saved': self.last_saved_model
            }))
