#!/usr/bin/env python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route("/result")
def result():
    return "RESULTS"

if __name__=='__main__':
    app.run(debug=True)
