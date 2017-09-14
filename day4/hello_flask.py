#! /usr/bin/env python3
# -*- coding : UTF-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# Run: FLASK_APP='hello_flask.py' flask run
