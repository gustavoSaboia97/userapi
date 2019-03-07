from .UserApiException import UserApiException


class AccessTokenException(UserApiException):
    def __init__(self):
        super(AccessTokenException, self).__init__("Could not create access token", 500)
