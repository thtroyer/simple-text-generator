from setuptools import setup, find_packages

setup(
    name='simple-text-generator',
    version='0.3.0',
    # packages=['simpletextgenerator'],
    package=find_packages(),
    package_dir={'': 'tests'},
    url='github.com/thtroyer/simple-text-generator',
    license='MIT',
    author='thtroyer',
    author_email='tom.troyer@gmail.com',
    description='',
    install_requires=['textgenrnn', 'tensorflow==2.4.2', 'chevron', 'PyYAML', 'pipfile']
)
