"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User, Post, Tag, PostTag
from datetime import datetime
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
    posts=Post.query.order_by(Post.created_at.desc()).limit(5).all()
    return render_template('homepage.html',posts=posts)

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
    user = User.query.get_or_404(user_id)
    return render_template('userdetail.html',user=user)

@app.route('/users/<user_id>/edit',methods=['GET'])
def show_editform(user_id):
    """ Render the edit form page """
    user = User.query.get_or_404(user_id)
    return render_template('edituser.html',user=user)

@app.route('/users/<user_id>/edit',methods=['POST'])
def edit_user(user_id):
    """ Edits the users information with information from the form """
    first_name = request.form['firstName']
    last_name = request.form['lastName']
    url = request.form['url']
    user = User.query.get_or_404(user_id)
    
    user.first_name = first_name
    user.last_name = last_name
    user.image_url = url

    db.session.add(user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<user_id>/delete')
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<user_id>/posts/new',methods=['GET'])
def show_postform(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('postform.html', user=user)

@app.route('/users/<user_id>/posts/new',methods=['POST'])
def add_post(user_id):
    user = User.query.get_or_404(user_id)
    new_post = Post(title=request.form['title'],
                    content=request.form['content'],
                    created_at=datetime.now().strftime("%m/%d/%Y %I:%M %p"),
                    user_id=user.id)
    db.session.add(new_post)
    db.session.commit()
    return redirect(f'/users/{user.id}')

@app.route('/posts/<post_id>',methods=['GET'])
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html',post=post)

@app.route('/posts/<post_id>/edit',methods=['GET'])
def view_postedit_form(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('editpost.html',post=post)

@app.route('/posts/<post_id>/edit',methods=['POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']

    db.session.add(post)
    db.session.commit()

    return redirect(f'/posts/{post.id}')

@app.route('/post/<post_id>/delete',methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    user_id = post.user.id
    db.session.delete(post)
    db.session.commit()

    return redirect(f'/users/{user_id}')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/tags',methods=['GET'])
def view_tags():
    tags = Tag.query.all()
    return render_template('tags.html',tags=tags)

@app.route('/tags/<tag_id>',methods=['GET'])
def view_tag_details(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    return render_template('tagdetails.html',tag=tag)

@app.route('/tags/new',methods=['GET'])
def view_addtag_form():
    return render_template('tag_create.html')

@app.route('/tags/new',methods=['POST'])
def add_tag():
    new_tag = Tag(name=request.form['tagName'])
    db.session.add(new_tag)
    db.session.commit()
    return redirect('/tags')

@app.route('/tags/<tag_id>/delete',methods=['POST'])
def delete_tag(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    db.session.delete(tag)
    db.session.commit()
    return redirect('/tags')
