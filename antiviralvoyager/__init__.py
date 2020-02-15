from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
import os, json

app = Flask(__name__)
DIR = os.path.dirname(__file__) or '.'
app.secret_key = os.urandom(32)

@app.route("/")
def root():
    return render_template("base.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
