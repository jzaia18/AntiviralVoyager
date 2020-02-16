from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
import os, json
from utils import ibm_utils
from utils import geocoder

app = Flask(__name__)
DIR = os.path.dirname(__file__) or '.'
app.secret_key = os.urandom(32)


@app.route("/")
def root():
    return render_template("home.html")


@app.route("/home")
def home():
    return redirect(url_for("root"))


@app.route("/maptest")
def maptest():
    return render_template("map.html")


@app.route("/sources")
def sources():
    return render_template("sources.html")


@app.route("/calcrisk")
def calc_risk():
    return render_template("calc_risk.html")


@app.route("/facts")
def facts():
    return render_template("facts.html")


@app.route("/infectionresults")
def infection_results():
    # print(request.args)
    result = ibm_utils.query_US(request.args['year'], request.args['month'], request.args['state'],
                                request.args['setting'], request.args['state'], request.args['year'],
                                request.args['disaster'])
    return render_template("calc_risk.html", result="%.2f" % result, resultType="infection")


@app.route("/volcanoresults")
def volcano_results():
    # print(request.args)
    coords = geocoder.get_coords(request.args['location'])
    # print(coords)
    if (request.args['disaster'] == 'earthquake'):
        result = ibm_utils.query_VolcanicEarthquake(coords[0], coords[1], request.args['elevation'], request.args['type'],request.args['VEI'])['predictions'][0]['values'][0]
    else:
        result = ibm_utils.query_VolcanicTsunami(coords[0], coords[1], request.args['elevation'], request.args['type'],request.args['VEI'])['predictions'][0]['values'][0]
    return render_template("calc_risk.html", result=result, resultType="volcanic")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
