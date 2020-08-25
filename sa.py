"""Move data to a database with SQLAlchemy

Script demonstrating how to move data from a CSV file to a database
using SQLAlchemy.

"""

import csv

from dateutil.parser import parse
from sqlalchemy import Column, Date, Float, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///ab_nyc.sqlite3", echo=True)

Base = declarative_base()


class Listing(Base):
    """SQLAlchemy mapped class. Maps a Listing object to the corresponding
    database table."""

    __tablename__ = "listings_sqlalchemy"

    id = Column(Integer, primary_key=True)
    name = Column(String(200))

    host_id = Column(Integer)
    host_name = Column(String(50))

    neighbourhood_group = Column(String(20))
    neighbourhood = Column(String(20))

    latitude = Column(Float)
    longitude = Column(Float)

    room_type = Column(String(20))
    price = Column(Integer)
    minimum_nights = Column(Integer)

    number_of_reviews = Column(Integer)
    last_review = Column(Date, nullable=True)
    reviews_per_month = Column(Integer)
    calculated_host_listings_count = Column(Integer)
    availability_365 = Column(Integer)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


def parse_none(dt):
    """Trys to parse a string date and returns None if unable to."""

    try:
        return parse(dt)
    except:
        return None


def prepare_listing(row):
    """Takes a row from CSV file and returns a Listing object from it."""

    row["last_review"] = parse_none(row["last_review"])
    return Listing(**row)


with open("AB_NYC_2019.csv", encoding="utf-8", newline="") as csv_file:
    csvreader = csv.DictReader(csv_file, quotechar='"')

    listings = [prepare_listing(row) for row in csvreader]

    session = Session()
    session.add_all(listings)
    session.commit()
