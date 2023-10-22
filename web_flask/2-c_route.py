#!/usr/bin/python3
"""
Starts a Flask web application.

- Listens on 0.0.0.0, port 5000.
- Defines three routes:
    1. '/': Displays "Hello HBNB!"
    2. '/hbnb': Displays "HBNB"
    3. '/c/<text>': Displays "C " followed by the value of the text variable (replace underscore _ symbols with a space).

Usage:
1. Run this script to start the web application.
2. Access the routes with a web browser or using curl.

"""

from flask import Flask
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
def display_text(text):
    """
    Displays "C " followed by the value of the text variable, replacing underscores with spaces.

    :param text: The text to be displayed.
    """
    text = unquote(text).replace('_', ' ')
    return f"C {text}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
