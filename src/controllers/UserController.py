from json import dumps

from src.util.JsonObjectEncoder import JsonObjectEncoder

import logging


class UserController:

    def get_users(self):
        logging.info(f"GET all users from database")
        return dumps({"name":"Gustavo"})