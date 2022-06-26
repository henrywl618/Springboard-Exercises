"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """ Connect to the database """
    db.app = app
    db.init_app(app)

class User(db.Model):
    """ User. """

    __tablename__="users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String,
                           nullable=False)
    last_name = db.Column(db.String,
                           nullable=False)                          
    image_url = db.Column(db.String)

    def get_fullname(self):
        """ Return First Name+Last Name of the user """

        return f'{self.first_name} {self.last_name}'