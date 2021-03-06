import yaml
import os
import shutil

from simpletextgenerator import training
from simpletextgenerator import job

project_dir = "./projects"
to_run_dir = "to_run"
output_dir = "output"


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


def create_jobs(dirs):
    new_jobs = []
    project_root_path = os.path.abspath(project_dir)
    for project in dirs:
        project_name = os.path.basename(project)
        if project_name == 'archive':
            continue
        try:
            with open(project + "/config.yaml", 'r') as config:
                config_data = yaml.safe_load(config)
            with open(project + "/state.yaml", 'r') as state:
                state_data = yaml.safe_load(state)
        except FileNotFoundError:
            print(f"Missing config.yaml or state.yaml. Skipping {project} directory")
            continue
        new_jobs.append(job.Job(config_data, state_data, project_root_path, project_name, to_run_dir, output_dir))
    return new_jobs


def sort_jobs(jobs_to_sort):
    jobs_to_sort.sort(key=lambda x: x.priority, reverse=True)


def train(jobs):
    for job_to_train in jobs:
        training_model = training.Train(job_to_train)
        training_model.run()


if __name__ == "__main__":
    project_dirs = [f.path for f in os.scandir(project_dir) if f.is_dir()]
    jobs_to_run = create_jobs(project_dirs)

    print("")
    print('Found ' + str(len(jobs_to_run)) + " projects to train.")
    print("")
    if (len(jobs_to_run) == 0):
        print('')
        print('------------------------------------')
        print("No projects found for training.  Ctrl+c to exit terminal.")
        exit(0)

    sort_jobs(jobs_to_run)
    train(jobs_to_run)

    print('')
    print('------------------------------------')
    print("All done.  Ctrl+c to exit terminal.")
    input()

