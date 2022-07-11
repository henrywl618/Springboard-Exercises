from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User, Feedback
from forms import RegisterForm, LoginForm, FeedbackForm
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///flask_feedback"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "abc123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
bcrypt = Bcrypt()
toolbar = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    return redirect('/register')

@app.route('/users/<username>')
def view_secret(username):
    user = User.query.get_or_404(username)
    if session.get('user') == username:
        feedback = user.feedback
        return render_template('secret.html',user=user, feedback=feedback)
    flash('You need to login first!')
    return redirect('/login')
    

@app.route('/register',methods=['GET','POST'])
def view_register():
    """Show user register form and handles form submission to create a new user"""
    form = RegisterForm()

    # On POST request, add the new user to the database
    if form.validate_on_submit():
        # Unpack items from form.data dictionary as keyword arguments. Remove csrf token from the dictionary since it is not an attribute of the User() model. Allows us to change the form and not have to change the route.
        new_user = User.register(**{key:value for (key,value) in form.data.items() if key != 'csrf_token'})
        db.session.add(new_user)
        db.session.commit()
        session['user'] = new_user.username
        flash('New user created successfully!')
        return redirect(f'/users/{new_user.username}')

    return render_template("register.html",form=form)

@app.route('/login',methods=['GET','POST'])
def view_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.authenticate(username = form.username.data,
                                 password = form.password.data)
        if user:
            session['user'] = user.username
            return redirect(f'/users/{user.username}')
        else:
            form.username.errors = ['Invalid username/password.']

    return render_template("login.html",form=form)

@app.route('/logout')
def logout():
    session.pop('user')
    flash('Logged out successfully!')
    return redirect('/')

@app.route('/users/<username>/delete',methods=['POST'])
def delete_user(username):
    user = User.query.get_or_404(username)
    if session.get('user') == user.username:
        db.session.delete(user)
        db.session.commit()
        flash(f'{user.username} deleted!')
        return redirect('/')
    flash(f'Not authorized to delete {username}.')
    return redirect('/')

@app.route('/users/<username>/feedback/add',methods=['GET','POST'])
def feedback(username):
    form = FeedbackForm()
    user = User.query.get_or_404(username)
    if session.get('user') != user.username:
        flash(f'Unable to add feedback for {user.username}.')
        return redirect('/')
    if form.validate_on_submit():
        if session.get('user') == user.username:
            title = form.title.data
            content = form.content.data
            new_feedback = Feedback(title=title, content=content, username=user.username)
            db.session.add(new_feedback)
            db.session.commit()
            return redirect(f'/users/{user.username}')
        else:
            flash(f'Unable to submit feedback under {user.username}.')

    return render_template('feedback.html', form=form, user=user)

@app.route('/feedback/<feedback_id>/update',methods=['GET','POST'])
def edit_feedback(feedback_id):
    feedback = Feedback.query.get_or_404(feedback_id)
    form = FeedbackForm(obj=feedback)
    if session.get('user') != feedback.user.username:
        flash(f'Unable to edit feedback for {feedback.user.username}.')
        return redirect('/')
    if form.validate_on_submit():
        if session.get('user') == feedback.user.username:
            feedback.title = form.title.data
            feedback.content = form.content.data
            db.session.commit()
            return redirect(f'/users/{feedback.user.username}')
        else:
            flash(f'Unable to edit feedback for {feedback.user.username}.')
            return redirect('/')

    return render_template('editfeedback.html', form=form, user=feedback.user, feedback=feedback)

@app.route('/feedback/<feedback_id>/delete',methods=['POST'])
def delete_feedback(feedback_id):
    feedback = Feedback.query.get_or_404(feedback_id)
    if session.get('user') == feedback.user.username:
        db.session.delete(feedback)
        db.session.commit()
        flash('Feedback deleted!')
        return redirect(f'/users/{feedback.user.username}')
    flash(f'Not authorized to delete {username}.')
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404