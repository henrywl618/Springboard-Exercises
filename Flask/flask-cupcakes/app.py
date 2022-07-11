"""Flask app for Cupcakes"""
from crypt import methods
from importlib_metadata import method_cache
from flask import Flask, render_template, redirect, request, flash, jsonify
from models import db, connect_db, Cupcake
from forms import CupcakeForm

app = Flask(__name__)
app.debug=True
app.config['SECRET_KEY'] = '12345678'
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.route('/')
def view_homepage():
    cupcakes = Cupcake.query.all()
    form = CupcakeForm()
    return render_template('homepage.html',form=form,cupcakes=cupcakes)

@app.route('/api/cupcakes',methods=['GET'])
def get_cupcakes():
    """ Returns JSON of all cupcakes in the DB"""
    cupcakes = Cupcake.query.all()
    # Convert list of SQLAlchemy models into list of serializable dicts and return JSON
    serialized_cupcakes = [cupcake.serialize() for cupcake in cupcakes]
    return jsonify({'cupcakes':serialized_cupcakes})

@app.route('/api/cupcakes/<int:cupcake_id>',methods=['GET'])
def get_cupcake(cupcake_id):
    """ Returns JSON of one cupcake specified by cupcake_id"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized_cupcake = cupcake.serialize()
    return jsonify({'cupcake':serialized_cupcake})

@app.route('/api/cupcakes',methods=['POST'])
def add_cupcake():
    """ Adds a new cupcake to the DB using JSON from the request body and returns JSON of the added cupcake"""
    # Unpack received JSON as kwargs and create a new Cupcake SQLALchemy model
    new_cupcake = Cupcake(**request.json)
    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify({'cupcake':new_cupcake.serialize()}),201)

@app.route('/api/cupcakes/<int:cupcake_id>',methods=['PATCH'])
def update_cupcake(cupcake_id):
    """ Updates an existing cupcake """
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor = request.json.get('flavor',cupcake.flavor)
    cupcake.size = request.json.get('size',cupcake.flavor)
    cupcake.rating = request.json.get('rating',cupcake.rating)
    cupcake.image = request.json.get('image',cupcake.image)
    db.session.commit()
    return jsonify({'cupcake':cupcake.serialize()})

@app.route('/api/cupcakes/<int:cupcake_id>',methods=['DELETE'])
def delete_cupcake(cupcake_id):
    """ Deletes an existing cupcake """
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify({'message':'deleted'})