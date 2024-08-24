#!/usr/bin/python3
"""This script starts a flask web application"""
from flask import Flask, render_template


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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays "C " followed by the value of the text variable.
    Underscores in the text variable are replaced with spaces.
    """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is_cool"):
    """
    Displays "Python " followed by the value of the text variable.
    Underscores in the text variable are replaced with spaces.
    The default value of the text is "is_cool"
    """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    return f"{n} is a number"

@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer:"""
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
