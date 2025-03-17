# app/routes.py
from flask import Blueprint, redirect, url_for, session
from app.auth import oauth

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def index():
    user = session.get('user')
    if user:
        return f'Hello, {user["name"]}!'
    return 'Welcome to the app! <a href="/login">Login</a>'

@auth_bp.route('/login')
def login():
    keycloak = oauth.create_client('keycloak')
    redirect_uri = url_for('auth.auth', _external=True)
    return keycloak.authorize_redirect(redirect_uri)

@auth_bp.route('/auth')
def auth():
    keycloak = oauth.create_client('keycloak')
    token = keycloak.authorize_access_token()
    user = keycloak.parse_id_token(token)
    session['user'] = user
    return redirect('/')