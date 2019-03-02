import unittest

from unittest.mock import Mock, MagicMock, patch

from src.controllers.UserController import UserController


class TestUserController(unittest.TestCase):
    @patch('src.business.UserBusiness.UserBusiness')
    def setUp(self, user_business_mock):
        self.__user_business = user_business_mock
        self.__user_controller = UserController()

    def test_should_get_all_users(self):
        self.__user_controller.get_users()
        self.assertTrue(self.__user_business.get_users.called)


if __name__ == "__main__":
    unittest.main()
