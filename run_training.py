import os
import shutil
import tensorflow
import sys

from simpletextgenerator import training, jobs_util
from simpletextgenerator.jobs_util import resource_path
from simpletextgenerator.models import job

# the following unused import is needed for pyinstaller to build correctly
import sklearn.utils._weight_vector

# Helps prevent a crash I was getting.  #todo evaluate
gpus = tensorflow.config.experimental.list_physical_devices('GPU')
tensorflow.config.experimental.set_memory_growth(gpus[0], True)

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
        shutil.copyfile(resource_path("templates/config_defaults.yaml"), new_project_dir + "/templates.yaml")


def create_jobs(dirs) -> list:
    new_jobs = []
    for project in dirs:
        try:
            new_job = jobs_util.create_job(project, project_dir)
            new_jobs.append(new_job)
        except RuntimeError:
            continue
        except FileNotFoundError:
            continue
    return new_jobs


def sort_jobs(jobs_to_sort):
    jobs_to_sort.sort(key=lambda x: x.config.priority, reverse=True)


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
        sys.exit(0)

    sort_jobs(jobs_to_run)
    train(jobs_to_run)

    print('')
    print('------------------------------------')
    print("All done.  Ctrl+c to exit terminal.")
    input()
