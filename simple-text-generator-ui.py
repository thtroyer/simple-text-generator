import os
import pathlib
from shutil import copyfile
from tkinter import filedialog
import tkinter as tk
import chevron
from pathlib import Path
from tkinter.messagebox import showwarning
import subprocess

from simpletextgenerator.models.config import Config
from simpletextgenerator.training import TrainingStatus
from simpletextgenerator.ui import new_job, edit_job


# This is my first tkinter project.
# I highly recommend not using this UI as a good example of anything.  It is currently
# a mess.  Maybe eventually it'll be good, but I suggest avoid looking at the UI portion for now.

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
            command=edit_job.draw_edit_existing_job_window,
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
