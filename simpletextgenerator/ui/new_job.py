import logging
import os
import tkinter as tk
from os.path import splitext
from pathlib import Path
from shutil import copyfile
from tkinter import filedialog
from tkinter import messagebox

import chevron

from simpletextgenerator.jobs_util import resource_path
from simpletextgenerator.models.config import Config
from simpletextgenerator.training_status import TrainingStatus

logger = logging.getLogger("ui")


def draw_new_job_window():
    new_job_window = NewJobWindow()
    new_job_window.mainloop()


def draw_new_job_load_model_window():
    new_job_window = NewJobWindowLoad()
    new_job_window.mainloop()


def draw_new_batch_job_window():
    new_batch_job_window = NewJobWindowBatch()
    new_batch_job_window.mainloop()


class AbstractNewJobWindow(tk.Tk):
    """Parent class for the 3 related UIs in this file."""

    def __init__(self):
        super().__init__()
        self.button_open_model_file = None
        self.button_open_training_file = None
        self.new_batch_job_window = None
        self.training_data_percent = None
        self.dropout = None
        self.save_frequency = None
        self.generation_frequency = None
        self.items_to_generate_at_end = None
        self.items_to_generate_between_generations = None
        self.temperatures_to_generate = None
        self.number_of_iterations = None
        self.project_name = None
        self.new_job_window = None
        self.new_job_load_model_window = None
        self.model_to_load = None

    def back_new_job_window(self):
        self.new_job_window.destroy()

    def back_new_job_load_model_window(self):
        self.new_job_load_model_window.destroy()

    def save_new_job_window(self):
        try:
            project_path = "projects/" + self.project_name.get()
            self.create_new_project_dir(project_path)
            self.create_config_file(project_path)
            self.create_state_file(project_path)
            self.copy_training_file(project_path)
            self.new_job_window.destroy()
        except Exception as e:
            # todo remove
            logger.error(e)
            raise e

    @staticmethod
    def create_new_project_dir(path):
        if os.path.exists(path):
            messagebox.showerror(title="Error", message="Project already exists.")
            raise Exception("Project already exists. Dir: " + path)

        logger.info("Creating dir: " + path)
        os.makedirs(path)

    def create_config_file(self, path):
        with open(path + '/config.yaml', 'w') as f:
            f.write(self.render_config_file_text())

    def render_config_file_text(self):
        with open(resource_path('templates/config.yml.mustache'), 'r') as f:
            config = Config(
                training_file=self.training_file,
                output_file="",
                output_dir="",
                num_loops=self.number_of_iterations.get(),
                priority="0",
                temperatures_to_generate=list(map(str.strip, self.temperatures_to_generate.get().split(','))),
                project_root_dir="",
                job_name="",
                input_folder="",
                output_folder="",
                items_to_generate_each_generation=self.items_to_generate_between_generations.get(),
                items_to_generate_at_end=self.items_to_generate_at_end.get(),
                generate_every_n_generations=self.generation_frequency.get(),
                save_model_every_n_generations=self.save_frequency.get(),
                dropout=self.dropout.get(),
                training_data_percent=self.training_data_percent.get(),
                initial_model_to_load=self.model_to_load
            )
            return config.render(f)

    def create_state_file(self, path):
        with open(path + '/state.yaml', 'w') as f:
            f.write(self.render_state_file_text())

    def copy_training_file(self, project_path):
        copyfile(self.training_file_origin_path, f"./{project_path}/{self.training_file}")

    def render_state_file_text(self):
        status = TrainingStatus.NEW
        if self.model_to_load is not None:
            status = TrainingStatus.NEW_LOAD_MODEL

        with open(resource_path('templates/state.yml.mustache'), 'r') as f:
            return (chevron.render(f, {
                'status': status,
                'iterations_run': 0,
                'latest_model_saved': ''
            }))

    def set_training_file(self):
        self.training_file_origin_path = self.open_file_dialog("txt")
        if self.new_job_load_model_window is not None:
            self.new_job_load_model_window.lift()
        if self.new_job_window is not None:
            self.new_job_window.lift()
        if self.new_batch_job_window is not None:
            self.new_batch_job_window.lift()
        self.training_file = Path(self.training_file_origin_path).name
        self.button_open_training_file['text'] = self.training_file

    @staticmethod
    def open_file_dialog(default_ext: str):
        home = os.path.expanduser('~')
        return filedialog.askopenfilename(
            initialdir=home,
            title="Select file",
            filetypes=(("file_type", f"*.{default_ext}"), ("all files", "*.*"))
        )

    def save_new_job_load_model_window(self):
        try:
            project_path = "projects/" + self.project_name.get()
            self.create_new_project_dir(project_path)
            self.create_config_file(project_path)
            self.create_state_file(project_path)
            self.copy_training_file(project_path)
            self.copy_model_file(project_path)
            self.new_job_load_model_window.destroy()
        except Exception as e:
            # todo remove
            logger.error(e)
            raise e

    def copy_model_file(self, project_path):
        copyfile(self.model_to_load_origin_path, f"{project_path}/m_{self.model_to_load}")

    def set_model_file(self):
        self.model_to_load_origin_path = self.open_file_dialog("hdf5")
        self.new_job_load_model_window.lift()
        self.model_to_load = Path(self.model_to_load_origin_path).name
        self.button_open_model_file['text'] = self.model_to_load

    def save_new_batch_job_window(self):
        try:
            for training_file in self.batch_training_files:
                self.training_file_origin_path = training_file
                file_name = os.path.basename(training_file)
                self.training_file = file_name
                project_name = splitext(file_name)[0]
                project_path = "projects/" + project_name
                self.create_new_project_dir(project_path)
                self.create_config_file(project_path)
                self.training_file = file_name
                self.create_state_file(project_path)
                self.copy_training_file(project_path)
            self.new_job_window.destroy()
        except Exception as e:
            # todo remove
            logger.error(e)
            raise e

    def set_training_file_batch(self):
        self.batch_training_files = tk.filedialog.askopenfilenames(title='Choose a file')
        self.new_job_window.lift()


