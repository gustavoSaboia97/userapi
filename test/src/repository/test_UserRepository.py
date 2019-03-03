import unittest

from unittest.mock import patch, MagicMock

from src.repository.UserRepository import UserRepository


class TestUserRepository(unittest.TestCase):

    @patch('src.repository.UserRepository.MongoConfiguration')
    def setUp(self, mongo_configuration_mock):
        self.__mongo_configuration_instance = mongo_configuration_mock.return_value
        self.__user_repository = UserRepository()

    def test_should_get_all_users(self):
        self.__user_repository.get_users()
        self.assertTrue(self.__mongo_configuration_instance.database.user_collection.find.called)

