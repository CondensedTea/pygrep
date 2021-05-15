from os.path import dirname, join

from setuptools import find_packages, setup

setup(
    name='pygrep',
    description='Grep clone written in python3',
    version='1.0',
    author='Alex Tyshkevich',
    author_email='alex@tyshkevich.ru',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={'console_scripts': ['pygrep = pygrep.pygrep:run']},
)
