# setup.py
from setuptools import find_packages, setup

setup(
    name="keycloak-flask-app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Flask",
        "Authlib",
        "python-dotenv",
    ],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "kcdemo=demo_app.app:main",
        ],
    },
)
