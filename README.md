# User API

This repository contains an user API that is responsible for controlling all user access.

# Install dependencies

`pip install -r requirements.txt`

# Running Tests

`python -m unittest discover`

# Running the application

`gunicorn --bind localhost:8080 wsgi`

# Mongo Configuration

An environment variable is necessary to set the database to persist information.

`DATABASE_URI=mongodb://localhost:27017/`

# Use of the API

POST routes:

* `/api/user/` -> Insert a new user by an json

Json request pattern:
```
    {
        "name": "user_name", 
        "login": "user_login",
        "password": "user_password"
    }
```
RESPONSE:
```
    {
        "id": "user_id",
        "name": "user_name",
        "login": "user_login"
    } 
```
GET routes:

* `/api/user/` -> Get all users from database

RESPONSE:
```
    [
        {
            "id": "user_id_1",
            "name": "user_name_1"
        },
        {
            "id": "user_id_2",
            "name": "user_name_2"
        }
    ]    
```

* `/api/user/USER_ID` -> Get information about getting it by the user id

RESPONSE:
```
    {
        "id": "user_id",
        "name": "user_name"
    }   
```

LOGIN routes:

* `/api/user/login/` -> Create an access token that is responsible for user system access.

Json request pattern:

```
    {
        "login": "user_login",
        "password": "user_password"
    }
```

RESPONSE:

``` 
    {
        "id": "user_id",
        "name": "user_name",
        "login": "user_login",
        "access_token": "user_access_token"
    }
```