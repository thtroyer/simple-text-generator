import os

from textgenrnn import textgenrnn
from simpletextgenerator.models.job import Job


class TrainingStatus:
    NEW = "NEW"
    NEW_LOAD_MODEL = "NEW_LOAD_MODEL"
    STARTED = "STARTED"
    FINISHED = "FINISHED"


class Train:
    # todo capture texgenrnn output (loss, etc) for logging
    # todo run until options (iterations? loss? time?)

    def __init__(self, job: Job):
        self.job = job
        self.status = job.state.status
        self.last_saved_model = job.state.latest_model_saved
        self.iterations_run = job.state.iterations_run
        self.textgen = textgenrnn()
        self.initial_model_to_load = job.config.initial_model_to_load
        self.state = job.state

    @staticmethod
    def create_dir(path):
        if not os.path.exists(path):
            os.makedirs(path)

    def save_lines_to_file(self, iteration, temperature, data):
        self.create_dir(self.job.config.output_dir)
        file_handle = open(self.job.config.output_file, "a", encoding='utf-8')
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
        path = f"{self.job.config.project_root_dir}/{self.job.config.job_name}/{model_name}"
        if path[-5:] != ".hdf5":
            path = f"{path}.hdf5"

        self.textgen.load(path)

    def run(self):
        print("")
        print("Loading project " + self.job.config.job_name)

        if self.state.status == TrainingStatus.FINISHED:
            print("Project already completed.")
            return

        if self.state.status == TrainingStatus.STARTED:
            self.load_model(self.state.latest_model_saved)

        if self.state.status == TrainingStatus.NEW_LOAD_MODEL:
            self.load_model(self.initial_model_to_load)

        self.state.status = TrainingStatus.STARTED
        for i in range(0, self.job.config.num_loops):
            self.train_model()
            self.generate_text(i)
            self.save_model_iteration(i)
            self.save_model("current")
            self.state.iterations_run += 1
            self.write_state_file()

        self.generate_final_text()
        self.save_final_model()
        self.state.status = TrainingStatus.FINISHED
        self.write_state_file()

    def save_final_model(self):
        print("Saving final model")
        self.textgen.save(self.job.config.output_dir + "/model_" + str(self.state.iterations_run) + ".hdf5")

    def generate_final_text(self):
        print("Generating final text")
        for temperature in self.job.config.temperatures_to_generate:
            generated = self.textgen.generate(n=self.job.config.items_to_generate_at_end, return_as_list=True,
                                              temperature=temperature)
            self.save_lines_to_file("last", temperature, generated)

    def save_model(self, model_name: str) -> None:
        print("Saving model current")
        model_file_name = "model_" + model_name
        self.state.latest_model_saved = model_file_name
        self.textgen.save(
            self.job.config.project_root_dir + "/" + self.job.config.job_name + "/" + model_file_name + ".hdf5")

    def save_model_iteration(self, i) -> None:
        print("Saving model")
        if self.job.config.save_model_every_n_generations > 0:
            if (i % self.job.config.save_model_every_n_generations) == 0:
                self.save_model(
                    str((i + 1) * self.job.config.generate_every_n_generations)
                )

    def generate_text(self, i) -> None:
        print("Generating text to output file.")
        if self.job.config.generate_every_n_generations > 0:
            if (i % self.job.config.generate_every_n_generations) == 0:
                for temperature in self.job.config.temperatures_to_generate:
                    try:
                        generated = self.textgen.generate(n=self.job.config.items_to_generate_each_generation,
                                                          return_as_list=True, temperature=temperature)
                    except KeyError:
                        continue
                    self.save_lines_to_file(i * self.job.config.generate_every_n_generations, temperature, generated)

    def train_model(self) -> None:
        self.textgen.train_from_file(
            self.job.config.training_file,
            num_epochs=1,
            train_size=self.job.config.training_data_percent,
            dropout=self.job.config.dropout
        )

    def write_state_file(self) -> None:
        print("Updating state")
        path = f"{self.job.config.project_root_dir}/{self.job.config.job_name}"
        with open(path + '/state.yaml', 'w') as f:
            f.write(self.render_state_file_text())

    def render_state_file_text(self) -> str:
        with open('templates/state.yml.mustache', 'r') as f:
            return self.state.render(f)
