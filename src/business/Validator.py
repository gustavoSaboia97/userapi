from src.models.models import UserLogin

from src.exceptions.exceptions import CannotBeBlankException


class Validator:

    @staticmethod
    def validate_user_dict_add_user(user_json: dict):
        if "name" not in user_json:
            raise CannotBeBlankException("name")
        if "login" not in user_json:
            raise CannotBeBlankException("login")
        if "password" not in user_json:
            raise CannotBeBlankException("password")
        if not bool(user_json["name"].strip()):
            raise CannotBeBlankException("name")
        if not bool(user_json["login"].strip()):
            raise CannotBeBlankException("login")
        if not bool(user_json["password"].strip()):
            raise CannotBeBlankException("password")

    @staticmethod
    def validate_user_dict_login(login_json: dict):
        if "login" not in login_json:
            raise CannotBeBlankException("login")
        if "password" not in login_json:
            raise CannotBeBlankException("password")
        if not bool(login_json["login"].strip()):
            raise CannotBeBlankException("login")
        if not bool(login_json["password"].strip()):
            raise CannotBeBlankException("password")

    @staticmethod
    def validate_user_dict_validate_access_token(access_token_json: dict):
        if "login" not in access_token_json:
            raise CannotBeBlankException("login")
        if "access_token" not in access_token_json:
            raise CannotBeBlankException("access_token")
        if not bool(access_token_json["login"].strip()):
            raise CannotBeBlankException("login")
        if not bool(access_token_json["access_token"].strip()):
            raise CannotBeBlankException("access_token")

    @staticmethod
    def is_wrong_access_token(user: UserLogin, user_login_information: UserLogin):
        return user.access_token != user_login_information.access_token

    @staticmethod
    def is_wrong_credentials(user: UserLogin, user_login_information: UserLogin):
        return (user.password != user_login_information.password) or (user.login != user_login_information.login)
