#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def remove_folder(filepath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))

if __name__ == '__main__':

    if '{{ cookiecutter.venv_type }}' != 'pipenv':
        remove_file('Pipfile')

    if '{{ cookiecutter.venv_type }}' != 'venv':
        remove_file('requirements.txt')
    
    if '{{ cookiecutter.config_type }}' != 'dotenv':
        remove_file('.env')

    if '{{ cookiecutter.config_type }}' != 'configs':
        remove_folder('configs')
