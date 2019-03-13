from src.models.models import UserLogin


class Validator:

    @staticmethod
    def is_wrong_access_token(user: UserLogin, user_login_information: UserLogin):
        return user.access_token != user_login_information.access_token

    @staticmethod
    def is_wrong_credentials(user: UserLogin, user_login_information: UserLogin):
        return (user.password != user_login_information.password) or (user.login != user_login_information.login)
