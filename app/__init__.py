from flask import Flask
from app.auth import init_auth

def create_app():
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object('config.Config')

    # Initialize authentication
    init_auth(app)

    # Register blueprints and views
    from app.views import views_bp
    app.register_blueprint(views_bp)

    return app