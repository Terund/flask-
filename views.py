from flask import render_template, request
from models import *
from main import app


@app.route('/')
def index():
    return render_template("index.html", **locals())


@app.route('/about/')
def about():
    return render_template("about.html")

