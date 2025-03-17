from flask import Blueprint, render_template, redirect, url_for, session
from app.auth import login, logout

# Define the blueprint for views
views_bp = Blueprint('views', __name__)

@views_bp.route('/')
def index():
    # Home page, check if user is authenticated
    user = session.get('user')
    if user:
        return render_template('index.html', user=user)
    else:
        return render_template('index.html', user=None)

@views_bp.route('/login')
def login_view():
    return login()

@views_bp.route('/logout')
def logout_view():
    return logout()