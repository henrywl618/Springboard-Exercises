import os
from flask import Flask, render_template, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from form import PetForm, PetEditForm
from models import db, connect_db, Pet
from werkzeug.utils import secure_filename



app = Flask(__name__)
app.debug=True
app.config['SECRET_KEY'] = '12345678'
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False
toolbar = DebugToolbarExtension(app)

UPLOAD_FOLDER = '/home/henry/Springboard/SQLAlchemy/adopt_app/static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

connect_db(app)
db.create_all()

@app.route('/')
def view_homepage():
    """View app homepage."""
    pets=Pet.query.all()
    return render_template('homepage.html',pets=pets)

@app.route('/add',methods=['GET','POST'])
def add_pets():
    """View form to add pets, and handles form submission"""    
    form = PetForm()
    # Add pet to the DB on form submission/validation and redirect to the homepage.
    if form.validate_on_submit():

        # Unpack items from form.data dictionary as keyword arguments. Remove csrf token from the dictionary since it is not an attribute of the Pet() model. Allows us to change the form and not have to change the route.
        new_pet = Pet(**{key:value for (key,value) in form.data.items() if key != 'csrf_token' and key != 'photo_file'})
        
        if form.photo_file.data:
            f = form.photo_file.data
            filename = secure_filename(f.filename)
            photo_path= os.path.join(app.config['UPLOAD_FOLDER'], filename)
            f.save(photo_path)
            # Set image url to be the photo_path
            new_pet.photo_url = f"/static/{filename}"
        # new_pet = Pet(name=form.name.data,
        #               species=form.species.data,
        #               photo_url=form.photo_url.data,
        #               age=form.age.data,
        #               notes=form.notes.data,
        #               available=form.available.data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f'{new_pet.name} was successfully added.')
        return redirect('/')
    else:
        return render_template('addpets.html',form=form)

@app.route('/<int:pet_id>',methods=['GET','POST'])
def pet_details(pet_id):
    """View pet deatail and form to edit a pet, and handles form submission"""   
    pet = Pet.query.get_or_404(pet_id)
    # Populate the form with attributes from the selected pet if the matching field is empty
    edit_form = PetEditForm(obj=pet)
    # Edits the pet in db on form submission/validation and redirect back to the pet detail page
    if edit_form.validate_on_submit():
        pet.notes = edit_form.notes.data
        pet.photo_url = edit_form.photo_url.data
        pet.available = edit_form.available.data
        db.session.commit()
        flash(f'{pet.name} was successfully edited.')
        return redirect(f'/{pet_id}')
    else:
        return render_template('view_edit_pet.html',pet=pet,form=edit_form)

