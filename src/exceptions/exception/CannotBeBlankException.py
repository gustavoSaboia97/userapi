from .UserApiException import UserApiException


class CannotBeBlankException(UserApiException):
    def __init__(self, field: str):
        super(CannotBeBlankException, self).__init__(f"Field {field} cannot be blank", 400)
