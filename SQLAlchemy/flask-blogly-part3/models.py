"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def connect_db(app):
    """ Connect to the database """
    db.app = app
    db.init_app(app)

class User(db.Model):
    """ User. """
    

    __tablename__="users"

    def __repr__(self):
        return f'<{self.id} {self.first_name} {self.last_name}>'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String,
                           nullable=False)
    last_name = db.Column(db.String,
                           nullable=False)                          
    image_url = db.Column(db.String)


    @property
    def full_name(self):
        """ Return First Name+Last Name of the user """

        return f'{self.first_name} {self.last_name}'

class Post(db.Model):
    """ Post """

    __tablename__="posts"

    def __repr__(self):
        return f'<{self.id} {self.title} {self.content} {self.created_at} {self.user_id}>'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String,
                      nullable=False)
    content = db.Column(db.String,
                    nullable=False)
    created_at = db.Column(db.String,
                    default=datetime.now().strftime("%m/%d/%Y %I:%M %p"))
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'))
    user = db.relationship('User', backref=db.backref('posts',cascade='all,delete-orphan'))

    tags = db.relationship('Tag',
                            secondary='posts_tags',
                            backref='posts')

class Tag(db.Model):
    """ Tag """

    __tablename__="tags"

    def __repr__(self):
        return f'<ID:{self.id} Name:{self.name}>'
    
    id = db.Column(db.Integer,
                 primary_key=True,
                 autoincrement=True)
    
    name = db.Column(db.String,
                     nullable=False,
                     unique=True)

class PostTag(db.Model):
    """ Post tags """

    __tablename__="posts_tags"

    post_id = db.Column(db.Integer,
                        db.ForeignKey('posts.id'),
                        primary_key=True)
    tag_id = db.Column(db.Integer,
                        db.ForeignKey('tags.id'),
                        primary_key=True)
    
    
    
