#!/usr/bin/python3
"""
Starts a Flask web application.

- Listens on 0.0.0.0, port 5000.
- Defines a single route '/' to display "Hello HBNB!"
- Uses the option strict_slashes=False in the route definition.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays "Hello HBNB!" when accessing the root route.
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
