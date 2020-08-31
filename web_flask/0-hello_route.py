#!/usr/bin/python3
"""Some random docstring"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """
    -------------------
    METHOD: HELLO WORLD
    -------------------
    Description:
        Prints out "Hello HBNB!" if
        flask hits a ping on 0:5000/
    Args:
        None
    """
    return("Hello HBNB!\n")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
