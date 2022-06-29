from unittest import TestCase

from app import app
from models import User, db

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI']='postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO']=False

# Make Flask errors be real errors, rather then HTML pages with error info
app.config['TESTING']=True

# Don't use Flask Debugtoolbar which will add html to the page
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class AppRouteTestCase(TestCase):
    """Tests for app routing."""

    def setUp(self):
        """Add sample user"""

        User.query.delete()
        john = User(first_name='John', last_name="Doe", image_url='https://www.stockvault.net/data/2009/06/09/109080/preview16.jpg')
        db.session.add(john)
        db.session.commit()
        self.user_id = john.id
    
    def tearDown(self):
        """ Clean up any fouled transaction."""
        db.session.rollback()
    
    def test_add_users(self):
        with app.test_client() as client:
            response = client.post('/users/new',data={
                'firstName' : 'Jane',
                'lastName' : 'Doe',
                'url' : 'www.google.com'
            },follow_redirects=True)
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code,200)
            self.assertIn('Jane Doe',html)

    def test_edit_users(self):
        with app.test_client() as client:
            response = client.post(f'/users/{self.user_id}/edit', data={
                'firstName' : 'Bruce',
                'lastName' : 'Lee',
                'url' : 'www.google.com'
            },follow_redirects=True)
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code,200)
            self.assertIn('Bruce Lee',html)
    
    def test_view_userlist(self):
        with app.test_client() as client:
            response = client.get('/users')
            html=response.get_data(as_text=True)

            self.assertEqual(response.status_code,200)
            self.assertIn('<li><a href="/users/5">John Doe</a>',html)

    def test_view_userdetail(self):
        with app.test_client() as client:
            response = client.get('/users/4')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code,200)
            self.assertIn('<h1>John Doe</h1>',html)