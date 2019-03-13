from .UserApiException import UserApiException


class NonValidAccessTokenException(UserApiException):
    def __init__(self):
        super(NonValidAccessTokenException, self).__init__("Invalid access token", 401)
