from json import dumps

from flask import Response

from src.business.UserBusiness import UserBusiness
from src.business.Validator import Validator
from src.models.models import UserLogin
from src.util.JsonObjectEncoder import JsonObjectEncoder
from src.util.Logger import Logger


class UserController:

    def __init__(self):
        self.__user_bussiness = UserBusiness()
        self.__logger = Logger().get_logger()

    def add_new_user(self, user_json: dict):
        self.__logger.info(f"Adding an new user")
        Validator.validate_user_dict_add_user(user_json)
        user = UserLogin(None, user_json["name"], user_json["login"], user_json["password"])
        new_user = self.__user_bussiness.add_new_user(user)
        new_user_json = dumps(new_user, cls=JsonObjectEncoder)
        return Response(new_user_json, status=201)

    def get_users(self):
        self.__logger.info("GET all users from configuration")
        users = self.__user_bussiness.get_users()
        users_json = dumps(users, cls=JsonObjectEncoder)
        return Response(users_json, status=200)

    def get_user_by_id(self, user_id):
        self.__logger.info(f"GET user data from id: {user_id}")
        user = self.__user_bussiness.get_user_by_id(user_id)
        user_json = dumps(user, cls=JsonObjectEncoder)
        return Response(user_json, status=200)

    def login(self, login_json: dict):
        self.__logger.info(f"Login user: {login_json['login']}")
        Validator.validate_user_dict_login(login_json)
        user = UserLogin(None, None, login_json["login"], login_json["password"])
        user = self.__user_bussiness.authenticate(user)
        user = self.__user_bussiness.get_access_token(user)
        user_json = dumps(user.access_token_to_dict())
        return Response(user_json, status=200)

    def validate_token(self, access_token_json: dict):
        self.__logger.info(f"Validating access token user: {access_token_json['login']}")
        Validator.validate_user_dict_validate_access_token(access_token_json)
        user = UserLogin(None, None, access_token_json["login"], "")
        user.access_token = access_token_json["access_token"]
        self.__user_bussiness.get_user_by_login(user.login)
        self.__user_bussiness.validate_access_token(user)
        user_json = dumps(user.access_token_validate_to_dict())
        return Response(user_json, status=200)
