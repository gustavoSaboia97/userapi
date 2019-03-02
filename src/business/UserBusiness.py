from src.repository.UserRepository import UserRepository


class UserBusiness:

    def __init__(self):
        self.__user_repository = UserRepository()

    def get_users(self):
        users = self.__user_repository.get_users()
        return users
