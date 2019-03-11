from .User import User

from src.util.UserHashPassword import UserHashPassword


class UserLogin(User):

    def __init__(self, user_id: str, name: str, login: str, password: str):
        super().__init__(user_id, name)
        self.__login = login
        self.__password = UserHashPassword.hash_password(password)
        self.__access_token = None

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @property
    def access_token(self):
        return self.__access_token

    @password.setter
    def password(self, password: str):
        self.__password = password

    @access_token.setter
    def access_token(self, access_token):
        self.__access_token = access_token

    def to_mongo_dict(self):
        return {
            "name": self.name,
            "login": self.login,
            "password": self.password,
            "access_token": self.access_token
        }

    def to_dict(self):
        return {
            "id": self.user_id,
            "name": self.name,
            "login": self.login
        }

    def access_token_to_dict(self):
        return {
            "id": self.user_id,
            "name": self.name,
            "login": self.login,
            "access_token": self.access_token
        }

    def access_token_validate_to_dict(self):
        return {
            "login": self.login,
            "access_token": "OK"
        }


