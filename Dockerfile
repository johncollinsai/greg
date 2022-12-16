FROM python:slim

WORKDIR /home/johncollins

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY johncollins.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP johncollins.py

ENV PORT 8080
ENTRYPOINT ["./boot.sh"]

