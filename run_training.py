import logging
import os
import pathlib
import shutil
import tensorflow
import sys

from simpletextgenerator import training, jobs_util
from simpletextgenerator.jobs_util import resource_path
from simpletextgenerator.logging_setup import setup_logging

# the following unused import is needed for pyinstaller to build correctly
import sklearn.utils._weight_vector

# Helps prevent a crash I was getting.  #todo evaluate
try:
    gpus = tensorflow.config.experimental.list_physical_devices('GPU')
    tensorflow.config.experimental.set_memory_growth(gpus[0], True)
except IndexError as ignored:
    pass


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
        pathlib.Path(new_project_dir).mkdir(exist_ok=True)
        os.rename(file, new_project_dir + "/" + new_project_name + ".txt")
        shutil.copyfile(resource_path("templates/config_defaults.yaml"), new_project_dir + "/templates.yaml")


def create_jobs(dirs) -> list:
    new_jobs = []
    for project in dirs:
        try:
            new_job = jobs_util.create_job(project)
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
        training_model = training.Train(job_to_train, logger)
        training_model.run()


if __name__ == "__main__":
    pathlib.Path('logs').mkdir(exist_ok=True)
    logger = logging.getLogger("ui")
    if not logger.hasHandlers():
        log_file_name = "logs/simple-text-generator-run_training.log"
        previous_log_file_name = "logs/simple-text-generator-run_training_previous.log"
        logger = logging.getLogger("training")
        setup_logging(logger, log_file_name, previous_log_file_name)

    project_dirs = [f.path for f in os.scandir(project_dir) if f.is_dir()]
    jobs_to_run = create_jobs(project_dirs)

    logger.info("")
    logger.info('Found ' + str(len(jobs_to_run)) + " projects to train.")
    logger.info("")
    if (len(jobs_to_run) == 0):
        logger.info('')
        logger.info('------------------------------------')
        logger.info("No projects found for training.  Ctrl+c to exit terminal.")
        sys.exit(0)

    sort_jobs(jobs_to_run)
    train(jobs_to_run)

    logger.info('')
    logger.info('------------------------------------')
    logger.info("All done.  Ctrl+c to exit terminal.")
    input()
