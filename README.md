# simple-text-generator
Tensorflow + textgenrnn based scripts to make playing with machine learning easier.

## Usage
Example usage for an Ubuntu AWS non-GPU instance:

Update and install dependencies/utilities:
~~~
sudo apt update
sudo apt -y upgrade
sudo apt -y install htop tig git tmux vim python3 python3-pip python3-venv
~~~

Set up environment:
~~~
cd /home/ubuntu
python3 -m venv tf
cd tf
source bin/activate
pip3 install tensorflow textgenrnn
~~~

To run, copy data into tf folder as training_data.txt.  Make sure environment is active and run.  

~~~
cd /home/ubuntu/tf
source bin/activate
python3 train.py
~~~

Model will show up as 'textgenrnn_weights.hdf5' and output as 'output.txt'.

