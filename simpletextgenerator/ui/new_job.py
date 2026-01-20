import logging
import os
import tkinter as tk
from os.path import splitext
from pathlib import Path
from shutil import copyfile
from typing import List, Optional

import chevron

from simpletextgenerator.jobs_util import resource_path
from simpletextgenerator.models.config import Config
from simpletextgenerator.training_status import TrainingStatus
from simpletextgenerator.ui.base import BaseWindow, JobConfigForm

logger = logging.getLogger("ui")


def draw_new_job_window(parent):
    NewJobWindow(parent)


def draw_new_job_load_model_window(parent):
    NewJobWindowLoad(parent)


def draw_new_batch_job_window(parent):
    NewJobWindowBatch(parent)


class AbstractNewJobWindow(BaseWindow):
    """Parent class for the 3 related UIs in this file."""

    def __init__(self, parent, title):
        super().__init__(parent, title)
        self.project_name: Optional[tk.Entry] = None
        self.job_config: Optional[JobConfigForm] = None

        self.training_file: str = ""
        self.training_file_origin_path: str = ""
        self.model_to_load: Optional[str] = None
        self.model_to_load_origin_path: str = ""
        self.batch_training_files: List[str] = []

    def _init_common_ui(self):
        main_frame = tk.Frame(self)
        main_frame.pack(padx=10, pady=10)

        top_frame = tk.Frame(main_frame)
        top_frame.pack(pady=5)

        tk.Label(top_frame, text="Project Name:").grid(row=0, column=0, sticky='e')
        self.project_name = tk.Entry(top_frame)
        self.project_name.grid(row=0, column=1, sticky='w')

        self.job_config = JobConfigForm(main_frame)
        self.job_config.pack(pady=5)

        bottom_frame = tk.Frame(main_frame)
        bottom_frame.pack(pady=10)

        tk.Button(bottom_frame, text='Cancel', command=self.destroy).grid(row=0, column=0, padx=5)
        tk.Button(bottom_frame, text='Save New Job', command=self.save_job).grid(row=0, column=1, padx=5)

    def save_job(self):
        # To be implemented by subclasses
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
                training_file=self.training_file,
                output_file="",
                output_dir="",
                num_loops=self.job_config.get_value("num_iterations"),
                priority="0",
                temperatures_to_generate=list(map(str.strip, self.job_config.get_value("temperatures").split(','))),
                project_root_dir="",
                job_name="",
                input_folder="",
                output_folder="",
                items_to_generate_each_generation=self.job_config.get_value("items_between"),
                items_to_generate_at_end=self.job_config.get_value("items_at_end"),
                generate_every_n_generations=self.job_config.get_value("gen_frequency"),
                save_model_every_n_generations=self.job_config.get_value("save_frequency"),
                dropout=self.job_config.get_value("dropout"),
                training_data_percent=self.job_config.get_value("training_data_percent"),
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


class NewJobWindow(AbstractNewJobWindow):
    """UI for completely new jobs."""

    def __init__(self, parent):
        super().__init__(parent, "Create New Job - simple-text-generator")
        self._init_ui()

    def _init_ui(self):
        self._init_common_ui()

        # Insert Training File button at the top of the form
        self.job_config.fields = {} # Reset fields to preserve order if needed, but dicts are ordered in py3.7+
        # Actually, JobConfigForm creates widgets on init. We can just add widgets to it.
        # But we want it at specific position. JobConfigForm uses grid.
        # We can shift existing widgets down or just insert at row 0 if we reset everything.
        # Easier: Just add it to JobConfigForm as a custom field if we modify JobConfigForm to support inserting custom widgets or
        # we can just use `add_file_selector` provided by JobConfigForm if we add it.

        # Let's see BaseWindow again. JobConfigForm has add_file_selector.
        # But it appends.

        # Ideally, I should have designed JobConfigForm to be more flexible.
        # But for now, I can just destroy the JobConfigForm created in _init_common_ui and create a new one with correct order,
        # OR I can just modify _init_common_ui to NOT create JobConfigForm, and let subclasses do it.
        pass

    # Override _init_common_ui to allow custom order
    def _init_common_ui(self):
        main_frame = tk.Frame(self)
        main_frame.pack(padx=10, pady=10)

        top_frame = tk.Frame(main_frame)
        top_frame.pack(pady=5)

        tk.Label(top_frame, text="Project Name:").grid(row=0, column=0, sticky='e')
        self.project_name = tk.Entry(top_frame)
        self.project_name.grid(row=0, column=1, sticky='w')

        self.job_config = JobConfigForm(main_frame, show_fields=[]) # Empty initially
        self.job_config.pack(pady=5)

        self.setup_form()

        bottom_frame = tk.Frame(main_frame)
        bottom_frame.pack(pady=10)

        tk.Button(bottom_frame, text='Cancel', command=self.destroy).grid(row=0, column=0, padx=5)
        tk.Button(bottom_frame, text='Save New Job', command=self.save_job).grid(row=0, column=1, padx=5)

    def setup_form(self):
        self.job_config.add_file_selector("Training file", "training_file", self.set_training_file)
        # Add rest of fields
        defaults = [
            ("Number of iterations:", "num_iterations", "5"),
            ("Dropout (keep low, ~0-0.2):", "dropout", "0"),
            ("Training Data Percent, 0-1.0):", "training_data_percent", "0.75"),
            ("Temperatures to generate:", "temperatures", "0.5, 1.0, 1.25"),
            ("Items to generate between generations:", "items_between", "50"),
            ("Generate every _ generations:", "gen_frequency", "1"),
            ("Save model every _ generations:", "save_frequency", "2"),
            ("Items to generate at end:", "items_at_end", "500"),
        ]
        for lbl, key, val in defaults:
            self.job_config.add_entry(lbl, key, val)

    def set_training_file(self):
        path = self.open_file_dialog("Select file", [("Text files", "*.txt"), ("All files", "*.*")])
        if path:
            self.training_file_origin_path = path
            self.training_file = Path(path).name
            self.job_config.fields["training_file"]['text'] = self.training_file
            self.lift()

    def save_job(self):
        try:
            project_path = "projects/" + self.project_name.get()
            self.create_new_project_dir(project_path)
            self.create_config_file(project_path)
            self.create_state_file(project_path)
            self.copy_training_file(project_path)
            self.destroy()
        except Exception as e:
            logger.error(e)
            self.show_error(str(e))


