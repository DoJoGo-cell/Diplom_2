class UserCreatingData:

    MISSING_EMAIL = {
        "password": "zxcdeadinside",
        "name": "adun"
    }

class UserLoginData:

    INVALID_DATA = {
        "email": "%^&*",
        "password": "%^&*"
    }

class OrderCreatingData:

    BURGER_WITH_INGREDIENTS = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70"]}

    BURGER_WITHOUT_INGREDIENTS = {"ingredients": []}

    INVALID_HREF = {"ingredients": ["123", "123"]}