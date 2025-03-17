from authlib.integrations.flask_client import OAuth
from flask import Flask, redirect, render_template_string, session, url_for

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
    if user:
        return render_template_string(
            """
            <h1>Welcome, {{ user['name'] }}!</h1>
            <form action="{{ url_for('logout') }}" method="post">
                <button type="submit">Logout</button>
            </form>
        """,
            user=user,
        )
    else:
        return render_template_string(
            """
            <h1>Hello, you are not logged in.</h1>
            <form action="{{ url_for('login') }}" method="post">
                <button type="submit">Login</button>
            </form>
        """
        )


# Login page
@app.route("/login", methods=["POST"])
def login():
    redirect_uri = url_for("auth", _external=True)
    return keycloak.authorize_redirect(redirect_uri)


# Auth callback
@app.route("/auth")
def auth():
    token = keycloak.authorize_access_token()
    print(token)
    session["user"] = keycloak.parse_id_token(token, nonce=token.get("nonce"))
    return redirect("/")


# Logout
@app.route("/logout", methods=["POST"])
def logout():
    session.pop("user", None)
    logout_url = f"{app.config['KEYCLOAK_LOGOUT_URL']}?redirect_uri={url_for('index', _external=True)}"
    return redirect(logout_url)


def main():
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
