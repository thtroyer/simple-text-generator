import os
from shutil import copyfile
from tkinter import filedialog
import tkinter as tk
import chevron
from pathlib import Path
from simpletextgenerator.jobs_util import create_job, resource_path
from simpletextgenerator.models.config import Config
from simpletextgenerator.training_status import TrainingStatus


def draw_edit_existing_job_window():
    edit_existing_job_window = EditJobWindow()
    edit_existing_job_window.draw_edit_existing_job_window()


class EditJobWindow:
    def __init__(self):
        try:
            self.selected_project_name.set("default")
        except AttributeError:
            # todo fix
            pass
        self.edit_job_window = None

        self.number_of_iterations = None
        self.project_name_edit_text = None
        self.dropout = None
        self.temperatures_to_generate = None
        self.items_to_generate_between_generations = None
        self.training_data_percent = None
        self.generation_frequency = None
        self.save_frequency = None
        self.items_to_generate_at_end = None
        self.button_open_training_file = None
        self.training_file = None
        self.training_file_origin_path = None
        self.model_to_load = None
        self.selected_project_name = None
        self.project_name_select = None
        self.project_name = ""

    def edit_existing_job_select_updated(self, selected_value):
        self.project_name_edit_text = selected_value
        self.selected_project_name.set(selected_value)
        self.project_name = selected_value
        loaded_job = create_job(selected_value)
        loaded_config = loaded_job.config
        temperature_strings = ['{:.2f}'.format(temp) for temp in loaded_config.temperatures_to_generate]
        temperature_string = ",".join(temperature_strings)

        self.number_of_iterations.delete(0, tk.END)
        self.number_of_iterations.insert(tk.END, loaded_config.num_loops)
        self.dropout.delete(0, tk.END)
        self.dropout.insert(tk.END, loaded_config.dropout)
        self.temperatures_to_generate.delete(0, tk.END)
        self.temperatures_to_generate.insert(tk.END, temperature_string)
        self.items_to_generate_between_generations.delete(0, tk.END)
        self.items_to_generate_between_generations.insert(tk.END, loaded_config.items_to_generate_each_generation)
        self.training_data_percent.delete(0, tk.END)
        self.training_data_percent.insert(tk.END, loaded_config.training_data_percent)
        self.generation_frequency.delete(0, tk.END)
        self.generation_frequency.insert(tk.END, loaded_config.generate_every_n_generations)
        self.save_frequency.delete(0, tk.END)
        self.save_frequency.insert(tk.END, loaded_config.save_model_every_n_generations)
        self.items_to_generate_at_end.delete(0, tk.END)
        self.items_to_generate_at_end.insert(tk.END, loaded_config.items_to_generate_at_end)

    def draw_edit_existing_job_window(self):
        if self.edit_job_window is not None:
            self.edit_job_window = None

        edit_job_window = tk.Tk()
        self.selected_project_name = tk.StringVar(edit_job_window)
        edit_job_window.title("Edit existing job - simple-text-generator")
        main_frame = tk.Frame(edit_job_window)
        main_frame.grid()
        top_frame = tk.Frame(main_frame)
        tk.Label(top_frame, text="Project Name:").grid(row=0, column=0)
        bottom_frame = tk.Frame(main_frame)
        option_list = self.get_projects_from_disk()
        self.selected_project_name.set("Select a project")
        self.project_name_select = tk.OptionMenu(
            top_frame,
            self.selected_project_name,
            *option_list,
            command=self.edit_existing_job_select_updated
        )

        self.project_name_select.config(width=30)
        self.project_name_select.grid(row=0, column=1)

        tk.Button(bottom_frame, text='Cancel', command=self.destroy_window()).grid(row=0, column=0)
        tk.Button(bottom_frame, text='Edit Job', command=self.save_edit_job_window).grid(row=0, column=1)
        bottom_frame.grid()
        self.edit_job_window = edit_job_window

        model_frame = tk.Frame(main_frame, relief="raised", borderwidth=3)
        model_frame.grid(row=1, column=0)
        tk.Label(model_frame, text="Training file").grid(row=0, column=0)
        self.button_open_training_file = tk.Button(model_frame, text="Select a file",
                                                   command=self.set_training_file)
        self.button_open_training_file.grid(row=0, column=1)

        tk.Label(model_frame, text="Number of iterations:").grid(row=1, column=0)
        self.number_of_iterations = tk.Entry(model_frame)
        self.number_of_iterations.grid(row=1, column=1)
        tk.Label(model_frame, text="Dropout (keep low, ~0-0.2):").grid(row=2)
        self.dropout = tk.Entry(model_frame)
        self.dropout.grid(row=2, column=1)
        tk.Label(model_frame, text="Training Data Percent, 0-1.0):").grid(row=3)
        self.training_data_percent = tk.Entry(model_frame)
        self.training_data_percent.grid(row=3, column=1)
        tk.Label(model_frame, text="Temperatures to generate:").grid(row=4)
        self.temperatures_to_generate = tk.Entry(model_frame)
        self.temperatures_to_generate.grid(row=4, column=1)
        tk.Label(model_frame, text="Items to generate between generations:").grid(row=5)
        self.items_to_generate_between_generations = tk.Entry(model_frame)
        self.items_to_generate_between_generations.grid(row=5, column=1)
        tk.Label(model_frame, text="Generate every _ generations:").grid(row=6)
        self.generation_frequency = tk.Entry(model_frame)
        self.generation_frequency.grid(row=6, column=1)
        tk.Label(model_frame, text="Save model every _ generations:").grid(row=7)
        self.save_frequency = tk.Entry(model_frame)
        self.save_frequency.grid(row=7, column=1)
        tk.Label(model_frame, text="Items to generate at end:").grid(row=8)
        self.items_to_generate_at_end = tk.Entry(model_frame)
        self.items_to_generate_at_end.grid(row=8, column=1)

        top_frame.grid(row=0, column=0)
        model_frame.grid(row=2, column=0)
        bottom_frame.grid(row=3, column=0)

    def save_edit_job_window(self):
        if self.project_name_edit_text is None:
            raise Exception("No project selected")

        try:
            project_path = "projects/" + self.project_name_edit_text
            self.create_config_file(project_path)
            self.create_state_file(project_path)
            self.edit_job_window.destroy()
        except Exception as e:
            # todo remove
            print(e)
            raise e

    def create_config_file(self, path):
        with open(path + '/config.yaml', 'w') as f:
            f.write(self.render_config_file_text())

    def create_state_file(self, path):
        with open(path + '/state.yaml', 'w') as f:
            f.write(self.render_state_file_text())

    def get_projects_from_disk(self):
        project_path = 'projects/'
        project_list = []
        for path in os.listdir(project_path):
            if os.path.isdir(os.path.join(project_path, path)):
                project_list.append(path)

        project_list.remove("archive")
        return project_list

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

    def destroy_window(self):
        if self.edit_job_window is not None:
            self.edit_job_window.destroy()

    def set_training_file(self):
        self.training_file_origin_path = self.open_file_dialog("txt")
        self.edit_job_window.lift()
        self.training_file = Path(self.training_file_origin_path).name
        copyfile(self.training_file_origin_path, f"projects/{self.project_name}/{self.training_file}")
        self.button_open_training_file['text'] = self.training_file

    @staticmethod
    def open_file_dialog(default_ext: str):
        home = os.path.expanduser('~')
        return filedialog.askopenfilename(
            initialdir=home,
            title="Select file",
            filetypes=(("file_type", f"*.{default_ext}"), ("all files", "*.*"))
        )