class NewJobWindowLoad(AbstractNewJobWindow):
    """UI for new jobs, but continuing from an existing model."""

    def __init__(self, parent):
        super().__init__(parent, "Create New Job, Load Model - simple-text-generator")
        self._init_ui()

    def _init_ui(self):
        self._init_common_ui()

    def setup_form(self):
        self.job_config.add_file_selector("Training file", "training_file", self.set_training_file)
        self.job_config.add_file_selector("Model file", "model_file", self.set_model_file, button_text="Select a model file (.hdf5)")

        defaults = [
            ("Number of iterations:", "num_iterations", "5"),
            ("Dropout (keep low, ~0-0.2):", "dropout", "0"),
            ("Training Data Percent, 0-1.0):", "training_data_percent", "0.75"),
            ("Temperatures to generate:", "temperatures", "0.5, 1.0, 1.25"),
            ("Items to generate between generations:", "items_between", "50"),
            ("Generate every _ generations:", "gen_frequency", "1"),
            ("Save model every _ generations:", "save_frequency", "2"),
            ("Items to generate at end:", "items_at_end", "500"),
        ]
        for lbl, key, val in defaults:
            self.job_config.add_entry(lbl, key, val)

    def set_training_file(self):
        path = self.open_file_dialog("Select file", [("Text files", "*.txt"), ("All files", "*.*")])
        if path:
            self.training_file_origin_path = path
            self.training_file = Path(path).name
            self.job_config.fields["training_file"]['text'] = self.training_file
            self.lift()

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
            self.copy_training_file(project_path)
            self.copy_model_file(project_path)
            self.destroy()
        except Exception as e:
            logger.error(e)
            self.show_error(str(e))

    def copy_model_file(self, project_path):
        copyfile(self.model_to_load_origin_path, f"{project_path}/m_{self.model_to_load}")


class NewJobWindowBatch(AbstractNewJobWindow):
    """UI for new jobs, set up as a batch."""

    def __init__(self, parent):
        super().__init__(parent, "Create New Batch Jobs - simple-text-generator")
        # Reuse init logic, but need to hide project name entry as it's derived from files
        self._init_ui()
        # Hide project name entry
        # self.project_name.master.pack_forget() # This would hide the whole top frame if it's the only child
        # But we created top_frame.

    def _init_ui(self):
        # Override to skip project name
        main_frame = tk.Frame(self)
        main_frame.pack(padx=10, pady=10)

        self.job_config = JobConfigForm(main_frame, show_fields=[])
        self.job_config.pack(pady=5)
        self.setup_form()

        bottom_frame = tk.Frame(main_frame)
        bottom_frame.pack(pady=10)

        tk.Button(bottom_frame, text='Cancel', command=self.destroy).grid(row=0, column=0, padx=5)
        tk.Button(bottom_frame, text='Save New Job', command=self.save_job).grid(row=0, column=1, padx=5)

    def setup_form(self):
        self.job_config.add_file_selector("Training files", "training_files", self.set_training_file_batch, button_text="Select files")

        defaults = [
            ("Number of iterations:", "num_iterations", "5"),
            ("Dropout (keep low, ~0-0.2):", "dropout", "0"),
            ("Training Data Percent, 0-1.0):", "training_data_percent", "0.75"),
            ("Temperatures to generate:", "temperatures", "0.5, 1.0, 1.25"),
            ("Items to generate between generations:", "items_between", "50"),
            ("Generate every _ generations:", "gen_frequency", "1"),
            ("Save model every _ generations:", "save_frequency", "2"),
            ("Items to generate at end:", "items_at_end", "500"),
        ]
        for lbl, key, val in defaults:
            self.job_config.add_entry(lbl, key, val)

    def set_training_file_batch(self):
        paths = self.open_files_dialog("Select files", [("Text files", "*.txt"), ("All files", "*.*")])
        if paths:
            self.batch_training_files = paths
            self.job_config.fields["training_files"]['text'] = f"{len(paths)} files selected"
            self.lift()

    def save_job(self):
        try:
            if not self.batch_training_files:
                raise Exception("No files selected")

            for training_file in self.batch_training_files:
                self.training_file_origin_path = training_file
                file_name = os.path.basename(training_file)
                self.training_file = file_name
                project_name = splitext(file_name)[0]
                project_path = "projects/" + project_name

                self.create_new_project_dir(project_path)
                # self.training_file is already set
                self.create_config_file(project_path)
                self.create_state_file(project_path)
                self.copy_training_file(project_path)
            self.destroy()
        except Exception as e:
            logger.error(e)
            self.show_error(str(e))
