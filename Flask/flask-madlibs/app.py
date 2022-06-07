from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

import stories

app=Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = '123456'

toolbar = DebugToolbarExtension(app)

story = stories.story
prompts = story.prompts

@app.route('/')
def homepage():
    return render_template('app.html',prompts=prompts)

@app.route('/story')
def get_story():
    answers = request.args
    generated_story = story.generate(answers)
    return render_template('story.html',generated_story=generated_story)