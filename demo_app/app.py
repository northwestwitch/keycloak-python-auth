import requests
from authlib.integrations.flask_client import OAuth
from flask import Flask, flash, redirect, render_template, session, url_for

from demo_app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = app.config["FLASK_SECRET_KEY"].encode()


oauth = OAuth(app)
keycloak = oauth.register(
    name="keycloak",
    client_id=app.config["KEYCLOAK_CLIENT_ID"],
    client_secret=app.config["KEYCLOAK_CLIENT_SECRET"],
    server_metadata_url=app.config["KEYCLOAK_SERVER_METADATA_URL"],
    client_kwargs={"scope": "openid profile email"},
)


@app.route("/")
def index():
    user = session.get("user")
    return render_template("index.html", user=user)


# Login page
@app.route("/login", methods=["POST"])
def login():
    redirect_uri = url_for(".auth", _external=True)
    return oauth.keycloak.authorize_redirect(redirect_uri)


# Auth callback
@app.route("/auth")
def auth():
    token = oauth.keycloak.authorize_access_token()
    session["token_response"] = token
    print(token)
    session["user"] = oauth.keycloak.parse_id_token(token, None)
    return redirect("/")


# Logout
@app.route("/logout", methods=["POST"])
def logout():
    if session.get("token_response"):
        refresh_token = session["token_response"]["refresh_token"]
        requests.post(
            app.config["KEYCLOAK_LOGOUT_URL"],
            data={
                "client_id": app.config["KEYCLOAK_CLIENT_ID"],
                "client_secret": app.config["KEYCLOAK_CLIENT_SECRET"],
                "refresh_token": refresh_token,
            },
        )
        session.clear()
        flash("You were logged out.", "success")

    return redirect(url_for("index"))


def main():
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
