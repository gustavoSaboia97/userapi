import unittest

from unittest.mock import patch

from src.controllers.UserController import UserController
from src.models.models import UserLogin


class TestUserController(unittest.TestCase):

    @patch('src.controllers.UserController.UserBusiness')
    def setUp(self, user_business_mock):
        self.__user_business_instance = user_business_mock.return_value
        self.__user_controller = UserController()

    def test_should_add_new_user(self):
        user_json = {"name": "name", "login": "login", "password": "password"}
        new_user = UserLogin("user_id", "name", "login", "password")
        self.__user_business_instance.add_new_user.return_value = new_user

        response = self.__user_controller.add_new_user(user_json)

        self.assertTrue(self.__user_business_instance.add_new_user.called)
        self.assertEqual(201, response.status_code)

    def test_should_get_all_users(self):
        self.__user_business_instance.get_users.return_value = []
        self.__user_controller.get_users()
        self.assertTrue(self.__user_business_instance.get_users.called)


if __name__ == "__main__":
    unittest.main()
