# Inventory Documentation


### Requirements:
After installing Django, please run *pip install -r requirements.txt* on your command line to install rest_framework.


**Using the App:**

User must login to access the app
use admin as default username and password

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


### User Management:


#### - 	user must be able to register
*POST /user/register/*

**Description:** Registration of User

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

Wrong input: status (404)


#### -	user must be able to update profile

*PUT /user/{user_id}/*
user_id = integer

**Description:** Update Profile Information of the User and not of others for Data Protection Purpose

Content:

```json
{
    "username": "",
    "first_name": "",
    "middle_name": "",
    "last_name": "",
    "email": "",
    "mobile": null,
    "birth_date": null
}
```

#### -	user must be able to retrieve his profile information

*GET /user/{user_id}/*

user_id = integer

**Description:** Retrieve Profile Information of the User and not of others

Content:

```json
{
    "username": "",
    "first_name": "",
    "middle_name": "",
    "last_name": "",
    "email": "",
    "mobile": null,
    "birth_date": null,
    "products": [
        1
    ]
}
```

Sucess: status(ok)


#### -	user must be able to change password

*POST /user/change_password/*

**Description:** Update User's password

Content:

```json
{
    "username": "",
    "password": "",
    "new_password": "",
    "confirm_password": ""
}
```


#### -	user must be able to login

*POST /user/login/*

**Description:** Verify and login user

Content:

```json
{
    "username": "",
    "password": ""
}
```

#### -	user must be able to logout

*GET /user/logout/*

**Description:** Logout User



### Core Functionalities: User must be able to 


#### -	create item (with unique code)

*POST /*
*GET /*

**Description:** This create and list all items

Content:

```json
{
    "name": "a",
    "price": "3.00",
    "quantity": 5
}
```

#### -	delete item

*DELETE /myitem/{product_id}/*
*PUT /myitem/{product_id}/*
*GET /myitem/{product_id}/*

product_id = integer

**Description:** This item can be retrieve, updated and deleted by the owner

Content:

```json
{
    "name": "a",
    "price": "3.00",
    "quantity": 5
}
```

#### -	View item

*GET /{product_id}/*
product_id = integer

**Description:** This item can be retrieve only

Content:

```json
{
    "name": "a",
    "price": "3.00",
    "quantity": 5
}
```

# I will cover others

#### -	search for item
#### -	view search history
#### -	set item quantity upon creation
#### -	add or remove from quantity based on purchase or use
#### -	view item inventory history
#### -	can filter items based on quantity
#### -	can filter item inventory history by date.

