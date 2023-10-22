#!/usr/bin/python3
""" This script starts a Flask web application. """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name)

@app.teardown_appcontext
def teardown_db(exception):
    """ Closes the current SQLAlchemy Session. """
    storage.close()

@app.route('/states_list', strict_slashes=False)
def display_states_list():
    """ Displays a list of all State objects sorted by name. """
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)

    return render_template('7-states_list.html', states=states)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
