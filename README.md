# Simple Text Generator
Simple python application built on top of textgenrnn to make it easier and faster to generate data.
## Usage
Tested on Ubuntu 16.04 and Python3.5.  Instructions require python3-venv package.  Not currently tested on Windows.

### Set up environment:
~~~
git clone git@github.com:thtroyer/simple-text-generator.git
cd simple-text-generator
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
~~~

### Running:

Drop files to train on into 'incoming_training_files' folder and execute run.py.  

~~~
python3 run.py
~~~

Results will show up in projects/output/(file_name).

If you run into issues executing, make sure you've set up the environment correctly and that the virtual environment is active.

~~~
source venv/bin/activate
~~~

### Features coming soon:

Much better and easier configuration

Model export/import

