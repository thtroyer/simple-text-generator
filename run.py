import yaml
import os
import shutil
from simpletextgenerator import training

project_folder = "./projects"
input_folder = "to_run"
output_folder = "output"

#todo clean this up
incoming_file_folder = "input"
input_files = [f.path for f in os.scandir(incoming_file_folder) if not f.is_dir()]
for file in input_files:
    file_name = os.path.basename(file)
    if file_name == ".gitignore":
        continue
    new_project_name = os.path.splitext(file_name)[0]
    #todo increment new_project_dir if it exists in to_run or output
    new_project_dir = project_folder + "/" + input_folder + "/" + new_project_name
    os.mkdir(new_project_dir)
    os.rename(file, new_project_dir + "/input.txt")
    shutil.copyfile("config_defaults.yaml", new_project_dir + "/config.yaml")

dirs = [f.path for f in os.scandir(project_folder + "/" + input_folder) if f.is_dir()]
print(dirs)

jobs = []
project_root_path = os.path.abspath(project_folder)

for project in dirs:
    project_name = os.path.basename(project)
    stream = open(project + "/config.yaml", 'r')
    config = yaml.load(stream)
    jobs.append(training.Job(config, project_root_path, project_name, input_folder, output_folder))

jobs.sort(key=lambda x: x.priority, reverse=True)

for job in jobs:
    input_job_folder = project_folder + "/" + input_folder + "/" + job.job_name
    output_job_folder = project_folder + "/" + output_folder + "/" + job.job_name
    os.rename(input_job_folder, output_job_folder)
    train = training.Train(job)
    train.run()

