''' I have not yet properly implemented the error handling in ch7 and code in 
this respect is rem'd out below. MUST REVISIT CH7, UNDERSTAND IT, AND IMPLEMENT
PROPERLY! UNDERSTANDING ERROR HANDLING IS SUPER-IMPORTANT
'''

# import logging
# from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask  # Flask (upper case) class imported from flask package
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail  # Not sure if this is properly installed
from flask_bootstrap import Bootstrap
from config import Config  # Config class (upper case) imported from config.py

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# mail = Mail(app)
bootstrap = Bootstrap(app)


# if not app.debug:
#     if app.config['MAIL_SERVER']:
#         auth = None
#         if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
#             auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
#         secure = None
#         if app.config['MAIL_USE_TLS']:
#             secure = ()
#         mail_handler = SMTPHandler(
#             mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
#             fromaddr='no-reply@' + app.config['MAIL_SERVER'],
#             toaddrs=app.config['ADMINS'], subject='Microblog Failure',
#             credentials=auth, secure=secure)
#         mail_handler.setLevel(logging.ERROR)
#         app.logger.addHandler(mail_handler)

#     if not os.path.exists('logs'):
#         os.mkdir('logs')
#     file_handler = RotatingFileHandler('logs/johncollins.log', maxBytes=10240,
#                                        backupCount=10)
#     file_handler.setFormatter(logging.Formatter(
#         '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
#     file_handler.setLevel(logging.INFO)
#     app.logger.addHandler(file_handler)

#     app.logger.setLevel(logging.INFO)
#     app.logger.info('johncollins startup')

from app import routes, models, errors