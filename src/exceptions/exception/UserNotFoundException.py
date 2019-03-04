from .UserApiException import UserApiException


class UserNotFoundException(UserApiException):

    def __init__(self):
        def __init__(self):
            super(UserNotFoundException, self).__init__("User Not Fount", 404)
