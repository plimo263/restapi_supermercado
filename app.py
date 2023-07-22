import os
from flask import Flask
from extensios import db
import models
from dotenv import load_dotenv

load_dotenv()


def create_app():

    app = Flask(__name__)
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///data.db')

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app