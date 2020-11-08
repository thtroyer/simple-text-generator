# Simple Text Generator
Simple Text Generator is a project to make it easy to train RNN on a set of text and generate similar text.

Built in python, utilizing the textgenrrn library (tensorflow).

## Example usage

todo

## Usage
Tested on Ubuntu 16.04 with Python3.5 and Windows with Python 3.7.7.  Instructions require python3-venv package.

### Set up environment
####Linux:
~~~
git clone git@github.com:thtroyer/simple-text-generator.git
cd simple-text-generator
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
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

Once a project is created, run the project by using `run.py`.  The trained model is saved off at the interval configured.  `run.py` can be killed at any time and resumed later from the last saved model.

To run, make sure you are in the virtual environment.

####Linux:
~~~
source env/bin/activate
python3 simple-text-generator-ui.py

python3 run.py
~~~

####Windows (cmd):
~~~
.\env\Scripts\activate
py simple-text-generator-ui.py

py run.py
~~~

### Features coming soon:

GUI (in progress)

Model export/import (in progress)

UI to archive project

Run training inside UI

Generate data from model without more training
