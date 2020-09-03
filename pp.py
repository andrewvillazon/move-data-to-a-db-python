import sqlite3
import csv


conn = sqlite3.connect("big_data.db")
curs = conn.cursor()

# Table setup
curs.execute(
    """
    CREATE TABLE IF NOT EXISTS pure_python (
        transaction_date TEXT,
        bban TEXT,
        color TEXT,
        phone_number TEXT,
        lat REAL,
        long REAL,
        age INT
    )
 """
)

# Remove any data from a previous run
curs.execute("DELETE FROM pure_python")
conn.commit()

# Read csv and INSERT each line
with open("big_data.csv", "r", encoding="utf-8") as csv_file:
    data_reader = csv.reader(csv_file, delimiter="|")
    next(data_reader)  # skip over header row if it has column names

    for row in data_reader:
        curs.execute("INSERT INTO pure_python VALUES(?,?,?,?,?,?,?)", row)

conn.commit()
conn.close()
