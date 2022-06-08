from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = '123456'

responses = []

@app.route('/')
def homepage():
    return render_template('home.html',satisfaction_survey=satisfaction_survey)

@app.route('/question/<number>')
def questions(number):
    if int(number) != len(responses):
        flash("Survey must be done in order.")
        return redirect(f"/question/{len(responses)}")
    elif len(responses) == len(satisfaction_survey.questions):
        flash("The survey is complete")
        return render_template('thankyou.html')
    return render_template('question.html', satisfaction_survey=satisfaction_survey, number=int(number))

#answer page should increment question counter and redirect to the next question
@app.route('/answer')
def answer():
    responses.append(request.args['choices'])
    if len(responses) == len(satisfaction_survey.questions):
        return render_template('thankyou.html')
    return redirect(f"/question/{len(responses)}")