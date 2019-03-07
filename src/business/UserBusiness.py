from src.models.models import UserLogin
from src.repository.UserRepository import UserRepository
from src.util.Logger import Logger

from src.exceptions.exceptions import UserAlreadyExistsException, UserNotFoundException, LoginException

from .AccessTokenBusiness import AccessTokenBusiness


class UserBusiness:

    def __init__(self):
        self.__user_repository = UserRepository()
        self.__access_token_business = AccessTokenBusiness()
        self.__logger = Logger().get_logger()

    def add_new_user(self, user: UserLogin):
        self.__logger.info(f"Validating the insertion of new user: {user.login}")
        existent_user = self.__user_repository.get_user_by_login(user.login)

        if existent_user is not None:
            raise UserAlreadyExistsException()

        new_user = self.__user_repository.add_new_user(user)
        self.__logger.info(f"New user ID: {new_user.user_id}")
        return new_user

    def get_users(self):
        users = self.__user_repository.get_users()
        return users

    def get_user_by_id(self, user_id: str):
        user = self.__user_repository.get_user_by_id(user_id)

        if user is None:
            raise UserNotFoundException()

        return user

    def get_user_by_login(self, login: str):
        user = self.__user_repository.get_user_by_login(login)

        if user is None:
            raise UserNotFoundException()

        return user

    def login(self, user: UserLogin):
        self.__logger.info(f"Login process for user: {user.user_id}")

        access_token = self.__access_token_business.create_access_token(user)
        user.access_token = access_token

        created = self.__user_repository.set_access_token(user, access_token)

        if not created:
            raise LoginException()

        return user
