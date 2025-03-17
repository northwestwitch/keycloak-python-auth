from flask import Flask

from app.auth import auth_bp, init_auth


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Debug the config values
    print("KEYCLOAK_AUTH_URL:", app.config.get("KEYCLOAK_AUTH_URL"))
    print("KEYCLOAK_TOKEN_URL:", app.config.get("KEYCLOAK_TOKEN_URL"))

    # Initialize authentication
    init_auth(app)

    # Register blueprints
    from app.views import views_bp

    app.register_blueprint(views_bp)

    # Register auth blueprint
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
