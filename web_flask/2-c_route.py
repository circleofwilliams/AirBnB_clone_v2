#!/usr/bin/python3
""" Script of a flask framework project """
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ A function to return a string """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hel():
    """ A function to return a string """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ A function to return C and user input text """
    newText = ""
    for i in text:
        if i == '_':
            i = ' '
        newText += i
    return "C {}".format(newText)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
