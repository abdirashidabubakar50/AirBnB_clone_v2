#!/usr/bin/python3
"""This module loads all the states instances from dbstorage and lists them"""


from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


app.teardown_appcontext


def teardown():
    """
     Close the storage session after each request.
     This ensures that the database connection is properly closed.
     """
    storage.close


@app.route('/states_list/', strict_slashes=False)
def list_states():
    """Display the list of all objects present in DB storage
    sorted b name (A - Z) and a description of each state"""
    all_states = storage.all('State')

    sorted_states = sorted(all_states.values(), key=lambda state: state.name)

    return render_template('7-states_list.html', states=sorted_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
