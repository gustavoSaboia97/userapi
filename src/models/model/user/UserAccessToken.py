from .User import User

import hashlib
import datetime


class UserAccessToken(User):

    def __init__(self, user_id: str, name: str):
        super().__init__(user_id, name)
        self.__get_access_token()

    @property
    def access_token(self):
        return self.__access_token

    def __get_access_token(self):
        access_token_hash = hashlib.new('ripemd160')
        access_token_hash.update(bytes(self.user_id, "utf-8"))
        access_token_hash.update(bytes(str(datetime.datetime.now()), "utf-8"))
        self.__access_token = access_token_hash.hexdigest()

    def to_dict(self):
        return {
            "id": self.user_id,
            "name": self.name,
            "access_token": self.access_token
        }
