#!/usr/bin/python3
"""Some random docstring"""
from flask import Flask, render_template
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
    return("Hello HBNB!")


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
    return("HBNB")


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
        text: empty (by default) / custom text to append
    """
    text = text.replace('_', ' ')
    return ("C " + text)


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
    return ("Python " + text)


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
        n: integer
    """
    return (str(n) + " is a number")


@app.route('/number_template/<int:n>', strict_slashes=False)
def hello_world_number_template_int(n):
    """
    ------------------------------------------
    METHOD: HELLO WORLD /number_template/{int}
    ------------------------------------------
    Description:
        Prints out "Number: <some_number>" if flask hits
        a ping on 0:5000/number_template/<some_number>
    Args:
        n: integer
    """
    return render_template('5-number.html',
                            title='HBNB',
                            body='Number: {}'.format(n),
                           )

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def hello_world_odd_even_int(n):
    """
    ---------------------------------------------
    METHOD: HELLO WORLD /number_odd_or_even/{int}
    ---------------------------------------------
    Description:
        Prints out "Number: <some_number> is odd/even" if flask hits
        a ping on 0:5000/number_odd_or_even/<some_number>
    Args:
        None
    """
    odd_even = "odd" if n % 2 != 0 else "even"
    return render_template('6-number_odd_or_even.html',
                            title='HBNB',
                            body='Number: {} is {}'.format(n, odd_even),
                           )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
