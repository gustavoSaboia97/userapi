import hashlib
import datetime

from src.models.models import UserLogin


class AccessTokenBusiness:

    def __init__(self, user: UserLogin):
        self.__access_token = str()
        self.__user = user

    def create_access_token(self):
        access_token_hash = hashlib.new('ripemd160')
        access_token_hash.update(bytes(self.__user.user_id, "utf-8"))
        access_token_hash.update(bytes(str(self.__user.password), "utf-8"))
        access_token_hash.update(bytes(str(datetime.datetime.now()), "utf-8"))
        self.__access_token = access_token_hash.hexdigest()
        return self.__access_token
