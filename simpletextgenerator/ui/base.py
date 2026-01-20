import tkinter as tk
from tkinter import filedialog, messagebox
import logging
import os
from pathlib import Path
from typing import Optional, Callable, Dict, Any, List

logger = logging.getLogger("ui")

class BaseWindow(tk.Toplevel):
    """Base class for all secondary windows in the application."""

    def __init__(self, parent: tk.Tk, title: str):
        super().__init__(parent)
        self.title(title)
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        # Center the window
        self.geometry("+%d+%d" % (parent.winfo_rootx() + 50, parent.winfo_rooty() + 50))

    def on_close(self):
        self.destroy()

    @staticmethod
    def open_file_dialog(title: str, filetypes: List[tuple]) -> str:
        home = os.path.expanduser('~')
        return filedialog.askopenfilename(
            initialdir=home,
            title=title,
            filetypes=filetypes
        )

    @staticmethod
    def open_files_dialog(title: str, filetypes: List[tuple]) -> List[str]:
        home = os.path.expanduser('~')
        return filedialog.askopenfilenames(
            initialdir=home,
            title=title,
            filetypes=filetypes
        )

    def show_error(self, message: str):
        messagebox.showerror(title="Error", message=message, parent=self)


class JobConfigForm(tk.Frame):
    """Reusable form for job configuration."""

    def __init__(self, parent, show_fields: Optional[List[str]] = None):
        super().__init__(parent, relief="raised", borderwidth=3)
        self.fields: Dict[str, Any] = {}
        self.row_counter = 0
        self.show_fields = show_fields if show_fields else []
        self._init_ui()

    def _init_ui(self):
        # Define all potential fields
        # (Label text, key, default value)
        potential_fields = [
            ("Number of iterations:", "num_iterations", "5"),
            ("Dropout (keep low, ~0-0.2):", "dropout", "0"),
            ("Training Data Percent, 0-1.0):", "training_data_percent", "0.75"),
            ("Temperatures to generate:", "temperatures", "0.5, 1.0, 1.25"),
            ("Items to generate between generations:", "items_between", "50"),
            ("Generate every _ generations:", "gen_frequency", "1"),
            ("Save model every _ generations:", "save_frequency", "2"),
            ("Items to generate at end:", "items_at_end", "500"),
        ]

        for label_text, key, default_val in potential_fields:
            if not self.show_fields or key in self.show_fields:
                self.add_entry(label_text, key, default_val)

    def add_entry(self, label_text: str, key: str, default_value: str = ""):
        tk.Label(self, text=label_text).grid(row=self.row_counter, column=0, sticky='e')
        entry = tk.Entry(self)
        entry.grid(row=self.row_counter, column=1, sticky='w')
        if default_value:
            entry.insert(tk.END, default_value)
        self.fields[key] = entry
        self.row_counter += 1

    def add_file_selector(self, label_text: str, key: str, command: Callable, button_text="Select a file"):
        tk.Label(self, text=label_text).grid(row=self.row_counter, column=0, sticky='e')
        btn = tk.Button(self, text=button_text, command=command)
        btn.grid(row=self.row_counter, column=1, sticky='w')
        self.fields[key] = btn
        self.row_counter += 1

    def get_value(self, key: str) -> str:
        if key in self.fields:
            widget = self.fields[key]
            if isinstance(widget, tk.Entry):
                return widget.get()
            elif isinstance(widget, tk.Button):
                return widget['text']
        return ""

    def set_value(self, key: str, value: str):
        if key in self.fields:
            widget = self.fields[key]
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)
                widget.insert(tk.END, str(value))
            elif isinstance(widget, tk.Button):
                widget['text'] = str(value)
