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
from app.forms import ContactForm
from app.models import Post, Contact
from app.email import send_contact_email

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
            page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('index', page=posts.next_num) if posts.has_next else None
    prev_url = url_for('index', page=posts.prev_num) if posts.has_prev else None
    return render_template('index.html', title='home', posts=posts.items,
                           next_url=next_url, prev_url=prev_url)

# Reuse the index.html template to create an archive page that shows all posts
@app.route('/archive')
def archive():
    page = request.args.get('page', 2, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
            page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('index', page=posts.next_num) if posts.has_next else None
    prev_url = url_for('index', page=posts.prev_num) if posts.has_prev else None
    return render_template('index.html', title='archive', posts=posts.items,
                           next_url=next_url, prev_url=prev_url)

@app.route('/me', methods=['GET', 'POST'])
def me():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(name=form.name.data, email=form.email.data, 
                          message=form.message.data)
        # add contact to database
        db.session.add(contact)
        db.session.commit()
        # pass contact to send_contact_email(contact) function in email.py
        if contact:
            send_contact_email(contact)
        flash('Thank you, John will get back to you')    
        return redirect(url_for('index'))
    return render_template('me.html', title='me', form=form)
        







