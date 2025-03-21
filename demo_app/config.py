class Config:
    """Base configuration class."""

    FLASK_SECRET_KEY = "your_flask_secret_key"
    KEYCLOAK_CLIENT_ID = "scout-client"
    KEYCLOAK_CLIENT_SECRET = "JV5DRR3YvxW5JEsUOD3UXtbhqvaxKHdd"
    REALM = "CG"
    KEYCLOAK_SERVER_METADATA_URL = (
        f"http://localhost:8080/realms/{REALM}/.well-known/openid-configuration"
    )
    KEYCLOAK_LOGOUT_URL = (
        f"http://localhost:8080/realms/{REALM}/protocol/openid-connect/logout"
    )
