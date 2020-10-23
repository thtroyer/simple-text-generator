import yaml
import os
import shutil

from simpletextgenerator import training
from simpletextgenerator import job

project_dir = "./projects"
to_run_dir = "to_run"
output_dir = "output"
incoming_file_folder = "incoming_training_files"


def create_project_from_files(input_files):
    for file in input_files:
        file_name = os.path.basename(file)
        if file_name == ".gitignore":
            continue
        new_project_name = os.path.splitext(file_name)[0]
        new_project_dir = project_dir + "/" + to_run_dir + "/" + new_project_name
        os.mkdir(new_project_dir)
        os.rename(file, new_project_dir + "/" + new_project_name + ".txt")
        shutil.copyfile("templates/config_defaults.yaml", new_project_dir + "/templates.yaml")


def create_jobs(project_dirs):
    new_jobs = []
    project_root_path = os.path.abspath(project_dir)
    for project in project_dirs:
        project_name = os.path.basename(project)
        if project_name == 'archive':
            continue
        with open(project + "/config.yaml", 'r') as config:
            config_data = yaml.load(config)
        with open(project + "/state.yaml", 'r') as state:
            state_data = yaml.load(state)
        new_jobs.append(job.Job(config_data, state_data, project_root_path, project_name, to_run_dir, output_dir))
    return new_jobs


def sort_jobs(jobs):
    jobs.sort(key=lambda x: x.priority, reverse=True)
    return jobs


def train(jobs):
    for job in jobs:
        if job.status == 'completed':
            continue
        # input_job_folder = project_dir + "/" + to_run_dir + "/" + job.job_name
        # output_job_folder = project_dir + "/" + output_dir + "/" + job.job_name
        # os.rename(input_job_folder, output_job_folder)
        train = training.Train(job)
        train.run()


#todo: move this to standalone file
# incoming_flat_files = [f.path for f in os.scandir(incoming_file_folder) if not f.is_dir()]
# create_project_from_files(incoming_flat_files)

project_dirs = [f.path for f in os.scandir(project_dir) if f.is_dir()]
jobs = create_jobs(project_dirs)
sorted_jobs = sort_jobs(jobs)
train(sorted_jobs)

