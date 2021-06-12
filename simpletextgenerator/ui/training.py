import asyncio
import contextlib
import os
import locale
import tkinter as tk


def create_training_window():
    TrainingWindow().draw_training_window()


class TrainingWindow:
    def __init__(self):
        self.set_training_file = None
        self.save_training_window = None
        self.back_training_window = None
        self.training_window = None

    def draw_training_window(self):
        if self.training_window is not None:
            self.training_window = None

        training_window = tk.Tk()
        training_window.title("Create New Job - simple-text-generator")
        main_frame = tk.Frame(training_window)
        main_frame.grid()
        top_frame = tk.Frame(main_frame)
        bottom_frame = tk.Frame(main_frame)
        tk.Label(top_frame, text="Project Name:").grid(row=0, column=0)
        self.project_name = tk.Entry(top_frame)
        self.project_name.grid(row=0, column=1)

        tk.Button(bottom_frame, text='Cancel', command=self.back_training_window).grid(row=0, column=0)
        tk.Button(bottom_frame, text='Save New Job', command=self.save_training_window).grid(row=0, column=1)
        bottom_frame.grid()
        self.training_window = training_window

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

        # Set some sane defaults:
        self.number_of_iterations.insert(tk.END, 5)
        self.dropout.insert(tk.END, 0)
        self.temperatures_to_generate.insert(tk.END, "0.5, 1.0, 1.25")
        self.items_to_generate_between_generations.insert(tk.END, 50)
        self.training_data_percent.insert(tk.END, "0.75")
        self.generation_frequency.insert(tk.END, 1)
        self.save_frequency.insert(tk.END, 2)
        self.items_to_generate_at_end.insert(tk.END, 500)

        top_frame.grid(row=0, column=0)
        model_frame.grid(row=1, column=0)
        bottom_frame.grid(row=3, column=0)
        # subprocess_protocol = SubprocessProtocol()
        # subprocess_protocol.run_training()


class SubprocessProtocol(asyncio.SubprocessProtocol):
    def __init__(self):
        self._exited = False
        self._closed_stdout = False
        self._closed_stderr = False
        self.loop = None

    @property
    def finished(self):
        return self._exited and self._closed_stdout and self._closed_stderr

    def signal_exit(self):
        if not self.finished:
            return
        self.loop.stop()

    def pipe_data_received(self, fd, data):
        name = ''
        if fd == 1:
            name = 'stdout'
        elif fd == 2:
            name = 'stderr'
        text = data.decode(locale.getpreferredencoding(False))
        print('Received from {}: {}'.format(name, text.strip()))

    def pipe_connection_lost(self, fd, exc):
        if fd == 1:
            self._closed_stdout = True
        elif fd == 2:
            self._closed_stderr = True
        self.signal_exit()

    def process_exited(self):
        self._exited = True
        self.signal_exit()

    def run_training(self):
        if os.name == 'nt':
            # On Windows, the ProactorEventLoop is necessary to listen on pipes
            self.loop = asyncio.ProactorEventLoop()
            asyncio.set_event_loop(self.loop)
        else:
            self.loop = asyncio.get_event_loop()

        with contextlib.closing(self.loop):
            transport = self.loop.run_until_complete(self.loop.subprocess_exec(
                # SubprocessProtocol, 'python', 'run_training.py'))[0]
                SubprocessProtocol, 'python', 'simpletextgenerator/mock/mock_run_training.py'))[0]
            # SubprocessProtocol, 'python', 'async_target.py'))[0]
            # SubprocessProtocol, 'python', '-c', 'print(\'Hello async world!\')'))[0]

            self.loop.run_forever()
