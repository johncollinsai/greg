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
    app.debug = True 


