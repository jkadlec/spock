FROM python:3.7.4-stretch

RUN pip3 install Flask-RESTful==0.3.7 gunicorn==19.9.0 requests==2.22.0

WORKDIR /app/worker

COPY . /app/worker

CMD gunicorn --log-level=info --bind 0.0.0.0:5000 -w 4 app:app
