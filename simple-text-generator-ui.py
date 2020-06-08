import tkinter as tk
from time import sleep


class WindowManager:

    def __init__(self):
        self.main_window = None
        self.new_job_window = None
        self.number_of_iterations = None
        self.project_name = None
        self.dropout = None
        self.temperatures_to_generate = None
        self.items_to_generate_between_generations = None
        self.generation_frequency = None
        self.save_frequency = None
        self.items_to_generate_at_end = None

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
            self.new_job_window = None

        new_job_window = tk.Tk()
        main_frame = tk.Frame(new_job_window)
        main_frame.grid()
        top_frame = tk.Frame(main_frame)
        tk.Label(top_frame, text="Project Name").grid(row=0, column=0)
        self.project_name = tk.Entry(top_frame)
        self.project_name.grid(row=0, column=1)

        tk.Button(main_frame, text='Back', command=self.back_new_job_window).grid(row=5, column=0)
        tk.Button(main_frame, text='Save New Job', command=self.save_new_job_window).grid(row=5, column=1)
        self.new_job_window = new_job_window

        model_frame = tk.Frame(main_frame, relief="raised", borderwidth=3)
        model_frame.grid(row=1, column=0)
        tk.Label(model_frame, text="Training configuration").grid(row=0)
        tk.Label(model_frame, text="Number of iterations").grid(row=1, column=0)
        self.number_of_iterations = tk.Entry(model_frame)
        self.number_of_iterations.grid(row=1, column=1)
        tk.Label(model_frame, text="Dropout").grid(row=2)
        self.dropout = tk.Entry(model_frame)
        self.dropout.grid(row=2, column=1)
        tk.Label(model_frame, text="Temperatures to generate:").grid(row=3)
        self.temperatures_to_generate = tk.Entry(model_frame)
        self.temperatures_to_generate.grid(row=3, column=1)
        tk.Label(model_frame, text="Items to generate between generations:").grid(row=4)
        self.items_to_generate_between_generations = tk.Entry(model_frame)
        self.items_to_generate_between_generations.grid(row=4, column=1)
        tk.Label(model_frame, text="Generate every _ generations").grid(row=5)
        self.generation_frequency = tk.Entry(model_frame)
        self.generation_frequency.grid(row=5, column=1)
        tk.Label(model_frame, text="Save model every _ generations").grid(row=6)
        self.save_frequency = tk.Entry(model_frame)
        self.save_frequency.grid(row=6, column=1)
        tk.Label(model_frame, text="Items to generate at end:").grid(row=7)
        self.items_to_generate_at_end = tk.Entry(model_frame)
        self.items_to_generate_at_end.grid(row=7, column=1)

        top_frame.grid(row=0, column=0)
        model_frame.grid(row=1, column=0)
        # model_frame.pack()

    def back_new_job_window(self):
        print(self.number_of_iterations.get())
        # todo: save details somehow
        self.new_job_window.destroy()

    def save_new_job_window(self):
        # todo: save details somehow
        self.new_job_window.destroy()


if __name__ == "__main__":
    window_manager = WindowManager()
    window_manager.draw_main_window()
