import yaml
import os
from simpletextgenerator import training

project_folder = "./projects"
input_folder = "to_run"
output_folder = "output"

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

