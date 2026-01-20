import logging
import tkinter as tk
from typing import Callable, List, Tuple

from simpletextgenerator.ui import new_job, edit_job, training, archive_delete, generating_only_job

logger = logging.getLogger("ui")


class MenuWindow(tk.Tk):
    """Main menu window for the application."""

    def __init__(self):
        super().__init__()
        self.title('simple-text-generator')
        self.geometry("400x320")
        self.center_window()
        self._init_ui()

    def center_window(self):
        """Centers the window on the screen."""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def _init_ui(self):
        main_frame = tk.Frame(self)
        main_frame.pack(pady=10)

        buttons: List[Tuple[str, Callable]] = [
            ('Create new job', lambda: new_job.draw_new_job_window(self)),
            ('Create new jobs in batch', lambda: new_job.draw_new_batch_job_window(self)),
            ('Create new job, using another model', lambda: new_job.draw_new_job_load_model_window(self)),
            ('Generate text from model', lambda: generating_only_job.draw_generation_job_window(self)),
            ('Generate text from multiple models (batch)', lambda: generating_only_job.draw_generation_batch_job_window(self)),
            ('Edit existing job', lambda: edit_job.draw_edit_existing_job_window(self)),
            ('Archive, delete job', lambda: archive_delete.draw_archive_delete_window(self)),
            ('Run jobs (experimental)', lambda: training.create_training_window(self)),
        ]

        for text, command in buttons:
            tk.Button(
                main_frame,
                text=text,
                command=command,
                width=40
            ).pack(pady=2)


def draw_main_menu():
    """Entry point to draw the main menu."""
    menu_window = MenuWindow()
    menu_window.mainloop()
