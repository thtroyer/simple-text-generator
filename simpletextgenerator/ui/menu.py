import tkinter as tk

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

        # tk.Button(
        #     main_frame,
        #     text='Run jobs (Linux only, experimental)',
        #     command=self.run_training,
        #     width=35
        # ).pack()

        main_window.mainloop()
        self.main_window = main_window


def draw_main_menu():
    MenuWindow().draw_main_window()
