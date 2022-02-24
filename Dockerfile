FROM python:slim

# RUN useradd microblog

WORKDIR /home/johncollins

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql cryptography

COPY app app
COPY migrations migrations
COPY johncollins.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP johncollins.py

# RUN chown -R johncollins:johncollins ./
# USER microblog

# https://www.cloudsavvyit.com/14880/whats-the-difference-between-exposing-and-publishing-a-docker-port/
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]

