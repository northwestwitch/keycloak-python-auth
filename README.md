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

<img width="1038" alt="Image" src="https://github.com/user-attachments/assets/8cede065-b1ab-4448-aadc-717457b6c3de" />

Note that general client settings are accessible at this URL: `http://localhost:8080/realms/CG/.well-known/openid-configuration`

```
{
   "issuer":"http://localhost:8080/realms/CG",
   "authorization_endpoint":"http://localhost:8080/realms/CG/protocol/openid-connect/auth",
   "token_endpoint":"http://localhost:8080/realms/CG/protocol/openid-connect/token",
   "introspection_endpoint":"http://localhost:8080/realms/CG/protocol/openid-connect/token/introspect",
   "userinfo_endpoint":"http://localhost:8080/realms/CG/protocol/openid-connect/userinfo",
   "end_session_endpoint":"http://localhost:8080/realms/CG/protocol/openid-connect/logout",
   "frontchannel_logout_session_supported":true,
   "frontchannel_logout_supported":true,
   "jwks_uri":"http://localhost:8080/realms/CG/protocol/openid-connect/certs",
   "check_session_iframe":"http://localhost:8080/realms/CG/protocol/openid-connect/login-status-iframe.html",
   "grant_types_supported":[
      "authorization_code",
      "implicit",
      "refresh_token",
      "password",
      "client_credentials",
      "urn:openid:params:grant-type:ciba",
      "urn:ietf:params:oauth:grant-type:device_code"
   ],
   "acr_values_supported":[
      "0",
      "1"
   ],
   "response_types_supported":[
      "code",
      "none",
      "id_token",
      "token",
      "id_token token",
      "code id_token",
      "code token",
      "code id_token token"
   ],
   "subject_types_supported":[
      "public",
      "pairwise"
   ],
   "id_token_signing_alg_values_supported":[
      "PS384",
      "ES384",
      "RS384",
      "HS256",
      "HS512",
      "ES256",
      "RS256",
      "HS384",
      "ES512",
      "PS256",
      "PS512",
      "RS512"
   ],
   "id_token_encryption_alg_values_supported":[
      "RSA-OAEP",
      "RSA-OAEP-256",
      "RSA1_5"
   ],
   "id_token_encryption_enc_values_supported":[
      "A256GCM",
      "A192GCM",
      "A128GCM",
      "A128CBC-HS256",
      "A192CBC-HS384",
      "A256CBC-HS512"
   ],
   "userinfo_signing_alg_values_supported":[
      "PS384",
      "ES384",
      "RS384",
      "HS256",
      "HS512",
      "ES256",
      "RS256",
      "HS384",
      "ES512",
      "PS256",
      "PS512",
      "RS512",
      "none"
   ],
   "userinfo_encryption_alg_values_supported":[
      "RSA-OAEP",
      "RSA-OAEP-256",
      "RSA1_5"
   ],
   "userinfo_encryption_enc_values_supported":[
      "A256GCM",
      "A192GCM",
      "A128GCM",
      "A128CBC-HS256",
      "A192CBC-HS384",
      "A256CBC-HS512"
   ],
   "request_object_signing_alg_values_supported":[
      "PS384",
      "ES384",
      "RS384",
      "HS256",
      "HS512",
      "ES256",
      "RS256",
      "HS384",
      "ES512",
      "PS256",
      "PS512",
      "RS512",
      "none"
   ],
   "request_object_encryption_alg_values_supported":[
      "RSA-OAEP",
      "RSA-OAEP-256",
      "RSA1_5"
   ],
   "request_object_encryption_enc_values_supported":[
      "A256GCM",
      "A192GCM",
      "A128GCM",
      "A128CBC-HS256",
      "A192CBC-HS384",
      "A256CBC-HS512"
   ],
   "response_modes_supported":[
      "query",
      "fragment",
      "form_post",
      "query.jwt",
      "fragment.jwt",
      "form_post.jwt",
      "jwt"
   ],
   "registration_endpoint":"http://localhost:8080/realms/CG/clients-registrations/openid-connect",
   "token_endpoint_auth_methods_supported":[
      "private_key_jwt",
      "client_secret_basic",
      "client_secret_post",
      "tls_client_auth",
      "client_secret_jwt"
   ],
   "token_endpoint_auth_signing_alg_values_supported":[
      "PS384",
      "ES384",
      "RS384",
      "HS256",
      "HS512",
      "ES256",
      "RS256",
      "HS384",
      "ES512",
      "PS256",
      "PS512",
      "RS512"
   ],
   "introspection_endpoint_auth_methods_supported":[
      "private_key_jwt",
      "client_secret_basic",
      "client_secret_post",
      "tls_client_auth",
      "client_secret_jwt"
   ],
   "introspection_endpoint_auth_signing_alg_values_supported":[
      "PS384",
      "ES384",
      "RS384",
      "HS256",
      "HS512",
      "ES256",
      "RS256",
      "HS384",
      "ES512",
      "PS256",
      "PS512",
      "RS512"
   ],
   "authorization_signing_alg_values_supported":[
      "PS384",
      "ES384",
      "RS384",
      "HS256",
      "HS512",
      "ES256",
      "RS256",
      "HS384",
      "ES512",
      "PS256",
      "PS512",
      "RS512"
   ],
   "authorization_encryption_alg_values_supported":[
      "RSA-OAEP",
      "RSA-OAEP-256",
      "RSA1_5"
   ],
   "authorization_encryption_enc_values_supported":[
      "A256GCM",
      "A192GCM",
      "A128GCM",
      "A128CBC-HS256",
      "A192CBC-HS384",
      "A256CBC-HS512"
   ],
   "claims_supported":[
      "aud",
      "sub",
      "iss",
      "auth_time",
      "name",
      "given_name",
      "family_name",
      "preferred_username",
      "email",
      "acr"
   ],
   "claim_types_supported":[
      "normal"
   ],
   "claims_parameter_supported":true,
   "scopes_supported":[
      "openid",
      "address",
      "phone",
      "microprofile-jwt",
      "acr",
      "roles",
      "web-origins",
      "offline_access",
      "email",
      "profile"
   ],
   "request_parameter_supported":true,
   "request_uri_parameter_supported":true,
   "require_request_uri_registration":true,
   "code_challenge_methods_supported":[
      "plain",
      "S256"
   ],
   "tls_client_certificate_bound_access_tokens":true,
   "revocation_endpoint":"http://localhost:8080/realms/CG/protocol/openid-connect/revoke",
   "revocation_endpoint_auth_methods_supported":[
      "private_key_jwt",
      "client_secret_basic",
      "client_secret_post",
      "tls_client_auth",
      "client_secret_jwt"
   ],
   "revocation_endpoint_auth_signing_alg_values_supported":[
      "PS384",
      "ES384",
      "RS384",
      "HS256",
      "HS512",
      "ES256",
      "RS256",
      "HS384",
      "ES512",
      "PS256",
      "PS512",
      "RS512"
   ],
   "backchannel_logout_supported":true,
   "backchannel_logout_session_supported":true,
   "device_authorization_endpoint":"http://localhost:8080/realms/CG/protocol/openid-connect/auth/device",
   "backchannel_token_delivery_modes_supported":[
      "poll",
      "ping"
   ],
   "backchannel_authentication_endpoint":"http://localhost:8080/realms/CG/protocol/openid-connect/ext/ciba/auth",
   "backchannel_authentication_request_signing_alg_values_supported":[
      "PS384",
      "ES384",
      "RS384",
      "ES256",
      "RS256",
      "ES512",
      "PS256",
      "PS512",
      "RS512"
   ],
   "require_pushed_authorization_requests":false,
   "pushed_authorization_request_endpoint":"http://localhost:8080/realms/CG/protocol/openid-connect/ext/par/request",
   "mtls_endpoint_aliases":{
      "token_endpoint":"http://localhost:8080/realms/CG/protocol/openid-connect/token",
      "revocation_endpoint":"http://localhost:8080/realms/CG/protocol/openid-connect/revoke",
      "introspection_endpoint":"http://localhost:8080/realms/CG/protocol/openid-connect/token/introspect",
      "device_authorization_endpoint":"http://localhost:8080/realms/CG/protocol/openid-connect/auth/device",
      "registration_endpoint":"http://localhost:8080/realms/CG/clients-registrations/openid-connect",
      "userinfo_endpoint":"http://localhost:8080/realms/CG/protocol/openid-connect/userinfo",
      "pushed_authorization_request_endpoint":"http://localhost:8080/realms/CG/protocol/openid-connect/ext/par/request",
      "backchannel_authentication_endpoint":"http://localhost:8080/realms/CG/protocol/openid-connect/ext/ciba/auth"
   },
   "authorization_response_iss_parameter_supported":true
}
```


