import pandas as pd


def preprocess_data(df):
    """
    Preprocesses the input DataFrame:
    - converts date columns to datetime

    Args:
        df (pd.DataFrame): Raw input DataFrame

    Returns:
        pd.DataFrame: Preprocessed DataFrame
    """
    df = df.copy()

    df[["observation_date", "date_of_introduction"]] = df[
        ["observation_date", "date_of_introduction"]
    ].apply(pd.to_datetime)

    return df
