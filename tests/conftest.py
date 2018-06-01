import pyspark
import pytest
from pathlib import Path


@pytest.fixture(scope='session')
def spark():
    """Create a local Spark Session for testing"""

    conf = (pyspark.SparkConf()
        .setMaster('local[2]')
        .set('spark.cores.max', 2)
        .set('spark.driver.memory', '2G')
        .setAppName('Tests')
    )

    spark = (pyspark.sql
        .SparkSession.builder
        .config(conf=conf)
        .getOrCreate()
    )

    return spark

@pytest.fixture(scope='session')
def data_dir():
    return Path('.') / 'tests' / 'data' 
