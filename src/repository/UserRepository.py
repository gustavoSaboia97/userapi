from src.configuration.MongoConfiguration import MongoConfiguration
from src.models.models import UserLogin, User
from src.util.Logger import Logger


class UserRepository:

    def __init__(self):
        self.__logger = Logger().get_logger()
        self.__mongo_configuration = MongoConfiguration()
        self.__database = self.__mongo_configuration.database
        self.__user_collection = self.__database.user_collection
        self.__user_collection.create_index("login", unique=True)

    def add_new_user(self, user: UserLogin):
        self.__logger.info(f"Inserting new user: {user.login}")
        mongo_object_id = self.__user_collection.insert_one(user.to_mongo_dict()).inserted_id
        user.user_id = str(mongo_object_id)
        return user

    def get_users(self):
        self.__logger.info("Getting users from configuration")

        users = list()

        for document in self.__user_collection.find():
            user_id = str(document['_id'])
            name = str(document['name'])

            user = User(user_id, name)
            users.append(user)

        return users

    def get_user_by_login(self, login: str):
        self.__logger.info(f"Getting user by login: {login}")

        user = None

        for document in self.__user_collection.find({"login":login}):
            user_id = str(document["_id"])
            user_name = str(document["name"])
            user_login = str(document["login"])

            user = UserLogin(user_id, user_name, user_login, None)

        return user

    def get_user_by_id(self, id: str):
        self.__logger.info(f"Getting user by login: {id}")

        user = None

        for document in self.__user_collection.find({"_id":id}):
            user_id = str(document["_id"])
            user_name = str(document["name"])
            user_login = str(document["login"])

            user = UserLogin(user_id, user_name, user_login, None)

        return user
