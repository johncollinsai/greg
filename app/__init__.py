""" My app/__init__.py file creates objects, such as the database and database
migration engine instances. These are created after the application. 
"""

from flask import Flask    # Flask (upper case) class imported from flask package
from config import Config  # Config class (upper case) imported from config.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
''' app.config.from_object method tells Flask to read and apply the Config class,
which it finds in config.py'''
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models, errors
