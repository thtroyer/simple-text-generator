import os
import pathlib
from shutil import copyfile
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
import chevron
from pathlib import Path
from tkinter.messagebox import showwarning
import subprocess

from simpletextgenerator.training import TrainingStatus

#todo add training data percent to UI

class WindowManager:
    def __init__(self):
        self.main_window = None
        self.new_job_window = None
        self.new_job_load_model_window = None
        # fields in new_job_window
        self.number_of_iterations = None
        self.project_name = None
        self.dropout = None
        self.temperatures_to_generate = None
        self.items_to_generate_between_generations = None
        self.generation_frequency = None
        self.save_frequency = None
        self.items_to_generate_at_end = None
        self.button_open_training_file = None
        self.button_open_model_file = None
        self.training_file = None
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
            command=self.draw_new_job_window,
            width=35
        ).pack()

        tk.Button(
            main_frame,
            text='Create new job, using another model',
            command=self.draw_new_job_load_model_window,
            width=35
        ).pack()

        tk.Button(
            main_frame,
            text='Edit existing job',
            command=quit,
            state=tk.DISABLED,
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

        tk.Button(
            main_frame,
            text='Run jobs (Linux only)',
            command=self.run_training,
            width=35
        ).pack()

        main_window.mainloop()
        self.main_window = main_window

    def draw_new_job_window(self):
        if self.new_job_window is not None:
            self.new_job_window = None

        new_job_window = tk.Tk()
        new_job_window.title("Create New Job - simple-text-generator")
        main_frame = tk.Frame(new_job_window)
        main_frame.grid()
        top_frame = tk.Frame(main_frame)
        bottom_frame = tk.Frame(main_frame)
        tk.Label(top_frame, text="Project Name:").grid(row=0, column=0)
        self.project_name = tk.Entry(top_frame)
        self.project_name.grid(row=0, column=1)

        tk.Button(bottom_frame, text='Cancel', command=self.back_new_job_window).grid(row=0, column=0)
        tk.Button(bottom_frame, text='Save New Job', command=self.save_new_job_window).grid(row=0, column=1)
        bottom_frame.grid()
        self.new_job_window = new_job_window

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
        tk.Label(model_frame, text="Temperatures to generate:").grid(row=3)
        self.temperatures_to_generate = tk.Entry(model_frame)
        self.temperatures_to_generate.grid(row=3, column=1)
        tk.Label(model_frame, text="Items to generate between generations:").grid(row=4)
        self.items_to_generate_between_generations = tk.Entry(model_frame)
        self.items_to_generate_between_generations.grid(row=4, column=1)
        tk.Label(model_frame, text="Generate every _ generations:").grid(row=5)
        self.generation_frequency = tk.Entry(model_frame)
        self.generation_frequency.grid(row=5, column=1)
        tk.Label(model_frame, text="Save model every _ generations:").grid(row=6)
        self.save_frequency = tk.Entry(model_frame)
        self.save_frequency.grid(row=6, column=1)
        tk.Label(model_frame, text="Items to generate at end:").grid(row=7)
        self.items_to_generate_at_end = tk.Entry(model_frame)
        self.items_to_generate_at_end.grid(row=7, column=1)

        # Set some sane defaults:
        self.number_of_iterations.insert(tk.END, 5)
        self.dropout.insert(tk.END, 0)
        self.temperatures_to_generate.insert(tk.END, "0.5, 1.0, 1.25")
        self.items_to_generate_between_generations.insert(tk.END, 50)
        self.generation_frequency.insert(tk.END, 1)
        self.save_frequency.insert(tk.END, 2)
        self.items_to_generate_at_end.insert(tk.END, 500)

        top_frame.grid(row=0, column=0)
        model_frame.grid(row=1, column=0)
        bottom_frame.grid(row=3, column=0)

    def draw_new_job_load_model_window(self):
        if self.new_job_load_model_window is not None:
            self.new_job_load_model_window = None

        new_job_load_model_window = tk.Tk()
        self.new_job_load_model_window = new_job_load_model_window
        new_job_load_model_window.title("Create New Job, Load Model - simple-text-generator")
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
        tk.Label(model_frame, text="Training file").grid(row=0, column=0)
        self.button_open_training_file = tk.Button(model_frame, text="Select a file",
                                                   command=self.set_training_file)
        self.button_open_training_file.grid(row=0, column=1)

        tk.Label(model_frame, text="Model file").grid(row=1, column=0)
        self.button_open_model_file = tk.Button(model_frame, text="Select a model file (.hdf5)",
                                                command=self.set_model_file)
        self.button_open_model_file.grid(row=1, column=1)

        tk.Label(model_frame, text="Number of iterations:").grid(row=2, column=0)
        self.number_of_iterations = tk.Entry(model_frame)
        self.number_of_iterations.grid(row=2, column=1)
        tk.Label(model_frame, text="Dropout (keep low, ~0-0.2):").grid(row=3)
        self.dropout = tk.Entry(model_frame)
        self.dropout.grid(row=3, column=1)
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

        # Set some sane defaults:
        self.number_of_iterations.insert(tk.END, 5)
        self.dropout.insert(tk.END, 0)
        self.temperatures_to_generate.insert(tk.END, "0.5, 1.0, 1.25")
        self.items_to_generate_between_generations.insert(tk.END, 50)
        self.generation_frequency.insert(tk.END, 1)
        self.save_frequency.insert(tk.END, 2)
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
            print(e)
            raise e

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
            print(e)
            raise e

    def render_config_file_text(self):
        with open('templates/config.yml.mustache', 'r') as f:
            return (chevron.render(f, {
                'priority': 0,
                'training_file': self.training_file,
                'number_of_iterations': self.number_of_iterations.get(),
                'dropout': self.dropout.get(),
                'training_data_percent': '0.75',
                'temperatures': map(str.strip, self.temperatures_to_generate.get().split(',')),
                'items_to_generate_between_iterations': self.items_to_generate_between_generations.get(),
                'generate_every_n_generations': self.generation_frequency.get(),
                'save_model_every_n_generations': self.save_frequency.get(),
                'items_to_generate_at_end': self.items_to_generate_at_end.get(),
                'model_to_load': f"m_{self.model_to_load}"
            }))

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
    def create_new_project_dir(path):
        if os.path.exists(path):
            messagebox.showerror(title="Error", message="Project already exists.")
            raise Exception("Project already exists. Dir: " + path)

        print("Creating dir: " + path)
        os.makedirs(path)

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

        label = tk.Label(training_window, text="Output of run.py")
        label.pack(fill=tk.X)

        # todo - find Windows solution
        xterm_frame = tk.Frame(training_window)
        xterm_frame.pack(fill=tk.BOTH, expand=True)

        xterm_frame_id = xterm_frame.winfo_id()

        try:
            # todo - sizing needs work.  bottom part of xterm remains hidden
            p = subprocess.Popen(
                ["xterm", "-into", str(xterm_frame_id), "-geometry", "120x40",
                 '-e', 'source env/bin/activate; python3.8 run.py'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                cwd="/home/tom/code/simple-text-generator")
        except FileNotFoundError:
            showwarning("Error", "xterm is not installed")
            raise SystemExit

        training_window.mainloop()


if __name__ == "__main__":
    window_manager = WindowManager()
    window_manager.draw_main_window()
