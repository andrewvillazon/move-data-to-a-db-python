"""Move data to a database with Pure Python

Script demonstrating how to move data from a CSV file to a database
using just Python.

"""

import sqlite3
import csv


conn = sqlite3.connect("ab_nyc.sqlite3")
curs = conn.cursor()

# Table setup
curs.execute(
    """
    CREATE TABLE IF NOT EXISTS listings_pure_python (
        id INT,
        name TEXT,
        host_id INT,
        host_name TEXT,
        neighbourhood_group TEXT,
        neighbourhood TEXT,
        latitude REAL,
        longitude REAL,
        room_type TEXT,
        price INT,
        minimum_nights INT,
        number_of_reviews INT,
        last_review TEXT,
        reviews_per_month REAL,
        calculated_host_listings_count INT,
        availability_365 INT
    )
 """
)

# Remove any data from a previous run
curs.execute("DELETE FROM listings_pure_python")
conn.commit()

# Read csv and INSERT each line
with open("AB_NYC_2019.csv", "r", encoding="utf-8", newline="") as csv_file:
    data_reader = csv.reader(csv_file, quotechar='"')
    next(data_reader)  # skip over header row if it has column names

    for row in data_reader:
        curs.execute(
            "INSERT INTO listings_pure_python VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            row,
        )

conn.commit()
conn.close()
