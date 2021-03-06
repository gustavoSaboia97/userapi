import unittest

from unittest.mock import patch

from src.models.models import UserLogin
from src.repository.UserRepository import UserRepository


class TestUserRepository(unittest.TestCase):

    @patch('src.repository.UserRepository.MongoConfiguration')
    def setUp(self, mongo_configuration_mock):
        self.__mongo_configuration_instance = mongo_configuration_mock.return_value
        self.__database = mongo_configuration_mock.database
        self.__user_repository = UserRepository()

    def test_should_add_new_user(self):
        new_user = UserLogin("user_id", "name", "login", "password")

        self.__user_repository.add_new_user(new_user)

        self.assertTrue(self.__mongo_configuration_instance.database.user_collection.insert_one.called)

    def test_should_get_all_users(self):
        self.__user_repository.get_users()

        self.assertTrue(self.__mongo_configuration_instance.database.user_collection.find.called)

    def test_should_get_user_by_id(self):
        self.__user_repository.get_user_by_id("5c7c0c22fd8a2f36f6cdea65")

        self.assertTrue(self.__mongo_configuration_instance.database.user_collection.find.called)

    def test_should_update_access_token(self):
        user = UserLogin("5c7c0c22fd8a2f36f6cdea65", "name", "login", "password")
        user.access_token = "access_token"

        self.__user_repository.set_access_token(user)

        self.assertTrue(self.__mongo_configuration_instance.database.user_collection.update_one.called)