class NewJobWindow(AbstractNewJobWindow):
    """UI for completely new jobs."""

    def __init__(self):
        super().__init__()

        self.title("Create New Job - simple-text-generator")
        main_frame = tk.Frame(self)
        main_frame.grid()
        top_frame = tk.Frame(main_frame)
        bottom_frame = tk.Frame(main_frame)
        tk.Label(top_frame, text="Project Name:").grid(row=0, column=0)
        self.project_name = tk.Entry(top_frame)
        self.project_name.grid(row=0, column=1)

        tk.Button(bottom_frame, text='Cancel', command=self.back_new_job_window).grid(row=0, column=0)
        tk.Button(bottom_frame, text='Save New Job', command=self.save_new_job_window).grid(row=0, column=1)
        bottom_frame.grid()
        self.new_job_window = self

        model_frame = tk.Frame(main_frame, relief="raised", borderwidth=3)
        model_frame.grid(row=1, column=0)
        tk.Label(model_frame, text="Training file").grid(row=0, column=0, sticky='e')
        self.button_open_training_file = tk.Button(model_frame, text="Select a file",
                                                   command=self.set_training_file)
        self.button_open_training_file.grid(row=0, column=1)

        tk.Label(model_frame, text="Number of iterations:").grid(row=1, column=0, sticky='e')
        self.number_of_iterations = tk.Entry(model_frame)
        self.number_of_iterations.grid(row=1, column=1)
        tk.Label(model_frame, text="Dropout (keep low, ~0-0.2):").grid(row=2, sticky='e')
        self.dropout = tk.Entry(model_frame)
        self.dropout.grid(row=2, column=1)
        tk.Label(model_frame, text="Training Data Percent, 0-1.0):").grid(row=3, sticky='e')
        self.training_data_percent = tk.Entry(model_frame)
        self.training_data_percent.grid(row=3, column=1)
        tk.Label(model_frame, text="Temperatures to generate:").grid(row=4, sticky='e')
        self.temperatures_to_generate = tk.Entry(model_frame)
        self.temperatures_to_generate.grid(row=4, column=1)
        tk.Label(model_frame, text="Items to generate between generations:").grid(row=5, sticky='e')
        self.items_to_generate_between_generations = tk.Entry(model_frame)
        self.items_to_generate_between_generations.grid(row=5, column=1)
        tk.Label(model_frame, text="Generate every _ generations:").grid(row=6, sticky='e')
        self.generation_frequency = tk.Entry(model_frame)
        self.generation_frequency.grid(row=6, column=1)
        tk.Label(model_frame, text="Save model every _ generations:").grid(row=7, sticky='e')
        self.save_frequency = tk.Entry(model_frame)
        self.save_frequency.grid(row=7, column=1)
        tk.Label(model_frame, text="Items to generate at end:").grid(row=8, sticky='e')
        self.items_to_generate_at_end = tk.Entry(model_frame)
        self.items_to_generate_at_end.grid(row=8, column=1)

        # Set some sane defaults:
        self.number_of_iterations.insert(tk.END, "5")
        self.dropout.insert(tk.END, "0")
        self.temperatures_to_generate.insert(tk.END, "0.5, 1.0, 1.25")
        self.items_to_generate_between_generations.insert(tk.END, "50")
        self.training_data_percent.insert(tk.END, "0.75")
        self.generation_frequency.insert(tk.END, "1")
        self.save_frequency.insert(tk.END, "2")
        self.items_to_generate_at_end.insert(tk.END, "500")

        top_frame.grid(row=0, column=0)
        model_frame.grid(row=1, column=0)
        bottom_frame.grid(row=3, column=0)


