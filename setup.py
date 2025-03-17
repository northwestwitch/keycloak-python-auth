from setuptools import setup, find_packages

setup(
    name='flask_keycloak_auth',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==3.1.0',
        'Authlib==1.5.1',
        'gunicorn==23.0.0',
        'requests==2.32.3',
        'flask_oauthlib==0.9.6',  # If you're still using it in some way
    ],
    entry_points={
        'console_scripts': [
            'run=run:app',  # Allow running your app directly from the command line
        ],
    },
    # Metadata to include with the package
    author='Chiara Rasi',
    author_email='rasi.chiara@gmail.com',
    description='Flask application with Keycloak authentication',
    long_description='A simple Flask application that integrates Keycloak for authentication using Authlib.',
    long_description_content_type='text/markdown',
    url='https://github.com/northwestwitch/flask_keycloak_auth',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Flask',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)