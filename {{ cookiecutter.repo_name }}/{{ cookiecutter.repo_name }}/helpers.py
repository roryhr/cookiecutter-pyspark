def rename_columns(df, prefix=None):
    """Prepend all column names with a prefix and return a new DataFrame

    Parameters
    ----------
    df : pyspark.sql.dataframe.DataFrame

    year : str
        Filter hard brake events by year. Return all if None.

    prefix : str
        Prefex to prepend to column names in df

    Returns
    -------
    prepended_df : pyspark.sql.dataframe.DataFrame
        Dataframe with new column names
    """
    if prefix is None:
        return df
    cols_to_rename = df.columns
    renamed_cols = [df[col].alias(prefix+col) for col in cols_to_rename]
    prepended_df = df.select(renamed_cols)
    return prepended_df