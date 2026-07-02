class StatusCodes:

    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    INTERNAL_SERVER_ERROR = 500

class UserCreationMessages:

    CREATED = {
        "success": True,
        "user": 
            {
                "email": "",
                "name": ""
            },
        "accessToken": "Bearer ...",
        "refreshToken": "..."
    }

    FORBIDDEN_EXIST = {
        "success": False,
        "message": "User already exists"
    }

    FORBIDDEN_EMPTY = {
        "success": False,
        "message": "Email, password and name are required fields"
    }

class UserLoginMessages:

    CREATED = {
        "success": True,
        "accessToken": "",
        "refreshToken": "",
        "user": 
        {
        "email": "",
        "name": ""
        }
    }

    UNAUTHORIZED = {
        "success": False,
        "message": "email or password are incorrect"
    }

class OrderCreatingMessages:

    CREATED = {
        "name": "Краторный метеоритный бургер",
        "order": {"number"},
        "success": True
    }
