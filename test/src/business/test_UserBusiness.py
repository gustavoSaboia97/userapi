import unittest

from unittest.mock import patch

from src.business.UserBusiness import UserBusiness


class TestUserBusiness(unittest.TestCase):

    @patch('src.business.UserBusiness.UserRepository')
    def setUp(self, user_repository_mock):
        self.__user_repository_instance = user_repository_mock.return_value
        self.__user_business = UserBusiness()

    def test_should_get_all_users(self):
        self.__user_repository_instance.get_users.return_value = []
        users = self.__user_business.get_users()
        self.assertTrue(self.__user_repository_instance.get_users.called)
        self.assertEqual(users, [])
