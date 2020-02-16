from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
import os, json

app = Flask(__name__)
DIR = os.path.dirname(__file__) or '.'
app.secret_key = os.urandom(32)

@app.route("/")
def root():
    return render_template("base.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/maptest")
def maptest():
    return render_template("map.html")

@app.route("/sources")
def sources():
    return render_template("sources.html")



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
