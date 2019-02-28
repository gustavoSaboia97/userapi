from .User import User


class UserLogin(User):

    def __init__(self, user_id: str, name: str, login: str, password: str):
        super().__init__(user_id, name)
        self.__login = login
        self.__password = password.__hash__()

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    def to_mongo_dict(self):
        return {
            "name": self.name,
            "login": self.login,
            "password": self.password
        }

    def to_dict(self):
        return {
            "id": self.user_id,
            "name": self.name,
            "login": self.login
        }
