''' Helper function to send email, i.e., Contact email from me form. Note that 
it is important to send email asynchonously because not doing so will slow
the application down considerably.
'''

from threading import Thread
from flask import render_template
from flask_mail import Message
from app import app, mail

# Asynchronous email send helper function, NB email passed by send_email() function below
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

# Email sending wrapper function. Passes email to send_async_email function above, 
# using the Thread class in final line
def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()

# modified version of def send_password_reset_email(user)
def send_contact_email(contact):
    send_email('Contact from johncollins.ai',
               sender=app.config['ADMINS'][0],
               recipients=['climatemetrics@gmail.com'],
               text_body=render_template('contact.txt',
                                         contact=contact),
               html_body=render_template('contact.html',
                                         contact=contact))


