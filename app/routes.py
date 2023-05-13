""" 1. Routes are the different URLs that my application (i.e., app, being the 
sub-directory 'app') implements. In Flask, handlers for the application routes
are written as Python functions, called view functions. View functions are 
mapped to one or more route URLs so that Flask knows what logic to execute when 
a client requests a given URL.
2. Flask makes extensive use of decorators.  A decorator modifies the function 
that follows it.
3. The order in which decorators are written matters.
"""

from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app import app    # import app variable, which is a member of app package.

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html', title='home')

@app.route('/analystgpt', methods=['GET'])
def analystgpt():
    return render_template('analystgpt.html')

@app.route('/volgpt', methods=['GET'])
def volgpt():
    return render_template('volgpt.html')

@app.route('/gpt4', methods=['GET'])
def gpt4():
    return render_template('gpt4.html')

@app.route('/nanogpt', methods=['GET'])
def nanogpt():
    return render_template('nanogpt.html')

@app.route('/lstm', methods=['GET'])
def lstm():
    return render_template('lstm.html')

@app.route('/high-frequency-data', methods=['GET'])
def high_frequency_data():
    return render_template('high-frequency-data.html')

@app.route('/deep-learning-finance', methods=['GET'])
def deep_learning_finance():
    return render_template('deep-learning-finance.html')

@app.route('/promptengineering', methods=['GET'])
def promptengineering():
    return render_template('promptengineering.html')
