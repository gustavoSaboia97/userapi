import unittest

from unittest.mock import patch

from src.controllers.UserController import UserController


class TestUserController(unittest.TestCase):

    @patch('src.controllers.UserController.UserBusiness')
    def setUp(self, user_business_mock):
        self.__user_business_instance = user_business_mock.return_value
        self.__user_controller = UserController()

    def test_should_get_all_users(self):
        self.__user_business_instance.get_users.return_value = []
        self.__user_controller.get_users()
        self.assertTrue(self.__user_business_instance.get_users.called)


if __name__ == "__main__":
    unittest.main()
