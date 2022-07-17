from flask import Flask

from app.api.urls import api


def KnockKnock():
    return {
        "message": "Hello from  learn deployment!"
    }


def register_blueprint(app):
    app.register_blueprint(api)


def create_app():
    app = Flask(__name__)
    register_blueprint(app)
    app.add_url_rule("/knockknock",
                     view_func=KnockKnock)
    return app
