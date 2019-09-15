from json import load
from flask import Flask
from flask_restful import Api as RESTfulAPI

def _load_choices(path):



def create_app(config):
    app = Flask(config.APP_NAME)
    app.config.from_object(config)
    app.choices = _load_choices(config.CHOICES_FILE)
    return app


def init_app(app):
    rest_api = RESTfulAPI(app, catch_all_404s=True)

