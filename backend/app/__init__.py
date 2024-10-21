# backend/app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)  # Enable CORS for all routes. Configure as needed.
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .routes import bp
    app.register_blueprint(bp, url_prefix='/api')
    
    return app
