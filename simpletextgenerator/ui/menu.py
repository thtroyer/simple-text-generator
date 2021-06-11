import subprocess
import tkinter as tk
from warnings import showwarning

from simpletextgenerator.ui import new_job, edit_job

class MenuWindow:
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

        tk.Button(
            main_frame,
            text='Run jobs (Linux only, experimental)',
            command=self.run_training,
            width=35
        ).pack()

        main_window.mainloop()
        self.main_window = main_window


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
            # p = subprocess.Popen(
            #     ["xterm", "-into", str(xterm_frame_id), "-geometry", "120x40",
            #      '-e', 'source env/bin/activate; python3.8 run_training.py'],
            #     stdin=subprocess.PIPE,
            #     stdout=subprocess.PIPE,
            #     cwd="/home/tom/code/simple-text-generator")
            p = subprocess.Popen(
                "python run_training.py",
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE
            )
        except FileNotFoundError:
            showwarning("Error", "xterm is not installed")
            raise SystemExit

        training_window.mainloop()


def draw_main_menu():
    MenuWindow().draw_main_window()


