import os
from flask import Flask
from flask_smorest import Api
from extensios import db
import models
from dotenv import load_dotenv
# List of endpoints
from resources.store_api import blp as StoreBlueprint
from resources.item_api import blp as ItemBlueprint

load_dotenv()


def create_app():

    app = Flask(__name__)
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///data.db')

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['API_TITLE'] = 'API Supermercado'
    #
    app.config['API_VERSION'] = 'v1.0'
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config['OPENAPI_URL_PREFIX'] = '/'
    app.config['OPENAPI_SWAGGER_UI_PATH'] = "/swagger-ui"
    app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'


    api = Api(app)

    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(ItemBlueprint)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app