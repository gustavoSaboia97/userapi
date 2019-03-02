from json import dumps

from src.business.UserBusiness import UserBusiness
from src.util.JsonObjectEncoder import JsonObjectEncoder
from src.util.Logger import Logger


class UserController:

    def __init__(self):
        self.__user_bussiness = UserBusiness()
        self.__logger = Logger().get_logger()

    def get_users(self):
        self.__logger.info("GET all users from configuration")
        users = self.__user_bussiness.get_users()
        return dumps(users, cls=JsonObjectEncoder)
