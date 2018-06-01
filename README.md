# Cookiecutter PySpark

Many of data science projects these days use Spark, and in particular the Python API.
This template is a guide for structuring your Spark project.

## Getting Started

``` bash
$ pip install cookiecutter
$ cookiecutter https://github.com/roryhr/cookiecutter-pyspark
```

### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── README.md          <- The top-level README for developers using this project.
├── documentation      <- Put documentation here
├── notebooks          <- Jupyter notebooks
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
├── {{repo_name}}      <- Source code for use in this project.
│   └── __init__.py    <- Makes {{repo_name}} a Python module
```

## Contributing

Feel free to contribute, fork this sucker, whatever...go nuts!

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests
