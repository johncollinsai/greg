""" the config.py module is where I read all the environment variables
"""

import os
from dotenv import load_dotenv 

''' NB: I import the .env file before the Config class is created, so that 
the variables are already set when the class is constructed.
'''
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

''' how much of below should be moved into .env?  See ch15 and this:
https://stackoverflow.com/questions/52162882/set-flask-environment-to-development-mode-as-default
'''

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' \
            + os.path.join(basedir, 'app.db') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # configure an email server for app to use to send emails notifying errors
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25) # 25 is email default 
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['john.collins@edhec.com']

    # configuration element confining how many posts the page will render
    POSTS_PER_PAGE = 10



