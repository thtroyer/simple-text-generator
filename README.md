# Simple Text Generator
Simple Text Generator is a project to make it easy to train RNN on a set of text and generate similar text.

Built in Python, using the textgenrrn library (tensorflow).

See the [milestones](https://github.com/thtroyer/simple-text-generator/milestones) page for work-in-progress and planned features.

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

## Releases and branches

End users should only use releases.  I aim to have some binary packages available soon, but in general, the releases will be the most stable and polished.

Features will often be created as feature branches and merged into master as they are completed.

`master` branch will be the latest code and should be in mostly-working order.  Use this if you want the latest, but possibly less stable than the released version.

Project uses [semantic versioning](https://semver.org/) for version numbers.

## Contributing

As a developer primarily familiar with Java and PHP, this is currently my playground for learning Python and ML, which includes making mistakes and messes, and then figuring out improvements.

That said, I welcome contributions, bugfixes, and feedback for anyone interested in helping move this project along.  Try to keep any pull requests small and focused for easy review and acceptance.  Overly large changes will be slow to accept or rejected.

## Final thoughts

This code, especially in its current state, should not be used as reference, study, or as a measure of my typical code quality.  I'm currently aiming for functionality and learning, which requires some mucking around.  I hope to be able to take this disclaimer off soon as I become more familiar with Python idioms, architecture, syntax, and add some unit tests.

Until then, read the code at your own risk.  Here be dragons.
