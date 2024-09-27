from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize the SQLAlchemy database instance
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Load configuration from the config.py file
    app.config.from_object('config.Config')

    # Initialize the SQLAlchemy database instance with the app
    db.init_app(app)

    # Initialize Flask-Migrate with the app
    migrate.init_app(app, db)

    # Import views and authentication modules
    with app.app_context():
        from .views import *
        from .auth import *

        return app
