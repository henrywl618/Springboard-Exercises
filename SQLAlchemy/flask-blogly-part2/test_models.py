from unittest import TestCase
import pdb
from app import app
from models import User, Post, db

app.config['SQLALCHEMY_DATABASE_URI']='postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO']=True

db.drop_all()
db.create_all()

class UserModelTestCase(TestCase):
    """ Tests for model for Users."""

    def setUp(self):
        """ Clean up any existing users. And add sample users"""
        User.query.delete()


    def tearDown(self):
        """ Clean up any fouled transaction."""
        db.session.rollback()
    
    def test_user_attributes(self):
        john = User(first_name='John', last_name="Doe", image_url='https://www.stockvault.net/data/2009/06/09/109080/preview16.jpg')
        db.session.add(john)
        db.session.commit()
        self.assertEqual(john.first_name,'John')
        self.assertEqual(john.last_name,'Doe')
        self.assertEqual(john.image_url,'https://www.stockvault.net/data/2009/06/09/109080/preview16.jpg')
    
    def test_post_attributes(self):
        john = User(first_name='John', last_name="Doe", image_url='https://www.stockvault.net/data/2009/06/09/109080/preview16.jpg')
        post1= Post(title='My dog',content='This is my dog!',user_id=1)
        db.session.add_all([john,post1])
        db.session.commit()
        self.assertEqual(post1.title,'My dog')
        self.assertEqual(post1.content,'This is my dog!')
        self.assertEqual(post1.user.id,1)

