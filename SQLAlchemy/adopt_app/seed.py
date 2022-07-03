"""Seed file to make sample data for adopt db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
buddy = Pet(name='Buddy', species="Dog", photo_url='https://bit.ly/3yfovzk',age=2,notes='This is the best doggo')
tabby = Pet(name='Tabby', species="Cat", photo_url='https://media.istockphoto.com/photos/closeup-portrait-of-funny-ginger-cat-wearing-sunglasses-isolated-on-picture-id1188445864?k=20&m=1188445864&s=612x612&w=0&h=0vuJeOxJr8Lu3Q1VdT1z7t6HcM8Oj7EVJe3CexGnH_8=',age=5,notes='This is the best cat')

db.session.add_all([buddy,tabby])
db.session.commit()
