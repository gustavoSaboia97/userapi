import hashlib
import datetime

from src.models.models import UserLogin
from src.util.Logger import Logger


class AccessTokenBusiness:

    def __init__(self):
        self.__logger = Logger().get_logger()
        self.__access_token = str()

    def create_access_token(self, user: UserLogin):
        self.__logger.info(f"Generating access token for user: {user.user_id}")
        access_token_hash = hashlib.sha256()
        access_token_hash.update(bytes(user.login, "utf-8"))
        access_token_hash.update(bytes(str(user.password), "utf-8"))
        access_token_hash.update(bytes(str(datetime.datetime.now()), "utf-8"))
        self.__access_token = access_token_hash.hexdigest()
        return self.__access_token
