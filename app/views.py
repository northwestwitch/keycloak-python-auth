from flask import Blueprint, render_template, session

from app.auth import login, logout

# Create a Blueprint for the views
views_bp = Blueprint("views", __name__)


@views_bp.route("/")
def index():
    user = session.get("user")
    return render_template("index.html", user=user)


@views_bp.route("/login")
def login_view():
    return login()


@views_bp.route("/logout")
def logout_view():
    return logout()
