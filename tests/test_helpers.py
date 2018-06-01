from pyspark.sql import Row
from {{ cookiecutter.repo_name }} import helpers


def test_rename_columns(spark):
    df = spark.createDataFrame(
        data=[Row(name='Alice', age=1)],
        schema='name: string, age: int',
    )

    prepended_df = helpers.rename_columns(df, prefix='TEST_')
    prepended_cols = prepended_df.columns

    assert prepended_cols[0] == 'TEST_name'
    assert prepended_cols[1] == 'TEST_age'
