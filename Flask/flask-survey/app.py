from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys

app = Flask(__name__)
# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = '123456'


@app.route('/')
def homepage():
    return render_template('home.html',surveys=surveys)

@app.route('/routesurvey')
def routesurvey():
    session['survey'] = request.args['survey']
    return redirect(f"/survey/{request.args['survey']}")

@app.route('/survey/<survey>')
def view_survey(survey):
    return render_template('survey.html',surveys=surveys,survey=survey)

@app.route('/question/<number>')
def questions(number):
    survey = surveys[session['survey']]
    responses = session.get('responses',[])

    if int(number) != len(responses):
        flash("Survey must be done in order.")
        return redirect(f"/question/{len(responses)}")
    elif len(responses) == len(survey.questions):
        flash("The survey is complete")
        return render_template('thankyou.html')
    return render_template('question.html', survey=survey, number=int(number))

#answer page should increment question counter and redirect to the next question
@app.route('/answer')
def answer():
    survey = surveys[session['survey']]
    responses = session['responses']
    responses.append(request.args['choices'])
    session['responses'] = responses
    if len(responses) == len(survey.questions):
        return render_template('thankyou.html')
    return redirect(f"/question/{len(responses)}")

@app.route('/start_survey')
def start_survey():
    session['responses'] = []
    return redirect('/question/0')