class NewJobWindowLoad(AbstractNewJobWindow):
    """UI for new jobs, but continuing from an existing model."""

    def __init__(self):
        super().__init__()

        self.new_job_load_model_window = self
        self.title("Create New Job, Load Model - simple-text-generator")
        main_frame = tk.Frame(self)
        main_frame.grid()
        top_frame = tk.Frame(main_frame)
        bottom_frame = tk.Frame(main_frame)
        tk.Label(top_frame, text="Project Name:").grid(row=0, column=0)
        self.project_name = tk.Entry(top_frame)
        self.project_name.grid(row=0, column=1)

        tk.Button(bottom_frame, text='Cancel', command=self.back_new_job_load_model_window).grid(row=0, column=0)
        tk.Button(bottom_frame, text='Save New Job', command=self.save_new_job_load_model_window).grid(row=0, column=1)
        bottom_frame.grid()

        model_frame = tk.Frame(main_frame, relief="raised", borderwidth=3)
        model_frame.grid(row=1, column=0)
        tk.Label(model_frame, text="Training file").grid(row=0, column=0, sticky='e')
        self.button_open_training_file = tk.Button(model_frame, text="Select a file",
                                                   command=self.set_training_file)
        self.button_open_training_file.grid(row=0, column=1)

        tk.Label(model_frame, text="Model file").grid(row=1, column=0, sticky='e')
        self.button_open_model_file = tk.Button(model_frame, text="Select a model file (.hdf5)",
                                                command=self.set_model_file)
        self.button_open_model_file.grid(row=1, column=1)

        tk.Label(model_frame, text="Number of iterations:").grid(row=2, column=0, sticky='e')
        self.number_of_iterations = tk.Entry(model_frame)
        self.number_of_iterations.grid(row=2, column=1)
        tk.Label(model_frame, text="Dropout (keep low, ~0-0.2):").grid(row=3, sticky='e')
        self.dropout = tk.Entry(model_frame)
        self.dropout.grid(row=3, column=1)
        tk.Label(model_frame, text="Training Data Percent, 0-1.0):").grid(row=4, sticky='e')
        self.training_data_percent = tk.Entry(model_frame)
        self.training_data_percent.grid(row=4, column=1)
        tk.Label(model_frame, text="Temperatures to generate:").grid(row=5, sticky='e')
        self.temperatures_to_generate = tk.Entry(model_frame)
        self.temperatures_to_generate.grid(row=5, column=1)
        tk.Label(model_frame, text="Items to generate between generations:").grid(row=6, sticky='e')
        self.items_to_generate_between_generations = tk.Entry(model_frame)
        self.items_to_generate_between_generations.grid(row=6, column=1)
        tk.Label(model_frame, text="Generate every _ generations:").grid(row=7, sticky='e')
        self.generation_frequency = tk.Entry(model_frame)
        self.generation_frequency.grid(row=7, column=1)
        tk.Label(model_frame, text="Save model every _ generations:").grid(row=8, sticky='e')
        self.save_frequency = tk.Entry(model_frame)
        self.save_frequency.grid(row=8, column=1)
        tk.Label(model_frame, text="Items to generate at end:").grid(row=9, sticky='e')
        self.items_to_generate_at_end = tk.Entry(model_frame)
        self.items_to_generate_at_end.grid(row=9, column=1)

        # Set some sane defaults:
        self.number_of_iterations.insert(tk.END, "5")
        self.dropout.insert(tk.END, "0")
        self.temperatures_to_generate.insert(tk.END, "0.5, 1.0, 1.25")
        self.items_to_generate_between_generations.insert(tk.END, "50")
        self.training_data_percent.insert(tk.END, "0.75")
        self.generation_frequency.insert(tk.END, "1")
        self.save_frequency.insert(tk.END, "2")
        self.items_to_generate_at_end.insert(tk.END, "500")

        top_frame.grid(row=0, column=0)
        model_frame.grid(row=1, column=0)
        bottom_frame.grid(row=3, column=0)


