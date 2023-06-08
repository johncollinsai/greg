from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app import app    # import app variable, which is a member of app package.

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html', title='home')

@app.route('/greguserguide', methods=['GET'])
def greguserguide():
    return render_template('greguserguide.html')
