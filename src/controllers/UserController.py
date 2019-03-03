from json import dumps

from flask import Response

from src.business.UserBusiness import UserBusiness
from src.models.models import UserLogin
from src.util.JsonObjectEncoder import JsonObjectEncoder
from src.util.Logger import Logger


class UserController:

    def __init__(self):
        self.__user_bussiness = UserBusiness()
        self.__logger = Logger().get_logger()

    def add_new_user(self, user_json: dict):
        self.__logger.info(f"Adding an new user")
        user = UserLogin(None, user_json["name"], user_json["login"], user_json["password"])
        new_user = self.__user_bussiness.add_new_user(user)
        new_user_json = dumps(new_user, cls=JsonObjectEncoder)
        return Response(new_user_json, status=201)

    def get_users(self):
        self.__logger.info("GET all users from configuration")
        users = self.__user_bussiness.get_users()
        return dumps(users, cls=JsonObjectEncoder)
