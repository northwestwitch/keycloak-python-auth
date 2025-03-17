import os

from authlib.integrations.flask_client import OAuth
from flask import Blueprint, current_app, redirect, session, url_for

auth_bp = Blueprint("auth", __name__)

# Initialize OAuth
oauth = OAuth()


def init_auth(app):
    oauth.init_app(app)

    # Keycloak OAuth configuration
    keycloak = oauth.register(
        "keycloak",
        client_id=app.config["KEYCLOAK_CLIENT_ID"],
        client_secret=app.config["KEYCLOAK_CLIENT_SECRET"],
        authorize_url=app.config["KEYCLOAK_AUTH_URL"],
        access_token_url=app.config["KEYCLOAK_TOKEN_URL"],
        client_kwargs={"scope": "openid profile email"},
    )

    app.keycloak = keycloak


@auth_bp.route("/login")
def login():
    keycloak = current_app.keycloak  # Accessing keycloak from the current app context
    redirect_uri = url_for(
        "auth.dashboard", _external=True
    )  # Correct redirect URI using the 'auth' blueprint
    return keycloak.authorize_redirect(redirect_uri)


# Dashboard view (success redirect after login)
@auth_bp.route("/dashboard")
def dashboard():
    return "Welcome to your dashboard! You are logged in."


@auth_bp.route("/auth_callback")
def auth_callback():
    keycloak = current_app.keycloak
    token = keycloak.authorize_access_token()
    user = keycloak.parse_id_token(token)
    session["user"] = user
    return redirect(
        url_for("views.index")
    )  # Ensure 'views.index' is a valid route in your app


@auth_bp.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("views.index"))  # Redirect to a valid route after logout
