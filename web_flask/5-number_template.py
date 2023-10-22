#!/usr/bin/python3
"""
Starts a Flask web application.

- Listens on 0.0.0.0, port 5000.
- Defines six routes:
    1. '/': Displays "Hello HBNB!"
    2. '/hbnb': Displays "HBNB"
    3. '/c/<text>': Displays "C " followed by the value of the text variable, replacing underscores with spaces.
    4. '/python/(<text>)': Displays "Python " followed by the value of the text variable, or "Python is cool" if no text is provided.
    5. '/number/<n>': Displays "n is a number" only if n is an integer.
    6. '/number_template/<n>': Displays an HTML page with the H1 tag: "Number: n" inside the BODY tag, but only if n is an integer.

Usage:
1. Run this script to start the web application.
2. Access the routes with a web browser or using curl.

"""

from flask import Flask, render_template
from urllib.parse import unquote

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays "Hello HBNB!" when accessing the root route.
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays "HBNB" when accessing the '/hbnb' route.
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """
    Displays "C " followed by the value of the text variable, replacing underscores with spaces.

    :param text: The text to be displayed.
    """
    text = unquote(text).replace('_', ' ')
    return f"C {text}"

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text):
    """
    Displays "Python " followed by the value of the text variable, or "Python is cool" if no text is provided.

    :param text: The text to be displayed.
    """
    text = unquote(text).replace('_', ' ')
    return f"Python {text}"

@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """
    Displays "n is a number" when accessing the '/number/<n>' route, but only if n is an integer.

    :param n: The number to be displayed.
    """
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """
    Displays an HTML page with the H1 tag: "Number: n" inside the BODY tag, but only if n is an integer.

    :param n: The number to be displayed.
    """
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
