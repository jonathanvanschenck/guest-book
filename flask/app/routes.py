# This manages all the flask views

from flask import url_for, render_template, flash, redirect

# Import the flask app instance so as to attach routes
from app import app

# Set the index views
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
