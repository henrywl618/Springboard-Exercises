from unittest import TestCase

from app import app
from models import User, db

app.config['SQLALCHEMY_DATABASE_URI']='postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO']=False

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
    
    def test_attributes(self):
        john = User(first_name='John', last_name="Doe", image_url='https://www.stockvault.net/data/2009/06/09/109080/preview16.jpg')
        self.assertEqual(john.first_name,'John')
        self.assertEqual(john.last_name,'Doe')
        self.assertEqual(john.image_url,'https://www.stockvault.net/data/2009/06/09/109080/preview16.jpg')
    

