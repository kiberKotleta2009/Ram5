from flask import Flask
from random import randint

app = Flask(__name__)


@app.route('/')
def menu():
    s = "<ul>"
    s += '<li><p><a href="https://ram5pls.herokuapp.com/task1/random">task1/random</a></p></li>'
    s += '<li><p><a href="https://ram5pls.herokuapp.com/task1/i_will_not">task1/i_will_not</a></p></li>'
#     s += '<li><p><a href="http://127.0.0.1:5000/task1/random">task1/random</a></p></li>'
#     s += '<li><p><a href="http://127.0.0.1:5000/task1/i_will_not">task1/i_will_not</a></p></li>'
    s += "</ul>"
    out = "<pre id=menu>{}</pre>".format(s)
    return out


@app.route('/haba')
def hello_world():
    s = ["Hello, Haba!",
         "Hello, Arsen!",
         "Hello, Karim!"]

    out = "<pre>{}</pre>".format("\n".join(s))
    return out


@app.route('/task1/random')
def task1():
    a = randint(1, 3)
    out = "<pre>{}</pre>".format("Haba's mark is " + str(a))
    return out


@app.route('/task1/i_will_not')
def task1_never():
    s = "<ul>"
    for i in range(100):
        s += "<li>I will not waste time</li>"
    s += "</ul>"
    out = "<pre id=blackboard >{}</pre>".format(s)
    return out


app.run()