class NewJobWindowBatch(AbstractNewJobWindow):
    """UI for new jobs, set up as a batch."""

    def __init__(self):
        super().__init__()

        if self.new_batch_job_window is not None:
            self.new_batch_job_window = None

        self.title("Create New Batch Jobs - simple-text-generator")
        main_frame = tk.Frame(self)
        main_frame.grid()
        top_frame = tk.Frame(main_frame)
        bottom_frame = tk.Frame(main_frame)

        tk.Button(bottom_frame, text='Cancel', command=self.back_new_job_window).grid(row=0, column=0)
        tk.Button(bottom_frame, text='Save New Job', command=self.save_new_batch_job_window).grid(row=0, column=1)
        bottom_frame.grid()
        self.new_job_window = self

        model_frame = tk.Frame(main_frame, relief="raised", borderwidth=3)
        model_frame.grid(row=1, column=0)
        tk.Label(model_frame, text="Training file").grid(row=0, column=0, sticky='e')
        self.button_open_training_file = tk.Button(model_frame, text="Select files",
                                                   command=self.set_training_file_batch)
        self.button_open_training_file.grid(row=0, column=1)

        tk.Label(model_frame, text="Number of iterations:").grid(row=1, column=0, sticky='e')
        self.number_of_iterations = tk.Entry(model_frame)
        self.number_of_iterations.grid(row=1, column=1)
        tk.Label(model_frame, text="Dropout (keep low, ~0-0.2):").grid(row=2, sticky='e')
        self.dropout = tk.Entry(model_frame)
        self.dropout.grid(row=2, column=1)
        tk.Label(model_frame, text="Training Data Percent, 0-1.0):").grid(row=3, sticky='e')
        self.training_data_percent = tk.Entry(model_frame)
        self.training_data_percent.grid(row=3, column=1)
        tk.Label(model_frame, text="Temperatures to generate:").grid(row=4, sticky='e')
        self.temperatures_to_generate = tk.Entry(model_frame)
        self.temperatures_to_generate.grid(row=4, column=1)
        tk.Label(model_frame, text="Items to generate between generations:").grid(row=5, sticky='e')
        self.items_to_generate_between_generations = tk.Entry(model_frame)
        self.items_to_generate_between_generations.grid(row=5, column=1)
        tk.Label(model_frame, text="Generate every _ generations:").grid(row=6, sticky='e')
        self.generation_frequency = tk.Entry(model_frame)
        self.generation_frequency.grid(row=6, column=1)
        tk.Label(model_frame, text="Save model every _ generations:").grid(row=7, sticky='e')
        self.save_frequency = tk.Entry(model_frame)
        self.save_frequency.grid(row=7, column=1)
        tk.Label(model_frame, text="Items to generate at end:").grid(row=8, sticky='e')
        self.items_to_generate_at_end = tk.Entry(model_frame)
        self.items_to_generate_at_end.grid(row=8, column=1)

        # Set some sane defaults:
        self.number_of_iterations.insert(tk.END, "5")
        self.dropout.insert(tk.END, "0")
        self.temperatures_to_generate.insert(tk.END, "0.5, 1.0, 1.25")
        self.items_to_generate_between_generations.insert(tk.END, "50")
        self.training_data_percent.insert(tk.END, "0.75")
        self.generation_frequency.insert(tk.END, "1")
        self.save_frequency.insert(tk.END, "2")
        self.items_to_generate_at_end.insert(tk.END, "500")

        top_frame.grid(row=0, column=0)
        model_frame.grid(row=1, column=0)
        bottom_frame.grid(row=3, column=0)
