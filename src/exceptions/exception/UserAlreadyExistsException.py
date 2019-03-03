from .UserApiException import UserApiException


class UserAlreadyExistsException(UserApiException):
    def __init__(self):
        super(UserAlreadyExistsException, self).__init__("User Already exists", 409)
