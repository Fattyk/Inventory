# Inventory Documentation


### Requirements:
After installing Django, please run *pip install -r requirements.txt* on your command line to install rest_framework.



**Using the App:**
- User must login to access the app
- Use admin as default username and password
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


## User Management:



### - 	user must be able to register
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


### -	user must be able to update profile
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


### -	user must be able to retrieve his profile information
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



### -	user must be able to change password
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



### -	user must be able to login
*POST /user/login/*
**Description:** Verify and login user
Content:

```json
{
    "username": "",
    "password": ""
}
```



### -	user must be able to logout
*GET /user/logout/*
**Description:** Logout User




## Core Functionalities: User must be able to 


### -	create item (with unique code)
*POST /create/*
**Description:** This create an item
Content:

```json
{
    "name": "a",
    "price": "3.00",
    "quantity": 5
}
```



### -	delete item
*DELETE /myitem/{product_id}/*
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



### -	View item
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



### -	search for item
*GET /*
**Description:** List all items and also enable search with 'search' parameter
**Example:** /?search=apple
Content:

```json
[
    {
        "name": "Apple",
        "price": "500.00",
        "quantity": 6
    },
    {
        "name": "Pineapple",
        "price": "250.00",
        "quantity": 8
    }
]
```



### -	view search history
*GET /search_history/*
**Description:** List search item history for the authenticated user
Content:

```json
[
    {
        "history": "rad",
        "created": "2021-08-15"
    },
    {
        "history": "rad",
        "created": "2021-08-15"
    },
    {
        "history": "2",
        "created": "2021-08-15"
    },
    {
        "history": "2",
        "created": "2021-08-15"
    }
]
```



### -	set item quantity upon creation
**Description:** Quantity, Price and Name must be supplied during registration
Content:

```json
{
    "name": "a",
    "price": "3.00",
    "quantity": 5
}
```



# I will cover others


### -	add or remove from quantity based on purchase or use
*PUT /myitem/{product_id}/*
product_id = integer
**Description:** name, price and quantity of this item can be modified by the owner. This will enable the owner/uer to add or remove quantity as desired.
Content:

```json
{
    "quantity": 15
}
```


### -	view item inventory history


### -	can filter items based on quantity
*GET /*
**Description:** List all items and also enable filter with 'quantity' parameter to filter quantity only
**Example:** /?quantity=3
Content:

```json
[
    {
        "name": "Mango",
        "price": "500.00",
        "quantity": 3
    },
    {
        "name": "Pineapple",
        "price": "250.00",
        "quantity": 3
    }
]
```



### -	can filter item inventory history by date.