"""Seed file to make sample data for jobly db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add pets
john = User(first_name='John', last_name="Doe", image_url='https://www.stockvault.net/data/2009/06/09/109080/preview16.jpg')
jane = User(first_name='Jane', last_name="Doe")
spike = User(first_name='Spike', last_name="Lee", image_url='https://cdn.britannica.com/04/113304-050-F9162580/Spike-Lee-2007.jpg')

# Add new objects to session, so they'll persist
db.session.add(john)
db.session.add(jane)
db.session.add(spike)

# Commit--otherwise, this never gets saved!
db.session.commit()