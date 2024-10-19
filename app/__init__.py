from flask import Flask
from flask_restx import Api
from pymongo import MongoClient
from config.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize MongoDB
    app.mongo = MongoClient(app.config['MONGO_URI'])
    app.db = app.mongo.get_default_database()

    # Initialize Flask-RESTX
    api = Api(app, title='User CRUD API', version='1.0', description='User CRUD API for Checking Out using Flask')

    # Import and register blueprints/resources
    from app.routes.user_routes import api as user_ns
    api.add_namespace(user_ns)

    return app