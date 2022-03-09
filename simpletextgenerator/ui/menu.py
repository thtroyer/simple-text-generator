import logging
import tkinter as tk

from simpletextgenerator.ui import new_job, edit_job, training, archive_delete, generating_only_job

logger = logging.getLogger("ui")


class MenuWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('simple-text-generator')
        self.geometry("400x300")
        main_frame = tk.Frame(self)
        main_frame.pack()
        tk.Button(
            main_frame,
            text='Create new job',
            command=new_job.draw_new_job_window,
            width=35
        ).pack()

        tk.Button(
            main_frame,
            text='Create new jobs in batch',
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
            text='Generate text from model',
            command=generating_only_job.draw_generation_job_window,
            width=35
        ).pack()

        tk.Button(
            main_frame,
            text='Generate text from multiple models (batch)',
            command=generating_only_job.draw_generation_batch_job_window,
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
            text='Archive, delete job',
            command=archive_delete.draw_archive_delete_window,
            width=35
        ).pack()

        tk.Button(
            main_frame,
            text='Run jobs (experimental)',
            command=training.create_training_window,
            width=35
        ).pack()


def draw_main_menu():
    menu_window = MenuWindow()
    menu_window.mainloop()
