from flask import Flask
from flask_restful import Api as RESTfulAPI


def create_app(config):
    app = Flask(config.APP_NAME)
    app.config.from_object(config)
    return app


def init_app(app):
    rest_api = RESTfulAPI(app, catch_all_404s=True)

