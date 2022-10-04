""" My app/__init__.py file creates objects, such as the database and database
migration engine instances. These are created after the application. 
"""

# Flask (upper case) class imported from flask package (lower case)
from flask import Flask    
# Config class (upper case) imported from config.py (lower case)
from config import Config  # Config class (upper case) imported from config.py (lower case)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_bootstrap import Bootstrap
from flask_bootstrap import Bootstrap4
from flask_fontawesome import FontAwesome
from flask_mail import Mail  # import Mail class
# Error handling per miguelgrinberg ch7
# import logging
# from logging.handlers import SMTPHander, RotatingFileHandler

app = Flask(__name__)
# app.config.from_object method tells Flask to read and apply the Config class, 
# which it finds in config.py
app.config.from_object(Config)
app.config['FONTAWESOME_STYLES'] = ['brands']
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap4(app)
fa = FontAwesome(app)
mail = Mail(app)

from app import routes, models, errors
