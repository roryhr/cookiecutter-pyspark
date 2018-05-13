# Cookiecutter PySpark

Many of data science projects these days use Spark, and in particular the Python API.
This template is an attempt to make my life easier and a solicitation of best practices.

### Requirements to use the cookiecutter template:

-----------
 - Python 2.7 or 3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda install --channel conda-forge cookiecutter
```


### To start a new project, run:
------------

    cookiecutter https://github.com/roryhr/cookiecutter-pyspark


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── documentation      <- Put documentation here
│
├── notebooks          <- Jupyter notebooks
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── {{repo_name}}      <- Source code for use in this project.
│   └── __init__.py    <- Makes {{repo_name}} a Python module
└── tox.ini            <- tox file with settings for running tox; see tox.testrun.org
```

## Contributing

Feel free to contribute, fork this sucker, whatever...go nuts!

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests
