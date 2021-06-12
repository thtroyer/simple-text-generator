# Simple Text Generator
Simple Text Generator is a project to make it easy to train RNN on a set of text and generate similar text.

Built in python, using the textgenrrn library (tensorflow).

## Usage
Tested on Ubuntu 18.04 with Python 3.8.10 and Windows 10 with Python 3.7.7.


## Set up environment

The following instructions are examples; adapt them for your needs.

Requires:

 - <= Python 3.8 (not sure earliest version) due to Tensorflow incompatibilities with Python 3.9+ right now.
 - pipenv  See https://pypi.org/project/pipenv/
 - Optional Tensorflow CUDA libraries for GPU training.  CPU training is used otherwise.

### Linux:
(Mac and Windows should be very similar with pipenv)

~~~
git clone git@github.com:thtroyer/simple-text-generator.git
cd simple-text-generator
pipenv install Pipfile

# run the executable code
python simple-text-generator-iu.py
python run_training.py
~~~

## Running:

Utilize `simple-text-generator-ui.py` to configure a project to run.  Projects are created and viewable in the projects/ directory.

Once a project is created, run the project by using `run_training.py`.  The trained model is saved off at the interval configured.  `run_training.py` can be killed at any time and resumed later from the last saved model.

## Features coming soon:

GUI (in progress)

Model export/import (in progress)

UI to archive project

Run training inside UI.

Generate data from model without more training
