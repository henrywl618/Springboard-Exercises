from boggle import Boggle
from flask import Flask, render_template, session, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY']='BOGGLE'

boggle_game = Boggle()
gameboard = boggle_game.make_board()

@app.route('/')
def display():
    global gameboard
    gameboard = boggle_game.make_board()
    session['gameboard'] = gameboard
    return render_template('home.html')

@app.route('/', methods=['POST'])
def find_word():
    guess = request.get_json().get('guess')
    result = {"result":boggle_game.check_valid_word(gameboard,guess)}
    return jsonify(result)