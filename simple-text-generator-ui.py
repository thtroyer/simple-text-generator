import tkinter as tk
from time import sleep


class WindowManager:

    def __init__(self):
        self.main_window = None
        self.new_job_window = None

    def draw_main_window(self):
        main_window = tk.Tk()
        main_window.geometry("150x150")
        main_frame = tk.Frame(main_window)
        main_frame.pack()
        new_project_button = tk.Button(
            main_frame,
            text='Create new job',
            command=self.draw_new_job_window
        )
        new_project_button.pack()

        edit_project_button = tk.Button(
            main_frame,
            text='Edit existing job',
            command=quit
        )
        edit_project_button.pack()

        delete_job_button = tk.Button(
            main_frame,
            text='Delete job',
            command=quit
        )
        delete_job_button.pack()

        run_jobs_button = tk.Button(
            main_frame,
            text='Run jobs',
            command=quit
        )
        run_jobs_button.pack()
        main_window.mainloop()
        self.main_window = main_window

    def draw_new_job_window(self):
        if self.new_job_window is not None:
            self.new_job_window.destroy()
        new_job_window = tk.Tk()
        main_frame = tk.Frame(new_job_window)
        main_frame.pack()
        back_button = tk.Button(
            main_frame,
            text='Back',
            command=self.back_new_job_window
        )
        save_button = tk.Button(
            main_frame,
            text='Save New Job',
            command=self.save_new_job_window
        )
        back_button.pack()
        save_button.pack()
        self.new_job_window = new_job_window
        # todo: complete

    def back_new_job_window(self):
        # todo: save details somehow
        self.new_job_window.destroy()

    def save_new_job_window(self):
        # todo: save details somehow
        self.new_job_window.destroy()


if __name__ == "__main__":
    window_manager = WindowManager()
    window_manager.draw_main_window()
