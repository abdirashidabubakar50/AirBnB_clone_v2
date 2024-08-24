#!/usr/bin/python3
"""This script starts a flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function will be executed when someone accesses the root URL ('/').
    It returns the string "Hello HBNB!" to be displayed in the browser or the
    terminal.
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function will be executed when someone accesses the root URL ('/').
    It returns the string "Hello HBNB!" to be displayed in the browser or the
    terminal.
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)