import asyncio
import collections
import contextlib
import os
import locale
import re
import sys
import threading
import tkinter
import tkinter as tk
from tkinter import ttk
from queue import Queue
from tkinter.scrolledtext import ScrolledText


# todo clean up this file

def create_training_window():
    TrainingRunner().begin_work()


class RunningMean:
    def __init__(self, max_number_of_elements=100):
        self.max_number_of_elements = max_number_of_elements
        self.number_of_elements = 0
        self.elements = collections.deque(maxlen=max_number_of_elements)

    def add(self, number):
        self.elements.append(number)

    def mean(self):
        total = 0
        num_elements = 0
        for i in self.elements:
            total += i
            num_elements += 1

        return round(total / num_elements, 3)


class TrainingRunner:
    def __init__(self):
        self.tk = tkinter

    def fire_training(self, loop, training_window, stdout_queue, stderr_queue):
        asyncio.set_event_loop(loop)

        subprocess_protocol = SubprocessProtocol(self.tk, training_window, stdout_queue, stderr_queue)
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
        self.is_autoscroll = True
        self.set_training_file = None
        self.save_training_window = None
        self.back_training_window = None
        self.training_window = None
        self.text_area = None
        self.tk = tk
        self.stdout_queue = stdout_queue
        self.stderr_queue = stderr_queue
        self.sub_progress_label = None
        self.sub_progress_eta = None
        self.sub_progress = None
        self.project_progress_label = None
        self.project_progress = None
        self.loss_label = None
        self.loss_value_label = None
        self.generation_label = None
        self.generation_value_label = None

        self.total_projects = 0
        self.projects_complete = 0
        self.running_mean_loss = RunningMean(10)
        self.running_mean_generation = RunningMean(100)

    def toggle_autoscroll(self):
        self.is_autoscroll = not self.is_autoscroll

    def draw_training_window(self):
        if self.training_window is not None:
            self.training_window = None

        training_window = self.tk.Tk()
        self.training_window = training_window
        tk = self.tk
        training_window.title("Training model - simple-text-generator")
        main_frame = tk.Frame(training_window)
        main_frame.grid()
        top_frame = tk.Frame(main_frame)
        self.project_name_label = tk.Label(top_frame)
        self.project_name_label.grid(row=0, column=0)

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

        text_area.grid(column=0, pady=20, padx=20)

        tk.Label(text_frame, text="Autoscroll").grid(row=1, column=0)
        checkbox = tk.Checkbutton(
            text_frame,
            text="Autoscroll",
            command=self.toggle_autoscroll,
        )
        checkbox.grid(row=1, column=0)
        checkbox.select()

        status_frame = tk.Frame(main_frame)
        status_frame.grid()
        self.sub_progress_label = tk.Label(status_frame, text="Progress")
        self.sub_progress_label.grid(row=0, column=0)
        self.sub_progress = ttk.Progressbar(status_frame, orient=tk.HORIZONTAL, maximum=100, length=300,
                                            mode='determinate')
        self.sub_progress.grid(row=0, column=1)
        self.sub_progress_eta = tk.Label(status_frame, text="ETA/Desc")
        self.sub_progress_eta.grid(row=1, column=1)

        self.loss_label = tk.Label(status_frame, text="Current loss: ")
        self.loss_label.grid(row=2, column=0)
        self.loss_value_label = tk.Label(status_frame, text="")
        self.loss_value_label.grid(row=2, column=1)

        self.generation_label = tk.Label(status_frame, text="Text generation speed: ")
        self.generation_label.grid(row=2, column=2)
        self.generation_value_label = tk.Label(status_frame, text="")
        self.generation_value_label.grid(row=2, column=3)

        # todo
        # self.project_progress_label = tk.Label(status_frame, text="Project progress")
        # self.project_progress_label.grid(row=3, column=0)
        # self.project_progress = ttk.Progressbar(status_frame, orient=tk.HORIZONTAL, maximum=100, length=300, mode='determinate')
        # self.project_progress.grid(row=3, column=1)
        self.project_progress_label = tk.Label(status_frame,
                                               text="This UI is a work in progress and not representative of final design.")
        self.project_progress_label.grid(row=3, column=0)

        top_frame.grid(row=0, column=0)
        text_frame.grid(row=1, column=0)
        status_frame.grid(row=2, column=0)
        self.periodic_callback()

    def add_text(self, text):
        text = text.encode("ascii", "ignore").decode()
        self.text_area.insert(tk.INSERT, text)
        self.text_area.insert(tk.INSERT, "\n")
        self.text_area.update_idletasks()
        self.training_window.update_idletasks()
        if self.is_autoscroll:
            self.text_area.see(tk.END)

    def is_progress_text(self, text):
        if self.is_progress_bar1(text):
            return True
        if self.is_progress_bar2(text):
            return True
        return False

    def is_progress_bar1(self, text):
        return (re.search(r"\d*\/\d*\ \[[\.=>]*\]", text)) is not None

    def is_progress_bar2(self, text):
        match1 = (re.search(r"\d*\.\d*s/it\]$", text)) is not None
        match2 = (re.search(r"\d*\.\d*it/s\]$", text)) is not None
        return match1 or match2

    def get_progress_text_bar1(self, text):
        pieces = text.split("\n")
        if pieces[0].find("[") == -1:
            return pieces[0]
        return pieces[0].split("-")[1]

    def get_progress_text_bar2(self, text):
        pieces = text.split("|")
        return pieces[2]

    def is_found_projects_statement(self, text):
        return (re.search(r"Found \d* projects to train\.", text)) is not None

    def is_saving_final_model(self, text):
        return (re.search(r"Saving final model", text)) is not None

    def process_text(self, text: str, type: str):
        if type == "stderr":
            print(text, file=sys.stderr)
        else:
            print(text, file=sys.stdout)

        if self.is_progress_text(text):
            if self.is_progress_bar1(text):
                percentage = self.get_percentage_bar1(text)
                eta_text = self.get_progress_text_bar1(text)
                loss_value = text.split("loss: ")[-1]
                if loss_value != '':
                    self.running_mean_loss.add(float(loss_value))
                self.loss_value_label.config(text=str(self.running_mean_loss.mean()))
                self.sub_progress_eta.config(text="Training model. " + eta_text)
            else:
                percentage = self.get_percentage_bar2(text)
                eta_text = self.get_progress_text_bar2(text)
                generation_text = eta_text.split(",  ")[-1].split("]")[0]
                if generation_text != '':
                    generation_value = float(generation_text[:-4])
                    if generation_text[-4:] == "s/it":
                        generation_value = 1 / generation_value
                    self.running_mean_generation.add(generation_value)
                items_per_second = self.running_mean_generation.mean()
                if items_per_second < 1:
                    seconds_per_item = round(1 / items_per_second, 3)
                    self.generation_value_label.config(text=str(seconds_per_item) + " sec/item")
                else:
                    self.generation_value_label.config(text=str(round(items_per_second, 3)) + " items/sec")
                self.sub_progress_eta.config(text="Generating text. " + eta_text)

            self.sub_progress["maximum"] = 100
            self.sub_progress["value"] = percentage
            return

        if type == "stderr":
            return

        # cleaning up some garbage characters
        text = str.replace(text, '\b', '')
        text = str.replace(text, '\r', '')

        if not text.strip():
            return

        if self.is_stray_ETA(text):
            return

        if self.is_found_projects_statement(text):
            pieces = text.split(" ")
            self.total_projects = int(pieces[1])
            if self.total_projects == 0:
                self.add_text("Found 0 projects to run.  Nothing to do.")
            self.update_project_label()
            return

        if self.is_saving_final_model(text):
            self.projects_complete += 1
            self.update_project_label()
            return

        self.add_text(text)

    def update_ui(self):
        while self.stdout_queue.qsize():
            try:
                msg = self.stdout_queue.get(0)
                self.process_text(msg, "stdout")
            except Exception as e:
                print(e)

        while self.stderr_queue.qsize():
            try:
                msg = self.stderr_queue.get(0)
                self.process_text(msg, "stderr")
            except Exception as e:
                print(e)

    def periodic_callback(self):
        self.update_ui()
        self.training_window.after(200, self.periodic_callback)

    def get_percentage_bar1(self, text) -> int:
        regex = re.compile(r"[^\.=>]")
        cleaned_string = regex.sub('', text)
        try:
            arrow_position = cleaned_string.index(">")
        except ValueError:
            return 0

        return int(
            (arrow_position / len(cleaned_string)) * 100
        )

    def get_percentage_bar2(self, text) -> int:
        pieces = text.split("%")
        return pieces[0]

    def update_project_label(self):
        current_project = self.projects_complete + 1
        self.project_name_label.config(text=f"Running {current_project} of {self.total_projects}")

        if (current_project > self.total_projects):
            self.project_name_label.config(text=f"Training and generation complete.")

    def is_stray_ETA(self, text):
        match1 = (re.search(r"^-\sETA:", text)) is not None
        match2 = (re.search(r"loss:\s\d*\.\d*$", text)) is not None
        return match1 and match2


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
        if self.loop:
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

        run_with_mock_data = os.environ.get('MOCK_UI_DATA')
        with contextlib.closing(self.loop):
            process = 'run_training.py'
            if run_with_mock_data is not None and run_with_mock_data:
                process = 'simpletextgenerator/mock/mock_run_training.py'

            transport = self.loop.run_until_complete(self.loop.subprocess_exec(SubprocessProtocol, 'python', process))[
                0]

            self.loop.run_forever()
