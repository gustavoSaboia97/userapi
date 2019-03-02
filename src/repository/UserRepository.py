from src.configuration.MongoConfiguration import MongoConfiguration
from src.models.models import User
from src.util.Logger import Logger


class UserRepository:

    def __init__(self):
        self.__logger = Logger().get_logger()
        self.__mongo_configuration = MongoConfiguration()
        self.__database = self.__mongo_configuration.database
        self.__user_collection = self.__database.user_collection

    def get_users(self):
        self.__logger.info("Getting users from configuration")

        users = list()

        for document in self.__user_collection.find():
            user_id = str(document['_id'])
            name = str(document['name'])

            user = User(user_id, name)
            users.append(user)

        return users
