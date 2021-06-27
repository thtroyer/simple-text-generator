import os
import shutil
import tkinter as tk

import logging

logger = logging.getLogger("ui")


def draw_archive_delete_window():
    draw_archive_delete_window = ArchiveDeleteWindow()
    draw_archive_delete_window.draw_archive_delete_window()


class ArchiveDeleteWindow:
    def __init__(self):
        self.selected_project_name = None
        self.archive_delete_window = None

        self.number_of_iterations = None
        self.project_name_edit_text = None
        self.dropout = None
        self.temperatures_to_generate = None
        self.items_to_generate_between_generations = None
        self.training_data_percent = None
        self.generation_frequency = None
        self.save_frequency = None
        self.items_to_generate_at_end = None
        self.button_open_training_file = None
        self.training_file = None
        self.training_file_origin_path = None
        self.model_to_load = None
        self.selected_project = ''

    def option_selected(self, selected_value):
        self.selected_project = selected_value
        self.project_name_select.config(text=selected_value)

    def archive_project(self):
        if self.selected_project_name.get() == '' or self.selected_project_name.get() == 'Select a project':
            return
        shutil.move(f"projects/{self.selected_project_name.get()}", f"projects/archive/{self.selected_project_name.get()}")
        self.selected_project_name.set("Select a project")
        # todo update options instead of destroying window
        self.destroy_window()

    def delete_project(self):
        if self.selected_project_name.get() == '' or self.selected_project_name.get() == 'Select a project':
            return
        shutil.rmtree(f"projects/{self.selected_project_name.get()}")
        self.selected_project_name.set("Select a project")
        self.destroy_window()

    def draw_archive_delete_window(self):
        if self.archive_delete_window is not None:
            self.archive_delete_window = None

        archive_delete_window = tk.Tk()
        archive_delete_window.title("Edit existing job - simple-text-generator")
        main_frame = tk.Frame(archive_delete_window)
        main_frame.grid()
        top_frame = tk.Frame(main_frame)
        bottom_frame = tk.Frame(main_frame)
        option_list = self.get_projects_from_disk()
        self.selected_project_name = tk.StringVar(archive_delete_window)
        self.selected_project_name.set("Select a project")
        self.project_name_select = tk.OptionMenu(
            top_frame,
            self.selected_project_name,
            *option_list
        )

        self.project_name_select.config(width=50)
        self.project_name_select.grid(row=0, column=1)

        tk.Button(bottom_frame, text='Cancel', command=self.destroy_window).grid(row=0, column=0)
        tk.Button(bottom_frame, text='Archive', command=self.archive_project).grid(row=0, column=1)
        tk.Button(bottom_frame, text='Delete', command=self.delete_project).grid(row=0, column=2)
        bottom_frame.grid()
        self.archive_delete_window = archive_delete_window

        top_frame.grid(row=0, column=0)
        bottom_frame.grid(row=2, column=0)

    def get_projects_from_disk(self):
        project_path = 'projects/'
        project_list = []
        for path in os.listdir(project_path):
            if os.path.isdir(os.path.join(project_path, path)):
                project_list.append(path)

        project_list.remove("archive")
        return project_list

    def destroy_window(self):
        if self.archive_delete_window is not None:
            self.archive_delete_window.destroy()
