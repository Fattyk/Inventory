# Inventory Documentation


### Requirements:
After installing Django, please run *pip install -r requirements.txt* on your command line to install rest_framework.


**Using the App:**

User must first register
User must login to access the app


### User Management:


#### - 	user must be able to register
*POST /user/register/*

**Description:** Registration of User

```json
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Users Registration",
    "description": "Registration of User",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ]
}

```

Content:

```json
{
    "username" : "", // Required
    "password" : "", // Required
    "first_name" : "",
    "middle_name" : "",
    "last_name" : "",
    "email" : "",
    "mobile" : "",
    "birth_date" : ""
}
```

Suceess: status(ok)

```json
{
    "username" : "data", 
    "password" : "data", 
    "first_name" : "data",
    "middle_name" : "data",
    "last_name" : "data",
    "email" : "data",
    "password" : "data",
    "mobile" : "data",
    "birth_date" : "data"
}

```

Wrong input: status (404)

```json
{
    "error":"Invalid Credentials"
}
```



#### -	user must be able to update profile
#### -	user must be able to retrieve his profile information
#### -	user must be able to change password


#### -	user must be able to login
*/user/login*
```json
{
    "username" : "",
    "password" : ""
}
```


#### -	user must be able to logout



### Core Functionalities: User must be able to 

#### -	create item (with unique code)
#### -	delete item
#### -	search for item
#### -	view search history
#### -	set item quantity upon creation
#### -	add or remove from quantity based on purchase or use
#### -	view item inventory history
#### -	can filter items based on quantity
#### -	can filter item inventory history by date.

