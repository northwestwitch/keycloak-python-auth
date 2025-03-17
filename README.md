# keycloak-python-auth

Example code of auth using keycloak and python Flask

# Launch keycloak using docker-compose

```
docker-compose up
```

## Log in into Keycloak and edit the settings

Go to `http://localhost:8080/admin/master/console/` and log in as the admin user:

```
user: admin
password: admin
```

You will be asked to modify your password.

### Step 1: Create a new Realm with a user

For the sake of testing, assume that user email is verified

<img width="1096" alt="Image" src="https://github.com/user-attachments/assets/b3928eb3-7904-4d2c-901d-db0256124b19" />

### Set user credentials

Also for the sake of testing set a password (example: "test") which is not a temporary password

<img width="1188" alt="Image" src="https://github.com/user-attachments/assets/164439fd-6be4-4219-bc52-6fd81c6aa2df" />

### Testing the login

Going to the following URL `http://localhost:8080/realms/CG/account`

Will show a login window that will work for the new user with the newly created credentials:

<img width="494" alt="Image" src="https://github.com/user-attachments/assets/8176c24b-dcdd-40c9-ad60-34971548b239" />

### Create a client

Back on the admin interface, create a client. A client is an application that can request authentication on behalf of a user. The application might be a web application or a backend API.

Client settings:

<img width="1398" alt="Image" src="https://github.com/user-attachments/assets/4a203d37-0fff-4395-a90f-fc1e3775a210" />

The client should have the following access settings:

```
Root URL: http://127.0.0.1/
Valid Redirect URIs: http://127.0.0.1:5000/auth
Valid Post Logout Redirect URIs: http://127.0.0.1/
Web Origins: http://127.0.0.1
```

And 



<img width="1038" alt="Image" src="https://github.com/user-attachments/assets/8cede065-b1ab-4448-aadc-717457b6c3de" />

Note that general client settings are accessible at this URL: `http://localhost:8080/realms/CG/.well-known/openid-configuration`


