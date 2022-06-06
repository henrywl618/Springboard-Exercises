# Put your app in here.
from operations import add, sub, div, mult
from flask import Flask, request
app = Flask(__name__)

@app.route('/add')
def addition():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{add(a,b)}"

@app.route('/sub')
def subtraction():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{sub(a,b)}"
    
@app.route('/mult')
def multiplication():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{mult(a,b)}"

@app.route('/div')
def division():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{div(a,b)}"

@app.route('/math/<operation>')
def math(operation):
    maths = {
        'add':add,
        'sub':sub,
        'mult':mult,
        'div':div
    }
    a = int(request.args["a"])
    b = int(request.args["b"])
    
    return f"{maths[operation](a,b)}"