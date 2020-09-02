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


@app.route('/states_list', strict_slashes=False)
def hello_world_states_list():
    """
    --------------------------------
    METHOD: HELLO WORLD /states_list
    --------------------------------
    Description:
        Generates and returns an HTML with all the
        states if flask hits a ping on 0:5000/states_list
    Args:
        n: integer
    """
    objects = storage.all(State).values()
    return render_template('7-states_list.html',
                           title='HBNB',
                           objects=objects
                           )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
