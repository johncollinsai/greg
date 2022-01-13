''' johncollins.py is a top-level script that represents the johncollins
application. The only thing this script does is import the application. Flask
obtains the application instance from this file via export FLASK_APP=johncollins.py
'''

from app import app, db
from app.models import Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Post': Post}


