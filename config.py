class Config:
    """Base configuration class."""

    SECRET_KEY = "your-secret-key"  # Replace with your secret key
    SESSION_COOKIE_NAME = "your_session_cookie_name"

    # For Keycloak (or any other OAuth service) setup:
    KEYCLOAK_CLIENT_ID = "scout-client"
    REALM = "CG"
    KEYCLOAK_CLIENT_SECRET = "iQrQgRetrnuDxuzuFQG0YHsoWSGH7NPe"
    KEYCLOAK_AUTH_URL = (
        f"http://localhost:8080/realms/{REALM}/protocol/openid-connect/auth"
    )
    KEYCLOAK_TOKEN_URL = (
        f"http://localhost:8080/realms/{REALM}/protocol/openid-connect/token"
    )
