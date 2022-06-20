from boggle import Boggle
from flask import Flask, render_template, session, request, jsonify
from random import choice
import pdb

app = Flask(__name__)
app.config['SECRET_KEY']='BOGGLE'

boggle_game = Boggle(5)
guesses = {}

@app.route('/')
def startpage():
    return render_template("startpage.html")

@app.route('/game')
def display():
    """Initializes a new gameboard,sends it to the client as a cookie and render the html page """
    global boggle_game
    global gameboard
    size = request.args.get("size",5)
    boggle_game.size = int(size)
    gameboard = boggle_game.make_board()
    session['gameboard'] = gameboard
    global answers
    answers = boggle_game.find_answers(gameboard)
    return render_template('game.html')

@app.route('/game', methods=['POST'])
def find_word():
    """Takes the guess from the client, checks if its a valid guess and returns the result as JSON"""
    gameboard = session["gameboard"]
    guess = request.get_json().get('guess')
    global guesses
    guesses = request.get_json().get('guesses',{})
    result = {"result":boggle_game.check_valid_word(gameboard,guess)}
    return jsonify(result)

@app.route('/endgame', methods=['POST'])
def end_game():
    """Checks if the final score received from the client is a highscore and sends the highscore and games played counter back to the client"""
    #get current session's highscore (default 0),update highscore if the current score is greater
    highScore = session.get('highscore',0)
    score = request.get_json().get('score')
    if score > highScore:
        highScore = score
    session['highscore'] = highScore

    #get current gamesplayed (default 0) and increment it by 1
    gamesPlayed = session.get('games_played',0)
    gamesPlayed += 1
    session['games_played'] = gamesPlayed
    
    #return hiscore and gamesplayed as json so we can update the frontend
    return jsonify({'highscore':highScore,'games_played':gamesPlayed})

@app.route('/hint')
def get_hint():
    global guesses
    global answers
    coordinates = []
    #pick a random answer that has not been guessed yet
    random_hint = choice(answers)
    while random_hint in guesses:
        while len(random_hint) < 2:
            random_hint = choice(answers)
    #get coordinates
    boggle_game.get_coord(gameboard, random_hint.upper(), coordinates)
    return jsonify(coordinates,random_hint)
