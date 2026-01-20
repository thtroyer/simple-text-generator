import logging
import os
import shutil
import tkinter as tk
from tkinter.messagebox import askyesno
from typing import List, Optional

from simpletextgenerator.ui.base import BaseWindow

logger = logging.getLogger("ui")


def draw_archive_delete_window(parent):
    ArchiveDeleteWindow(parent)


class ArchiveDeleteWindow(BaseWindow):
    def __init__(self, parent):
        super().__init__(parent, "Archive/Delete job - simple-text-generator")

        self.selected_project_name: Optional[tk.StringVar] = None
        self.project_name_select: Optional[tk.OptionMenu] = None
        self._init_ui()

    def _init_ui(self):
        main_frame = tk.Frame(self)
        main_frame.pack(padx=20, pady=20)

        top_frame = tk.Frame(main_frame)
        top_frame.pack(pady=10)

        option_list = self.get_projects_from_disk()
        self.selected_project_name = tk.StringVar(self)
        self.selected_project_name.set("Select a project")

        self.project_name_select = tk.OptionMenu(
            top_frame,
            self.selected_project_name,
            *option_list
        )
        self.project_name_select.config(width=40)
        self.project_name_select.pack()

        bottom_frame = tk.Frame(main_frame)
        bottom_frame.pack(pady=10)

        tk.Button(bottom_frame, text='Cancel', command=self.destroy).grid(row=0, column=0, padx=5)
        tk.Button(bottom_frame, text='Archive', command=self.archive_project).grid(row=0, column=1, padx=5)
        tk.Button(bottom_frame, text='Delete', command=self.delete_project).grid(row=0, column=2, padx=5)

    def get_projects_from_disk(self) -> List[str]:
        project_path = 'projects/'
        if not os.path.exists(project_path):
            os.makedirs(project_path)

        project_list = []
        for path in os.listdir(project_path):
            if os.path.isdir(os.path.join(project_path, path)):
                project_list.append(path)

        if "archive" in project_list:
            project_list.remove("archive")

        if len(project_list) == 0:
            project_list.append("No projects.")

        return project_list

    def archive_project(self):
        project = self.selected_project_name.get()
        if not project or project == 'Select a project' or project == "No projects.":
            return

        try:
            archive_dir = "projects/archive"
            if not os.path.exists(archive_dir):
                os.makedirs(archive_dir)

            shutil.move(f"projects/{project}", f"{archive_dir}/{project}")
            self.selected_project_name.set("Select a project")
            self.destroy()
        except Exception as e:
            logger.error(e)
            self.show_error(str(e))

    def delete_project(self):
        project = self.selected_project_name.get()
        if not project or project == 'Select a project' or project == "No projects.":
            return

        if askyesno(title='Delete confirmation', message='Are you sure you want to delete this project?', parent=self):
            try:
                shutil.rmtree(f"projects/{project}")
                self.selected_project_name.set("Select a project")
                self.destroy()
            except Exception as e:
                logger.error(e)
                self.show_error(str(e))
