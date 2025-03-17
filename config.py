# config.py

class Config:
    """Base configuration class."""
    SECRET_KEY = 'your-secret-key'  # Replace with your secret key
    SESSION_COOKIE_NAME = 'your_session_cookie_name'

    # For Keycloak (or any other OAuth service) setup:
    KEYCLOAK_SERVER_URL = 'http://localhost:8080/auth'
    KEYCLOAK_CLIENT_ID = 'your-client-id'
    KEYCLOAK_CLIENT_SECRET = 'your-client-secret'
    KEYCLOAK_REALM = 'CG'
