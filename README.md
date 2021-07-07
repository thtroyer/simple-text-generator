# Simple Text Generator
Create new text via machine learning of existing source material.  Uses Recurrent Neural Networks (RNN) using textgenrnn, tensorflow libraries.

Built in Python, using the textgenrrn library (tensorflow).

See the [milestones](https://github.com/thtroyer/simple-text-generator/milestones) page for work-in-progress and planned features.

Also see [CHANGELOG.md](https://github.com/thtroyer/simple-text-generator/blob/master/CHANGELOG.md) for project history.

## Releases 

There are Windows binaries available soon.  This is by far the easiest way to run simple-text-generator.  Created with PyInstaller, it includes all dependencies including Python.

## Development environment

The following instructions are examples; adapt them for your needs.

Requires:

 - <= Python 3.8 (not sure earliest version) due to Tensorflow incompatibilities with Python 3.9+ right now.
 - pipenv  See https://pypi.org/project/pipenv/
 - Optional Tensorflow CUDA libraries for GPU training.  CPU training is used otherwise.  Be warned that setup is not straightforward and I currently do not have instructions.

### Setup example in Linux
#### (Mac and Windows should be very similar with pipenv)

~~~
git clone git@github.com:thtroyer/simple-text-generator.git
cd simple-text-generator
pipenv install Pipfile

# run the executable code
python simple-text-generator-iu.py
python run_training.py
~~~

## Branches
Tagged releases will be the most stable. 

Features will often be created as feature branches and merged into master as they are completed. `master` branch will be the latest code and should be in mostly-working order.  Use this if you want the latest, but possibly less stable than the released version.

This project uses [semantic versioning](https://semver.org/).

## Contributing

As a developer primarily familiar with Java and PHP, this is currently my playground for learning Python and ML, which includes making mistakes and messes, and then figuring out improvements.

That said, I welcome contributions, bugfixes, and feedback for anyone interested in helping move this project along.  Try to keep any pull requests small and focused for easy review and acceptance.  Overly large changes will be slow to accept or rejected.

## Final thoughts

This code, especially in its current state, should not be used as reference, study, or as a measure of my typical code quality.  I'm currently aiming for functionality and learning, which requires some mucking around.  I hope to be able to take this disclaimer off soon as I become more familiar with Python idioms, architecture, syntax, and add some unit tests.

Until then, read the code at your own risk.  Here be dragons.
