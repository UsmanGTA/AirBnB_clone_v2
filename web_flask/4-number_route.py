#!/usr/bin/python3
"""Some random docstring"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world_root():
    """
    ------------------------
    METHOD: HELLO WORLD ROOT
    ------------------------
    Description:
        Prints out "Hello HBNB!" if
        flask hits a ping on 0:5000/
    Args:
        None
    """
    return("Hello HBNB!\n")


@app.route('/hbnb', strict_slashes=False)
def hello_world_hbnb():
    """
    ------------------------
    METHOD: HELLO WORLD HBNB
    ------------------------
    Description:
        Prints out "HBNB!" if flask hits
        a ping on 0:5000/hbnb
    Args:
        None
    """
    return("HBNB\n")


@app.route('/c/<text>', strict_slashes=False)
def hello_world_c_text(text=""):
    """
    -----------------------------
    METHOD: HELLO WORLD /C/{TEXT}
    -----------------------------
    Description:
        Prints out "C + {text}" if flask hits
        a ping on 0:5000/c/<some_text>
    Args:
        None
    """
    text = text.replace('_', ' ')
    return ("C " + text + '\n')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_world_python_text(text="is_cool"):
    """
    ----------------------------------
    METHOD: HELLO WORLD /python/{TEXT}
    ----------------------------------
    Description:
        Prints out "Python + {text}" if flask hits
        a ping on 0:5000/python/<some_text>
    Args:
        None
    """
    text = text.replace('_', ' ')
    return ("Python " + text + '\n')


@app.route('/number/<int:n>', strict_slashes=False)
def hello_world_number_int(n):
    """
    ----------------------------------
    METHOD: HELLO WORLD /number/{int}
    ----------------------------------
    Description:
        Prints out "n + is a number" if flask hits
        a ping on 0:5000/number/<some_number>
    Args:
        None
    """
    return (str(n) + " is a number\n")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
