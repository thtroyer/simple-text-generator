# Simple Text Generator
This repo will contain simple scripts built on top of RNN libaries like textgenrnn to make it easier and faster for me to generate data for myself.

## Usage
Testes on Ubuntu 16.04 and Python3.  Instructions require python3-venv package.

### Set up environment:
~~~
git clone git@github.com:thtroyer/simple-text-generator.git
cd simple-text-generator
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
~~~

### Running:

train.py will read from training_data.txt in the same directory.

~~~
python3 train.py
~~~

Model will show up as 'textgenrnn_weights.hdf5' and output as 'output.txt'.

If you run into issues executing, make sure your virtual environment is active (`source venv/bin/activate`).

