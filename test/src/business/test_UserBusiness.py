import unittest

from unittest.mock import patch

from src.business.UserBusiness import UserBusiness
from src.models.models import UserLogin


class TestUserBusiness(unittest.TestCase):

    @patch('src.business.UserBusiness.UserRepository')
    def setUp(self, user_repository_mock):
        self.__user_repository_instance = user_repository_mock.return_value
        self.__user_business = UserBusiness()

    def test_should_add_new_user(self):
        user = UserLogin(None, "name", "login", "password")
        new_user = UserLogin("user_id", "name", "login", "password")
        self.__user_repository_instance.get_user.return_value = None
        self.__user_repository_instance.add_new_user.return_value = new_user

        response = self.__user_business.add_new_user(user)

        self.assertTrue(self.__user_repository_instance.get_user.called)
        self.assertTrue(self.__user_repository_instance.add_new_user.called)
        self.assertEqual(new_user, response)

    def test_should_get_all_users(self):
        self.__user_repository_instance.get_users.return_value = []

        users = self.__user_business.get_users()

        self.assertTrue(self.__user_repository_instance.get_users.called)
        self.assertEqual([], users)
