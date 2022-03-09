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


def draw_generation_job_window():
    train_job_window = NewGenerationJobWindow()
    train_job_window.draw_generation_window()


def draw_generation_batch_job_window():
    train_job_batch_window = NewGenerationJobWindow()
    train_job_batch_window.draw_generation_batch_window()


class NewGenerationJobWindow:

    def __init__(self):
        self.new_job_window = None
        self.new_batch_job_window = None
        self.new_job_load_model_window = None

        self.project_name = None
        self.temperatures_to_generate = None
        self.training_data_percent = None
        self.items_to_generate_at_end = None
        self.button_open_training_file = None
        self.button_open_model_file = None
        self.training_file = None
        self.batch_model_files = None
        self.training_file_origin_path = None
        self.model_to_load = None
        self.model_to_load_origin_path = None

        self.batch_project_prefix = None

    # def draw_generation_window(self):
    #     if self.new_job_window is not None:
    #         self.new_job_window = None
    #
    #     new_job_window = tk.Tk()
    #     new_job_window.title("Create New Job - simple-text-generator")
    #     main_frame = tk.Frame(new_job_window)
    #     main_frame.grid()
    #     top_frame = tk.Frame(main_frame)
    #     bottom_frame = tk.Frame(main_frame)
    #     tk.Label(top_frame, text="Project Name:").grid(row=0, column=0)
    #     self.project_name = tk.Entry(top_frame)
    #     self.project_name.grid(row=0, column=1)
    #
    #     tk.Button(bottom_frame, text='Cancel', command=self.back_new_job_window).grid(row=0, column=0)
    #     tk.Button(bottom_frame, text='Save New Job', command=self.save_new_job_window).grid(row=0, column=1)
    #     bottom_frame.grid()
    #     self.new_job_window = new_job_window
    #
    #     model_frame = tk.Frame(main_frame, relief="raised", borderwidth=3)
    #     model_frame.grid(row=1, column=0)
    #     tk.Label(model_frame, text="Training file").grid(row=0, column=0, sticky='e')
    #     self.button_open_training_file = tk.Button(model_frame, text="Select a file",
    #                                                command=self.set_training_file)
    #     self.button_open_training_file.grid(row=0, column=1)
    #
    #     tk.Label(model_frame, text="Dropout (keep low, ~0-0.2):").grid(row=2, sticky='e')
    #     self.dropout = tk.Entry(model_frame)
    #     self.dropout.grid(row=2, column=1)
    #     tk.Label(model_frame, text="Temperatures to generate:").grid(row=4, sticky='e')
    #     self.temperatures_to_generate = tk.Entry(model_frame)
    #     self.temperatures_to_generate.grid(row=4, column=1)
    #     tk.Label(model_frame, text="Items to generate at end:").grid(row=8, sticky='e')
    #     self.items_to_generate_at_end = tk.Entry(model_frame)
    #     self.items_to_generate_at_end.grid(row=8, column=1)
    #
    #     # Set some sane defaults:
    #     self.temperatures_to_generate.insert(tk.END, "0.5, 1.0, 1.25")
    #     self.items_to_generate_at_end.insert(tk.END, 500)
    #
    #     top_frame.grid(row=0, column=0)
    #     model_frame.grid(row=1, column=0)
    #     bottom_frame.grid(row=3, column=0)

    def draw_generation_window(self):
        if self.new_job_load_model_window is not None:
            self.new_job_load_model_window = None

        new_job_load_model_window = tk.Tk()
        self.new_job_load_model_window = new_job_load_model_window
        new_job_load_model_window.title("Generate text from model - simple-text-generator")
        main_frame = tk.Frame(new_job_load_model_window)
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

        tk.Label(model_frame, text="Model file").grid(row=1, column=0, sticky='e')
        self.button_open_model_file = tk.Button(model_frame, text="Select a model file (.hdf5)",
                                                command=self.set_model_file)
        self.button_open_model_file.grid(row=1, column=1)

        tk.Label(model_frame, text="Temperatures to generate:").grid(row=5, sticky='e')
        self.temperatures_to_generate = tk.Entry(model_frame)
        self.temperatures_to_generate.grid(row=5, column=1)
        tk.Label(model_frame, text="Items to generate per temperature:").grid(row=9, sticky='e')
        self.items_to_generate_at_end = tk.Entry(model_frame)
        self.items_to_generate_at_end.grid(row=9, column=1)

        # Set some sane defaults:
        self.temperatures_to_generate.insert(tk.END, "0.5, 1.0, 1.25")
        self.items_to_generate_at_end.insert(tk.END, 500)

        top_frame.grid(row=0, column=0)
        model_frame.grid(row=1, column=0)
        bottom_frame.grid(row=3, column=0)

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
                training_file="",
                output_file="",
                output_dir="",
                num_loops="0",
                priority="0",
                temperatures_to_generate=list(map(str.strip, self.temperatures_to_generate.get().split(','))),
                project_root_dir="",
                job_name="",
                input_folder="",
                output_folder="",
                items_to_generate_each_generation="0",
                items_to_generate_at_end=self.items_to_generate_at_end.get(),
                generate_every_n_generations="0",
                save_model_every_n_generations="0",
                dropout="0",
                training_data_percent="0",
                initial_model_to_load=self.model_to_load
            )
            return config.render(f)

    def create_state_file(self, path):
        with open(path + '/state.yaml', 'w') as f:
            f.write(self.render_state_file_text())

    def copy_training_file(self, project_path):
        # todo delete
        pass
        # copyfile(self.training_file_origin_path, f"./{project_path}/{self.training_file}")

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
            for batch_file in self.batch_model_files:
                self.model_to_load_origin_path = batch_file
                file_name = os.path.basename(batch_file)
                self.model_to_load = file_name
                project_name = splitext(file_name)[0]
                project_name_prefix = self.batch_project_prefix.get()
                if project_name_prefix:
                    project_name_prefix = f"{project_name_prefix}_"
                project_path = f"projects/{project_name_prefix}{project_name}"
                self.create_new_project_dir(project_path)
                self.create_config_file(project_path)
                self.training_file = ""
                self.create_state_file(project_path)
                self.copy_model_file(project_path)
            self.new_job_window.destroy()
        except Exception as e:
            # todo remove
            logger.error(e)
            raise e

    def draw_generation_batch_window(self):

        if self.new_batch_job_window is not None:
            self.new_batch_job_window = None

        new_job_window = tk.Tk()
        new_job_window.title("Generate text from model (batch) - simple-text-generator")
        main_frame = tk.Frame(new_job_window)
        main_frame.grid()
        top_frame = tk.Frame(main_frame)
        bottom_frame = tk.Frame(main_frame)

        tk.Button(bottom_frame, text='Cancel', command=self.back_new_job_window).grid(row=0, column=0)
        tk.Button(bottom_frame, text='Save New Job', command=self.save_new_batch_job_window).grid(row=0, column=1)
        bottom_frame.grid()
        self.new_job_window = new_job_window

        tk.Label(top_frame, text="Project Name Prefix:").grid(row=0, column=0)
        self.batch_project_prefix = tk.Entry(top_frame)
        self.batch_project_prefix.grid(row=0, column=1)

        model_frame = tk.Frame(main_frame, relief="raised", borderwidth=3)
        model_frame.grid(row=1, column=0)
        tk.Label(model_frame, text="Model files").grid(row=0, column=0, sticky='e')
        self.button_open_training_file = tk.Button(model_frame, text="Select files",
                                                   command=self.set_model_file_batch)
        self.button_open_training_file.grid(row=0, column=1)

        tk.Label(model_frame, text="Temperatures to generate:").grid(row=4, sticky='e')
        self.temperatures_to_generate = tk.Entry(model_frame)
        self.temperatures_to_generate.grid(row=4, column=1)
        tk.Label(model_frame, text="Items to generate per temperature:").grid(row=8, sticky='e')
        self.items_to_generate_at_end = tk.Entry(model_frame)
        self.items_to_generate_at_end.grid(row=8, column=1)

        # Set some sane defaults:
        self.temperatures_to_generate.insert(tk.END, "0.5, 1.0, 1.25")
        self.items_to_generate_at_end.insert(tk.END, 500)

        top_frame.grid(row=0, column=0)
        model_frame.grid(row=1, column=0)
        bottom_frame.grid(row=3, column=0)

    def set_model_file_batch(self):
        self.batch_model_files = tk.filedialog.askopenfilenames(title='Choose the models')
        self.new_job_window.lift()
