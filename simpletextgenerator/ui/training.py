import asyncio
import contextlib
import os
import locale
import threading
import tkinter
import tkinter as tk
from queue import Queue
from tkinter.scrolledtext import ScrolledText


def create_training_window():
    TrainingRunner().begin_work()
    # subprocess_protocol = SubprocessProtocol(tk)
    # subprocess_protocol.run_training()


class TrainingRunner:
    def __init__(self):
        self.tk = tkinter
        # self.training_window = TrainingWindow(tk)
        # self.training_window.draw_training_window()

    def fire_training(self, loop, training_window, stdout_queue, stderr_queue):
        asyncio.set_event_loop(loop)

        subprocess_protocol = SubprocessProtocol(self.tk, training_window, stdout_queue, stderr_queue)
        # subprocess_protocol.run_training(self.training_window)
        subprocess_protocol.run_training()

    def begin_work(self):
        stdout_queue = Queue()
        stderr_queue = Queue()
        training_window = TrainingWindow(self.tk, stdout_queue, stderr_queue)
        training_window.draw_training_window()

        loop = asyncio.new_event_loop()
        threading.Thread(target=self.fire_training, daemon=True,
                         args=[loop, training_window, stdout_queue, stderr_queue]).start()


class TrainingWindow:
    def __init__(self, tk, stdout_queue, stderr_queue):
        self.autoscroll = tkinter.IntVar()
        self.set_training_file = None
        self.save_training_window = None
        self.back_training_window = None
        self.training_window = None
        self.text_area = None
        self.tk = tk
        self.stdout_queue = stdout_queue
        self.stderr_queue = stderr_queue

    def draw_training_window(self):
        if self.training_window is not None:
            self.training_window = None

        training_window = self.tk.Tk()
        self.training_window = training_window
        tk = self.tk
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
            width=100,
            height=30,
            font=("Terminal", 7),
            state='normal'
        )
        text_area.grid(row=0, column=0)
        self.text_area = text_area

        self.add_text("bork")
        self.add_text("bork2")
        self.add_text("bork3")
        # text_area.config(state='disabled')
        text_area.see(tk.END)

        text_area.grid(column=0, pady=20, padx=20)

        tk.Label(text_frame, text="Autoscroll:").grid(row=1, column=0)
        tk.Checkbutton(
            text_frame,
            text="Autoscroll:",
            variable=self.autoscroll
        ).grid(row=1, column=0)

        status_frame = tk.Frame(main_frame)

        top_frame.grid(row=0, column=0)
        text_frame.grid(row=1, column=0)
        status_frame.grid(row=2, column=0)
        self.periodic_callback()

    def add_text(self, text):
        print("found " + text)
        self.text_area.insert(tk.INSERT, text)
        self.text_area.insert(tk.INSERT, "\n")
        self.text_area.update_idletasks()
        self.training_window.update_idletasks()
        if self.autoscroll: # todo fix autoscroll
            self.text_area.see(tk.END)

    def process_text(self, text: str, type: str):
        #todo filter and update various UI elements
        self.add_text(f"{type}: {text}")

    def update_ui(self):
        while self.stdout_queue.qsize():
            try:
                msg = self.stdout_queue.get(0)
                self.process_text(msg, "stdout")
            # except Queue.Empty:
            except Exception as e:
                print(e)

        while self.stderr_queue.qsize():
            try:
                msg = self.stderr_queue.get(0)
                self.process_text(msg, "stderr")
            # except Queue.Empty:
            except Exception as e:
                print(e)

    def periodic_callback(self):
        self.update_ui()
        self.training_window.after(2000, self.periodic_callback)


class SubprocessProtocol(asyncio.SubprocessProtocol):
    training_window = None
    tk = None
    stdout_queue = None
    stderr_queue = None

    def __init__(self, tk=None, training_window=None, stdout_queue=None, stderr_queue=None):
        self._exited = False
        self._closed_stdout = False
        self._closed_stderr = False
        self.loop = None
        if tk is not None:
            SubprocessProtocol.tk = tk
        if training_window is not None:
            SubprocessProtocol.training_window = training_window
        if stdout_queue is not None:
            SubprocessProtocol.stdout_queue = stdout_queue
        if stderr_queue is not None:
            SubprocessProtocol.stderr_queue = stderr_queue

    @property
    def finished(self):
        return self._exited and self._closed_stdout and self._closed_stderr

    def signal_exit(self):
        if not self.finished:
            return
        self.loop.stop()

    def pipe_data_received(self, fd, data):
        text = data.decode(locale.getpreferredencoding(False))
        if fd == 1:
            # stdout
            SubprocessProtocol.stdout_queue.put(text.strip())
        elif fd == 2:
            # stderr
            SubprocessProtocol.stderr_queue.put(text.strip())

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
            self.loop = asyncio.ProactorEventLoop()
            asyncio.set_event_loop(self.loop)
        else:
            self.loop = asyncio.get_event_loop()

        with contextlib.closing(self.loop):
            transport = self.loop.run_until_complete(self.loop.subprocess_exec(
                SubprocessProtocol, 'python', 'simpletextgenerator/mock/mock_run_training.py'))[0]

            self.loop.run_forever()
