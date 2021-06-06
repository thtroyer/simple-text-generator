import os
import pathlib
from os.path import splitext
from shutil import copyfile
from tkinter import filedialog
import tkinter as tk
import chevron
from pathlib import Path
from tkinter.messagebox import showwarning
import subprocess

import run_training
from simpletextgenerator.models.config import Config
from simpletextgenerator.training import TrainingStatus
from simpletextgenerator.ui import new_job


# This is my first tkinter project.
# I highly recommend not using this UI as a good example of anything.  It is currently
# a mess.  Maybe eventually it'll be good, but I suggest avoid looking at this file for now.

# todo add training data percent to UI


class WindowManager:
    def __init__(self):
        self.main_window = None
        self.new_job_window = None
        self.new_batch_job_window = None
        self.edit_job_window = None
        self.new_job_load_model_window = None
        # fields in new_job_window
        self.number_of_iterations = None
        self.project_name = None
        self.project_name_edit_text = None
        self.dropout = None
        self.temperatures_to_generate = None
        self.items_to_generate_between_generations = None
        self.training_data_percent = None
        self.generation_frequency = None
        self.save_frequency = None
        self.items_to_generate_at_end = None
        self.button_open_training_file = None
        self.button_open_model_file = None
        self.training_file = None
        self.batch_training_files = None
        self.training_file_origin_path = None
        self.model_to_load = None
        self.model_to_load_origin_path = None

    def draw_main_window(self):
        main_window = tk.Tk()
        main_window.title('simple-text-generator')
        main_window.geometry("300x180")
        main_frame = tk.Frame(main_window)
        main_frame.pack()
        tk.Button(
            main_frame,
            text='Create new job',
            command=new_job.draw_new_job_window,
            width=35
        ).pack()

        tk.Button(
            main_frame,
            text='Create new batch job',
            command=new_job.draw_new_batch_job_window,
            width=35
        ).pack()

        tk.Button(
            main_frame,
            text='Create new job, using another model',
            command=new_job.draw_new_job_load_model_window,
            width=35
        ).pack()

        tk.Button(
            main_frame,
            text='Edit existing job',
            command=self.draw_edit_existing_job_window,
            width=35
        ).pack()

        tk.Button(
            main_frame,
            text='Archive job',
            command=quit,
            state=tk.DISABLED,
            width=35
        ).pack()

        tk.Button(
            main_frame,
            text='Delete job',
            command=quit,
            state=tk.DISABLED,
            width=35
        ).pack()

        # tk.Button(
        #     main_frame,
        #     text='Run jobs (Linux only, experimental)',
        #     command=self.run_training,
        #     width=35
        # ).pack()

        main_window.mainloop()
        self.main_window = main_window

    def edit_existing_job_select_updated(self, selected_value):
        self.project_name_edit_text = selected_value
        self.selected_project_name.set(selected_value)
        loaded_job = run_training.create_job(f"./projects/{selected_value}")
        loaded_config = loaded_job.config
        temperature_strings = ['{:.2f}'.format(temp) for temp in loaded_config.temperatures_to_generate]
        temperature_string = ",".join(temperature_strings)

        self.number_of_iterations.delete(0, tk.END)
        self.number_of_iterations.insert(tk.END, loaded_config.num_loops)
        self.dropout.delete(0, tk.END)
        self.dropout.insert(tk.END, loaded_config.num_loops)
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
        edit_job_window.title("Edit existing job - simple-text-generator")
        main_frame = tk.Frame(edit_job_window)
        main_frame.grid()
        top_frame = tk.Frame(main_frame)
        tk.Label(top_frame, text="Project Name:").grid(row=0, column=0)
        bottom_frame = tk.Frame(main_frame)
        option_list = self.get_projects_from_disk()
        self.selected_project_name = tk.StringVar()
        self.selected_project_name.set(option_list[0])
        self.project_name_select = tk.OptionMenu(
            top_frame,
            self.selected_project_name,
            *option_list,
            command=self.edit_existing_job_select_updated
        )

        self.project_name_select.config(width=10)
        self.project_name_select.grid(row=0, column=1)

        tk.Button(bottom_frame, text='Cancel', command=self.back_new_job_window).grid(row=0, column=0)
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


    def render_config_file_text(self):
        with open('templates/config.yml.mustache', 'r') as f:
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

    def create_config_file(self, path):
        with open(path + '/config.yaml', 'w') as f:
            f.write(self.render_config_file_text())

    def create_state_file(self, path):
        with open(path + '/state.yaml', 'w') as f:
            f.write(self.render_state_file_text())

    def set_training_file(self):
        self.training_file_origin_path = self.open_file_dialog("txt")
        self.training_file = Path(self.training_file_origin_path).name
        self.button_open_training_file['text'] = self.training_file

    def set_training_file_batch(self):
        # root = tk.Tk()
        self.batch_training_files = tk.filedialog.askopenfilenames(title='Choose a file')

        # self.button_open_model_file['text'] = self.model_to_load

    def set_model_file(self):
        self.model_to_load_origin_path = self.open_file_dialog("hdf5")
        self.model_to_load = Path(self.model_to_load_origin_path).name
        self.button_open_model_file['text'] = self.model_to_load

    def copy_training_file(self, project_path):
        current_dir = pathlib.Path(__file__).parent
        copyfile(self.training_file_origin_path, str(current_dir) + "/" + project_path + "/" + self.training_file)

    def copy_model_file(self, project_path):
        current_dir = pathlib.Path(__file__).parent
        copyfile(self.model_to_load_origin_path,
                 str(current_dir) + "/" + project_path + "/" + f"m_{self.model_to_load}")

    def render_state_file_text(self):
        status = TrainingStatus.NEW
        if self.model_to_load is not None:
            status = TrainingStatus.NEW_LOAD_MODEL

        with open('templates/state.yml.mustache', 'r') as f:
            return (chevron.render(f, {
                'status': status,
                'iterations_run': 0,
                'latest_model_saved': ''
            }))

    @staticmethod
    def open_file_dialog(default_ext: str):
        home = os.path.expanduser('~')
        return filedialog.askopenfilename(
            initialdir=home,
            title="Select file",
            filetypes=(("file_type", f"*.{default_ext}"), ("all files", "*.*"))
        )

    @staticmethod
    def run_training():

        training_window = tk.Tk()
        training_window.title("Training - simple-text-generator")
        training_window.geometry("800x600")

        label = tk.Label(training_window, text="Output of run_training.py")
        label.pack(fill=tk.X)

        # todo - find Windows solution
        xterm_frame = tk.Frame(training_window)
        xterm_frame.pack(fill=tk.BOTH, expand=True)

        xterm_frame_id = xterm_frame.winfo_id()

        try:
            # todo - sizing needs work.  bottom part of xterm remains hidden
            p = subprocess.Popen(
                ["xterm", "-into", str(xterm_frame_id), "-geometry", "120x40",
                 '-e', 'source env/bin/activate; python3.8 run_training.py'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                cwd="/home/tom/code/simple-text-generator")
        except FileNotFoundError:
            showwarning("Error", "xterm is not installed")
            raise SystemExit

        training_window.mainloop()

    def get_projects_from_disk(self):
        project_path = 'projects/'
        project_list = []
        for path in os.listdir(project_path):
            if os.path.isdir(os.path.join(project_path, path)):
                project_list.append(path)

        project_list.remove("archive")
        return project_list


if __name__ == "__main__":
    window_manager = WindowManager()
    window_manager.draw_main_window()
