from .UserApiException import UserApiException


class AuthenticationException(UserApiException):
    def __init__(self):
        super(AuthenticationException, self).__init__("Wrong login or password", 401)
