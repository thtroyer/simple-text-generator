import inquirer
import yaml
import os
import shutil
from simpletextgenerator import training

project_dir = "./projects"
to_run_dir = "to_run"
output_dir = "output"
incoming_file_folder = "incoming_training_files"


def main_activity_question():
    activity_question = [
      inquirer.List(
          'activity',
          message="What would you like to do?",
          choices=['Create training job.', 'Run training jobs.', 'Create additional output from model.']
      ),
    ]
    answer = inquirer.prompt(activity_question)
    print(answer)

    if answer['activity'] == 'Create training job.':
        #todo select which input file
        questions = [
            inquirer.Text(
                'num_loops',
                message="How many iterations to train?",
                default="10"),
            inquirer.Text(
                'temperatures',
                message="What temperatures to generate?",
                default="0.6, 0.8, 1.0"),
            inquirer.Text(
                'generate_every_n_generations',
                message="While training, how many iterations between generating output?",
                default="1"),
            inquirer.Text(
                'items_to_generate_between_generations',
                message="How many to generate?",
                default="50"),
            inquirer.Text(
                'save_model_every_n_generations',
                message="How many iterations between saving model?",
                default="5"),
            inquirer.Text(
                'items_to_generate_at_end',
                message="After last iteration, how many items to generate?",
                default="500"),

            # inquirer.Text('phone', message="What's your phone number",
            #               validate=lambda _, x: re.match('\+?\d[\d ]+\d', x),
            #               )
        ]
        answers = inquirer.prompt(questions)
        print(answers)
        #todo create yaml


main_activity_question()


# ########### FROM run.py below ##########


def create_project_from_files(input_files):
    for file in input_files:
        file_name = os.path.basename(file)
        if file_name == ".gitignore":
            continue
        new_project_name = os.path.splitext(file_name)[0]
        # todo increment new_project_dir if it exists in to_run or output
        new_project_dir = project_dir + "/" + to_run_dir + "/" + new_project_name
        os.mkdir(new_project_dir)
        os.rename(file, new_project_dir + "/input.txt")
        shutil.copyfile("config_defaults.yaml", new_project_dir + "/config.yaml")


def create_jobs(project_dirs):
    jobs = []
    project_root_path = os.path.abspath(project_dir)
    for project in project_dirs:
        project_name = os.path.basename(project)
        stream = open(project + "/config.yaml", 'r')
        config = yaml.load(stream)
        jobs.append(training.Job(config, project_root_path, project_name, to_run_dir, output_dir))
    return jobs


def sort_jobs(jobs):
    jobs.sort(key=lambda x: x.priority, reverse=True)
    return jobs


def train(jobs):
    for job in jobs:
        input_job_folder = project_dir + "/" + to_run_dir + "/" + job.job_name
        output_job_folder = project_dir + "/" + output_dir + "/" + job.job_name
        os.rename(input_job_folder, output_job_folder)
        train = training.Train(job)
        train.run()


incoming_flat_files = [f.path for f in os.scandir(incoming_file_folder) if not f.is_dir()]
create_project_from_files(incoming_flat_files)
project_dirs = [f.path for f in os.scandir(project_dir + "/" + to_run_dir) if f.is_dir()]
jobs = create_jobs(project_dirs)
sorted_jobs = sort_jobs(jobs)
train(sorted_jobs)

