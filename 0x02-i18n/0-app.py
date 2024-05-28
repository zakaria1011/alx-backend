#!/usr/bin/python3
""" flask app """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ redner template"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
