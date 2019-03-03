from src.models.models import UserLogin
from src.repository.UserRepository import UserRepository
from src.util.Logger import Logger

from src.exceptions.exceptions import UserAlreadyExistsException


class UserBusiness:

    def __init__(self):
        self.__user_repository = UserRepository()
        self.__logger = Logger().get_logger()

    def add_new_user(self, user: UserLogin):
        self.__logger.info(f"Validating the insertion of new user: {user.login}")
        existent_user = self.__user_repository.get_user(user.login)

        if existent_user is not None:
            raise UserAlreadyExistsException()

        new_user = self.__user_repository.add_new_user(user)
        self.__logger.info(f"New user ID: {new_user.user_id}")
        return new_user

    def get_users(self):
        users = self.__user_repository.get_users()
        return users
