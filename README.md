# Cookiecutter Data Science

Opinionated data science project template.


Usage
------------

Install `cookiecutter`, see [https://github.com/audreyr/cookiecutter](https://github.com/audreyr/cookiecutter)

On Mac

```sh
brew install cookiecutter
```

Or with `pip`

```sh
pip install cookiecutter
```

Create a data science project

```sh
cookiecutter https://github.com/yaojiach/cookiecutter-data-science.git
```


Project Structure
------------

```
    .
    ├── .env               <- If you choose `dotenv` as config_type, it is included in .gitignore
    ├── .gitignore
    ├── LICENSE
    ├── Pipfile            <- If you choose `pipenv` as venv_type
    ├── README.rst
    ├── configs            <- If you choose `configs` as config_type, it is included in .gitignore
    │   └── README.rst
    ├── data
    │   ├── processed
    │   └── raw
    ├── docs               <- Minimal Sphinx template
    │   ├── Makefile
    │   ├── conf.py
    │   ├── index.rst
    │   ├── make.bat
    │   └── readme.rst
    ├── models             <- Your can store txt/binary/pickle model files here
    ├── notebooks          <- For jupyter notebooks
    ├── outputs            <- You can store model outputs, visualizations here
    │   ├── figures
    │   └── tables
    ├── references         <- You can store your reference literature here
    ├── requirements.txt   <- If you choose `venv` as venv_type
    ├── setup.py           <- Use `pip install` if you want to package it
    └── src
        ├── __init__.py
        ├── featurizer
        │   └── __init__.py
        ├── modeler
        │   └── __init__.py
        ├── predictor
        │   └── __init__.py
        └── visualizer
            └── __init__.py
```
