# Simple Text Generator
Simple python application built on top of textgenrnn to make it easier and faster to generate output text that mimics the input it was trained on.
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

Drop files to train on into 'incoming_training_files' folder and execute run.py.  

Results will show up in projects/output/(file_name).

Make sure you are in the virtual environment.

####Linux:
~~~
source env/bin/activate
python3 run.py
~~~

####Windows (cmd):
~~~
.\env\Scripts\activate
py run.py
~~~

### Features coming soon:

GUI

Model export/import

