"""
Project name: fisher
Description:
Create Time: 2020/7/30 13:53
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config.from_object("app.config.secret")
    app.config.from_object("app.config.settings")

    register_blueprint(app)
    register_plugin(app)

    print(app.url_map)
    return app

def register_blueprint(app: Flask):
    from app.web.book import bp_book
    app.register_blueprint(bp_book, url_prefix="/book")


def register_plugin(app: Flask):
    from app.models.book import db
    db.init_app(app)
    with app.app_context():
        db.create_all()
