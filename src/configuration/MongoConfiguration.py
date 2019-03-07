from pymongo import MongoClient

import os


class MongoConfiguration:

    def __init__(self):
        self.__database_uri = os.environ.get("DATABASE_URI")
        self.__mongo_client = MongoClient(self.__database_uri)
        self.__database = self.__mongo_client.users_database

    @property
    def database(self):
        return self.__database
