""" [Description]
"""

from flask import Flask    # Flask (upper case) class imported from flask package
from config import Config  # Config class (upper case) imported from config.py

app = Flask(__name__)
''' app.config.from_object method tells Flask to read and apply the Config class,
which it finds in config.py'''
app.config.from_object(Config)

from app import routes
