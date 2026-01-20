import logging
import os
import tkinter as tk
from pathlib import Path
from shutil import copyfile
from typing import List, Optional

import chevron

from simpletextgenerator.jobs_util import create_job, resource_path
from simpletextgenerator.models.config import Config
from simpletextgenerator.training_status import TrainingStatus
from simpletextgenerator.ui.base import BaseWindow, JobConfigForm

logger = logging.getLogger("ui")


def draw_edit_existing_job_window(parent):
    EditJobWindow(parent)


class EditJobWindow(BaseWindow):
    def __init__(self, parent):
        super().__init__(parent, "Edit existing job - simple-text-generator")

        self.project_name: str = ""
        self.selected_project_name: Optional[tk.StringVar] = None
        self.project_name_select: Optional[tk.OptionMenu] = None
        self.job_config: Optional[JobConfigForm] = None

        self.training_file: str = ""
        self.training_file_origin_path: str = ""
        self.model_to_load: Optional[str] = None

        self._init_ui()

    def _init_ui(self):
        main_frame = tk.Frame(self)
        main_frame.pack(padx=10, pady=10)

        top_frame = tk.Frame(main_frame)
        top_frame.pack(pady=5)

        tk.Label(top_frame, text="Project Name:").grid(row=0, column=0, sticky='e')

        self.selected_project_name = tk.StringVar(self)
        self.selected_project_name.set("Select a project")
        option_list = self.get_projects_from_disk()

        self.project_name_select = tk.OptionMenu(
            top_frame,
            self.selected_project_name,
            *option_list,
            command=self.edit_existing_job_select_updated
        )
        self.project_name_select.config(width=30)
        self.project_name_select.grid(row=0, column=1, sticky='w')

        self.job_config = JobConfigForm(main_frame, show_fields=[])
        self.job_config.pack(pady=5)
        self.setup_form()

        bottom_frame = tk.Frame(main_frame)
        bottom_frame.pack(pady=10)

        tk.Button(bottom_frame, text='Cancel', command=self.destroy).grid(row=0, column=0, padx=5)
        tk.Button(bottom_frame, text='Edit Job', command=self.save_edit_job_window).grid(row=0, column=1, padx=5)

    def setup_form(self):
        self.job_config.add_file_selector("Training file", "training_file", self.set_training_file)

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

    def get_projects_from_disk(self) -> List[str]:
        project_path = 'projects/'
        if not os.path.exists(project_path):
            os.makedirs(project_path)

        project_list = []
        for path in os.listdir(project_path):
            if os.path.isdir(os.path.join(project_path, path)):
                project_list.append(path)

        if "archive" in project_list:
            project_list.remove("archive")

        if len(project_list) == 0:
            project_list.append("No projects.")
        return project_list

    def edit_existing_job_select_updated(self, selected_value):
        if selected_value == "No projects.":
            return

        self.project_name = selected_value
        try:
            loaded_job = create_job(f"projects/{selected_value}")
            loaded_config = loaded_job.config

            # Fix potential bug where temperatures is not a list
            temps = loaded_config.temperatures_to_generate
            if isinstance(temps, list):
                # Ensure they are floats
                temperature_strings = ['{:.2f}'.format(float(temp)) for temp in temps]
                temperature_string = ",".join(temperature_strings)
            else:
                temperature_string = str(temps)

            self.job_config.set_value("num_iterations", loaded_config.num_loops)
            self.job_config.set_value("dropout", loaded_config.dropout)
            self.job_config.set_value("temperatures", temperature_string)
            self.job_config.set_value("items_between", loaded_config.items_to_generate_each_generation)
            self.job_config.set_value("training_data_percent", loaded_config.training_data_percent)
            self.job_config.set_value("gen_frequency", loaded_config.generate_every_n_generations)
            self.job_config.set_value("save_frequency", loaded_config.save_model_every_n_generations)
            self.job_config.set_value("items_at_end", loaded_config.items_to_generate_at_end)

            # Preserve initial_model_to_load
            # Note: create_config in config.py parses initial_model_to_load.
            # However, create_job uses yaml.safe_load, so config is a dict initially, then converted to Config object?
            # looking at create_job in jobs_util.py:
            # config_data = yaml.safe_load(config)
            # return job.Job(config_data, ...)
            # job.Job init calls create_config.

            # The Config object has initial_model_to_load attribute.
            self.model_to_load = loaded_config.initial_model_to_load

            # Training file
            self.training_file = loaded_config.training_file.split('/')[-1] # training_file in config is full path?
            # create_config says: training_file = project_root_dir + '/' + job_name + '/' + config_data['file']['training_file']
            # So loaded_config.training_file is an absolute path or relative from root.
            # But the file selector button expects just the filename as text usually.

            # Let's see how create_config constructs it.
            # training_file = project_root_dir + '/' + job_name + '/' + config_data['file']['training_file']
            # So it is a full path. We just want the filename.
            self.training_file = os.path.basename(loaded_config.training_file)
            self.job_config.fields["training_file"]['text'] = self.training_file

        except Exception as e:
            logger.error(f"Error loading job {selected_value}: {e}")
            self.show_error(f"Error loading job: {e}")

    def set_training_file(self):
        if not self.project_name:
             self.show_error("Please select a project first.")
             return

        path = self.open_file_dialog("Select file", [("Text files", "*.txt"), ("All files", "*.*")])
        if path:
            self.training_file_origin_path = path
            self.training_file = Path(path).name

            # Copy file immediately as in original code
            try:
                dest = f"projects/{self.project_name}/{self.training_file}"
                copyfile(self.training_file_origin_path, dest)
                self.job_config.fields["training_file"]['text'] = self.training_file
                self.lift()
            except Exception as e:
                self.show_error(f"Error copying file: {e}")

    def save_edit_job_window(self):
        if not self.project_name:
            self.show_error("No project selected")
            return

        try:
            project_path = "projects/" + self.project_name
            self.create_config_file(project_path)
            self.create_state_file(project_path)
            self.destroy()
        except Exception as e:
            logger.error(e)
            self.show_error(str(e))

    def create_config_file(self, path):
        with open(path + '/config.yaml', 'w') as f:
            f.write(self.render_config_file_text())

    def create_state_file(self, path):
        with open(path + '/state.yaml', 'w') as f:
            f.write(self.render_state_file_text())

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
