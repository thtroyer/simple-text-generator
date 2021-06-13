import asyncio
import contextlib
import os
import locale
import threading
import tkinter
import tkinter as tk
from time import sleep
from tkinter.scrolledtext import ScrolledText


def create_training_window():
    TrainingRunner().begin_work()
    # subprocess_protocol = SubprocessProtocol()
    # subprocess_protocol.run_training()


class TrainingRunner:
    def __init__(self):
        pass
        # self.training_window = TrainingWindow()
        # self.training_window.draw_training_window()

    def fire_training(self, loop):
        asyncio.set_event_loop(loop)
        subprocess_protocol = SubprocessProtocol()
        # subprocess_protocol.run_training(self.training_window)
        subprocess_protocol.run_training()

    def begin_work(self):
        loop = asyncio.new_event_loop()
        threading.Thread(target=self.fire_training, daemon=True, args=[loop]).start()


class TrainingWindow:
    def __init__(self):
        self.autoscroll = tkinter.IntVar()
        self.set_training_file = None
        self.save_training_window = None
        self.back_training_window = None
        self.training_window = None
        self.text_area = None

    def toggle_autoscroll(self):
        # todo
        pass

    def draw_training_window(self):
        if self.training_window is not None:
            self.training_window = None

        training_window = tk.Tk()
        training_window.title("Create New Job - simple-text-generator")
        main_frame = tk.Frame(training_window)
        main_frame.grid()
        top_frame = tk.Frame(main_frame)
        tk.Label(top_frame, text="Project Name:").grid(row=0, column=0)
        self.project_name = tk.Label(top_frame)
        self.project_name.grid(row=0, column=1)

        text_frame = tk.Frame(main_frame)
        text_area = ScrolledText(
            text_frame,
            wrap=tk.WORD,
            width=80,
            height=40,
            font=("Helvetica", 10),
            state='normal'
        )
        text_area.grid(row=0, column=0)

        text_area.insert(tk.END, "bork")
        text_area.config(state='disabled')
        text_area.see(tk.END)
        self.text_area = text_area

        text_area.grid(column=0, pady=20, padx=20)

        tk.Label(text_frame, text="Autoscroll:").grid(row=1, column=0)
        tk.Checkbutton(
            text_frame,
            text="Autoscroll:",
            command=self.toggle_autoscroll,
            variable=self.autoscroll,
            state='disabled'  # enable when feature set up
        ).grid(row=1, column=0)

        status_frame = tk.Frame(main_frame)

        top_frame.grid(row=0, column=0)
        text_frame.grid(row=1, column=0)
        status_frame.grid(row=2, column=0)

    def add_text(self, text):
        self.text_area.insert(tkinter.END, text)


class SubprocessProtocol(asyncio.SubprocessProtocol):
    training_window = None

    def __init__(self):
        self._exited = False
        self._closed_stdout = False
        self._closed_stderr = False
        self.loop = None
        self.training_window = None

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
        SubprocessProtocol.training_window.add_text(text.strip)

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
        training_window = TrainingWindow()
        training_window.draw_training_window()
        SubprocessProtocol.training_window = training_window
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

            self.loop.run_forever()
