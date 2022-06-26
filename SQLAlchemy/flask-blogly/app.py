"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = '123456'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False
app.debug=True
toolbar = DebugToolbarExtension(app)


connect_db(app)
db.create_all()

@app.route('/')
def homepage():
    return redirect('/users')

@app.route('/users')
def userlist():
    """Renders the userlist page"""
    users = User.query.order_by(User.last_name,User.first_name).all()
    return render_template('userlist.html',users=users)

@app.route('/users/new',methods=['GET'])
def load_createuser_page():
    """Renders the add user form page """
    return render_template('adduser.html')

@app.route('/users/new',methods=['POST'])
def add_user():
    """Adds inputed user information to the database and redirects back to the user list"""
    first_name = request.form['firstName']
    last_name = request.form['lastName']
    url = request.form['url']
    new_user = User(first_name=first_name, last_name=last_name, image_url=url)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<user_id>')
def show_userinfo(user_id):
    """Renders user detail page for given user_id """
    user = User.query.get(user_id)
    return render_template('userdetail.html',user=user)

@app.route('/users/<user_id>/edit',methods=['GET'])
def show_editform(user_id):
    """ Render the edit form page """
    user = User.query.get(user_id)
    return render_template('edituser.html',user=user)

@app.route('/users/<user_id>/edit',methods=['POST'])
def edit_user(user_id):
    """ Edits the users information with information from the form """
    first_name = request.form['firstName']
    last_name = request.form['lastName']
    url = request.form['url']
    user = User.query.get(user_id)
    
    user.first_name = first_name
    user.last_name = last_name
    user.image_url = url

    db.session.add(user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<user_id>/delete')
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')
