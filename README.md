# Simple Text Generator
Simple Text Generator is a project to make it easy to train RNN on a set of text and generate similar text.

Built in python, utilizing the textgenrrn library (tensorflow).

## Usage
Tested on Ubuntu 16.04 with Python3.8.7.  (Windows needs retested)

### Set up environment

The following instructions are examples; adapt them for your needs.

Use requirements.txt for CPU-based training and requirements-gpu.txt for GPU-based training.  GPU training may require additional dependencies based on your system and OS.

####Linux:

~~~
git clone git@github.com:thtroyer/simple-text-generator.git
cd simple-text-generator
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt
~~~

####Windows:
Clone repository

Run the following in cmd after navigating to root of cloned directory:
~~~
py -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
~~~

### Running:

Utilize `simple-text-generator-ui.py` to configure a project to run.  Projects are created and viewable in the projects/ directory.

Once a project is created, run the project by using `train.py`.  The trained model is saved off at the interval configured.  `train.py` can be killed at any time and resumed later from the last saved model.

If you encounter errors when attempting to train, make sure your virtual environment is activated.

####Linux:
~~~
source env/bin/activate
python3 simple-text-generator-ui.py

python3 train.py
~~~

####Windows (cmd):
~~~
.\env\Scripts\activate
py simple-text-generator-ui.py

py train.py
~~~

### Features coming soon:

GUI (in progress)

Model export/import (in progress)

UI to archive project

Run training inside UI (in progress, Linux-only and buggy)

Generate data from model without more training

Update textgenrnn version
