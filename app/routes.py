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
from app import db     # import database for posting forms [REM later?]
# from app.forms import PostForm
from app.models import Post

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    # form = PostForm()
    # if form.validate_on_submit():
    #     post = Post(body=form.post.data, author='John Collins')
    #     db.session.add(post)
    #     db.session.commit()
    #     flash('Database updated')
    #     return redirect(url_for('index'))   # i.e., post/redirect/get pattern

    # posts = Post.query.all()
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', title='Home', posts=posts)

# Reuse the index.html template to create a page for older posts
@app.route('/archive')
def archive():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', title='archive', posts=posts)



