"""Seed file to make sample data for jobly db."""

from models import User,Post,Tag,PostTag, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
john = User(first_name='John', last_name="Doe", image_url='https://www.stockvault.net/data/2009/06/09/109080/preview16.jpg')
jane = User(first_name='Jane', last_name="Doe")
spike = User(first_name='Spike', last_name="Lee", image_url='https://cdn.britannica.com/04/113304-050-F9162580/Spike-Lee-2007.jpg')

# Add posts
post1= Post(title='My dog',content='This is my dog!',user_id=1)
post2= Post(title='Catz',content='This is my cat!',user_id=2)
post3= Post(title='I took this picture',content='Amazing sunset!',user_id=2)
post4= Post(title='Short Movie',content='Check out this short I made!',user_id=3)

# Add tags

tag1= Tag(name='meme')
tag2= Tag(name='news')
tag3= Tag(name='cat')
tag4= Tag(name='puppers')
tag5= Tag(name='fun')

# Add Post Tags

post_tag1= PostTag(post_id=1,tag_id=4)
post_tag2= PostTag(post_id=1,tag_id=5)
post_tag3= PostTag(post_id=2,tag_id=3)
post_tag4= PostTag(post_id=2,tag_id=5)

# Add new objects to session, so they'll persist
db.session.add(john)
db.session.add(jane)
db.session.add(spike)

# Commit--otherwise, this never gets saved!
db.session.commit()

db.session.add_all([post1,post2,post3,post4])
db.session.commit()

db.session.add_all([tag1,tag2,tag3,tag4,tag5])
db.session.commit()

db.session.add_all([post_tag1,post_tag2,post_tag3,post_tag4])
db.session.commit()