""" 1. Routes are the different URLs that my application (i.e., app, being the 
sub-directory 'app') implements. In Flask, handlers for the application routes
are written as Python functions, called view functions. View functions are 
mapped to one or more route URLs so that Flask knows what logic to execute when 
a client requests a given URL.
2. Flask makes extensive use of decorators.  A decorator modifies the function 
that follows it.
3. The order in which decorators are written matters.
"""

from flask import render_template
from app import app    # import app variable, which is a member of app package.

@app.route('/')
@app.route('/index')
def index():

    posts = [
        {
            'author':  'John',
            'body': 'Lets go out for lunch'
        },
        {
            'author': 'Chiafen',
            'body': 'What are we going to have to eat?'
        }
    ]

    return render_template('index.html', title='Home', posts=posts)
