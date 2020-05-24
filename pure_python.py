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
