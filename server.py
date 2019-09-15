from json import load
from logging import getLogger
from flask import Flask
from flask_restful import Api as RESTfulAPI

from choices import Choices
from resources import ChoiceResource, ChoicesResource


def _load_choices(path):
    with open(path) as f:
        rules = load(f)
    return Choices(rules)


def create_app(config):
    app = Flask(config.APP_NAME)
    app.config.from_object(config)
    app.choices = _load_choices(config.RULES_FILE)

    gunicorn_logger = getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

    return app


def init_app(app):
    rest_api = RESTfulAPI(app, catch_all_404s=True)
    rest_api.add_resource(ChoicesResource, '/api/v0.1/choices')
    rest_api.add_resource(ChoiceResource, '/api/v0.1/choice')
