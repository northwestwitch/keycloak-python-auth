from authlib.integrations.flask_client import OAuth
from flask import redirect, url_for, session
import os

# Initialize OAuth
oauth = OAuth()

def init_auth(app):
    # Set up the OAuth client for Keycloak
    oauth.init_app(app)

    # Keycloak configuration
    keycloak = oauth.register(
        'keycloak',
        client_id=os.getenv('KEYCLOAK_CLIENT_ID'),
        client_secret=os.getenv('KEYCLOAK_CLIENT_SECRET'),
        authorize_url=os.getenv('KEYCLOAK_AUTH_URL'),
        authorize_params=None,
        access_token_url=os.getenv('KEYCLOAK_TOKEN_URL'),
        refresh_token_url=None,
        client_kwargs={'scope': 'openid profile email'},
    )

    app.keycloak = keycloak

def login():
    # Redirect to Keycloak's login page
    redirect_uri = url_for('auth.auth_callback', _external=True)
    return app.keycloak.authorize_redirect(redirect_uri)

def auth_callback():
    # Handle the callback from Keycloak and retrieve the user info
    token = app.keycloak.authorize_access_token()
    user = app.keycloak.parse_id_token(token)
    session['user'] = user
    return redirect(url_for('views.index'))

def logout():
    session.pop('user', None)
    return redirect(url_for('views.index'))