from .UserApiException import UserApiException


class LoginException(UserApiException):
    def __init__(self):
        super(LoginException, self).__init__("Could not create access token", 500)
