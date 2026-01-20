import logging
import os
import tkinter as tk
from os.path import splitext
from pathlib import Path
from shutil import copyfile
from tkinter import filedialog, messagebox
from typing import List, Optional

import chevron

from simpletextgenerator.jobs_util import resource_path
from simpletextgenerator.models.config import Config
from simpletextgenerator.training_status import TrainingStatus
from simpletextgenerator.ui.base import BaseWindow, JobConfigForm

logger = logging.getLogger("ui")


def draw_generation_job_window(parent):
    GenerationJobWindow(parent)


def draw_generation_batch_job_window(parent):
    GenerationBatchJobWindow(parent)


class BaseGenerationJobWindow(BaseWindow):
    def __init__(self, parent, title):
        super().__init__(parent, title)
        self.job_config: Optional[JobConfigForm] = None
        self.model_to_load: Optional[str] = None
        self.model_to_load_origin_path: str = ""

    def _init_common_ui(self):
        main_frame = tk.Frame(self)
        main_frame.pack(padx=10, pady=10)

        self.top_frame = tk.Frame(main_frame)
        self.top_frame.pack(pady=5)

        # Subclasses will add to top_frame

        self.job_config = JobConfigForm(main_frame, show_fields=[])
        self.job_config.pack(pady=5)
        self.setup_form()

        bottom_frame = tk.Frame(main_frame)
        bottom_frame.pack(pady=10)

        tk.Button(bottom_frame, text='Cancel', command=self.destroy).grid(row=0, column=0, padx=5)
        tk.Button(bottom_frame, text='Save New Job', command=self.save_job).grid(row=0, column=1, padx=5)

    def setup_form(self):
        # To be implemented by subclasses
        pass

    def save_job(self):
        pass

    @staticmethod
    def create_new_project_dir(path):
        if os.path.exists(path):
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
                temperatures_to_generate=list(map(str.strip, self.job_config.get_value("temperatures").split(','))),
                project_root_dir="",
                job_name="",
                input_folder="",
                output_folder="",
                items_to_generate_each_generation="0",
                items_to_generate_at_end=self.job_config.get_value("items_at_end"),
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

    def copy_model_file(self, project_path):
        copyfile(self.model_to_load_origin_path, f"{project_path}/m_{self.model_to_load}")


class GenerationJobWindow(BaseGenerationJobWindow):
    def __init__(self, parent):
        super().__init__(parent, "Generate text from model - simple-text-generator")
        self.project_name: Optional[tk.Entry] = None
        self._init_ui()

    def _init_ui(self):
        self._init_common_ui()

        tk.Label(self.top_frame, text="Project Name:").grid(row=0, column=0, sticky='e')
        self.project_name = tk.Entry(self.top_frame)
        self.project_name.grid(row=0, column=1, sticky='w')

    def setup_form(self):
        self.job_config.add_file_selector("Model file", "model_file", self.set_model_file, button_text="Select a model file (.hdf5)")
        self.job_config.add_entry("Temperatures to generate:", "temperatures", "0.5, 1.0, 1.25")
        self.job_config.add_entry("Items to generate per temperature:", "items_at_end", "500")

    def set_model_file(self):
        path = self.open_file_dialog("Select model", [("HDF5 files", "*.hdf5"), ("All files", "*.*")])
        if path:
            self.model_to_load_origin_path = path
            self.model_to_load = Path(path).name
            self.job_config.fields["model_file"]['text'] = self.model_to_load
            self.lift()

    def save_job(self):
        try:
            project_path = "projects/" + self.project_name.get()
            self.create_new_project_dir(project_path)
            self.create_config_file(project_path)
            self.create_state_file(project_path)
            self.copy_model_file(project_path)
            self.destroy()
        except Exception as e:
            logger.error(e)
            self.show_error(str(e))


class GenerationBatchJobWindow(BaseGenerationJobWindow):
    def __init__(self, parent):
        super().__init__(parent, "Generate text from model (batch) - simple-text-generator")
        self.batch_project_prefix: Optional[tk.Entry] = None
        self.batch_model_files: List[str] = []
        self._init_ui()

    def _init_ui(self):
        self._init_common_ui()

        tk.Label(self.top_frame, text="Project Name Prefix:").grid(row=0, column=0, sticky='e')
        self.batch_project_prefix = tk.Entry(self.top_frame)
        self.batch_project_prefix.grid(row=0, column=1, sticky='w')

    def setup_form(self):
        self.job_config.add_file_selector("Model files", "model_files", self.set_model_file_batch, button_text="Select files")
        self.job_config.add_entry("Temperatures to generate:", "temperatures", "0.5, 1.0, 1.25")
        self.job_config.add_entry("Items to generate per temperature:", "items_at_end", "500")

    def set_model_file_batch(self):
        paths = self.open_files_dialog("Choose the models", [("HDF5 files", "*.hdf5"), ("All files", "*.*")])
        if paths:
            self.batch_model_files = paths
            self.job_config.fields["model_files"]['text'] = f"{len(paths)} files selected"
            self.lift()

    def save_job(self):
        try:
            if not self.batch_model_files:
                raise Exception("No files selected")

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
                self.create_state_file(project_path)
                self.copy_model_file(project_path)
            self.destroy()
        except Exception as e:
            logger.error(e)
            self.show_error(str(e))
