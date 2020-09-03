#!/usr/bin/python3
"""Some random docstring"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """SHUTS THE SESSION DOWN"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def hello_world_states(id=None):
    """
    ---------------------------
    METHOD: HELLO WORLD /states
    ---------------------------
    Description:
        Generates and returns an HTML with all the
        states if flask hits a ping on 0:5000/states
    Args:
        id: optional argument that generates an HTML
        with all the details of that specific state.
    """
    states = storage.all(State)
    if id is not None:
        id = 'State' + '.' + id
    return render_template('9-states.html',
                           objects=states,
                           id=id
                           )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
