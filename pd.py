"""Move data to a database with pandas

Script demonstrating how to move data from a CSV file to a database
using pandas.

"""

import pandas as pd
import sqlalchemy


df = pd.read_csv(
    filepath_or_buffer="AB_NYC_2019.csv",
    header=0,
    index_col="id",
    quotechar='"',
    parse_dates=["last_review"],
)

# Optionally summarise df
# print(df.shape)
# print(df.info())
# print(df.isnull().sum())

engine = sqlalchemy.create_engine("sqlite:///ab_nyc.sqlite3")

with engine.connect() as connection:
    df.to_sql(
        name="listings_pandas",
        con=connection,
        if_exists="replace",
        index=True,
        index_label="id",
        dtype={"last_review": sqlalchemy.Date},
    )
