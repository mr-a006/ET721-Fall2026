from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import db
from .routes import main

def create_app(config_object=None):
    app = Flask(__name__)

    # Set the default SQLALCHEMY_DATABASE_URI if not provided by config_object
    app.config.setdefault('SQLALCHEMY_DATABASE_URI', 'sqlite:///:memory:')
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)

    if config_object:
        app.config.from_object(config_object)
    
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main)

    return app
