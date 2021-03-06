import unittest

from unittest.mock import patch

from src.controllers.UserController import UserController
from src.models.models import UserLogin, User


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

    def test_should_get_user_by_id(self):
        user = User("user_id", "name")
        self.__user_business_instance.get_user_by_id.return_value = user
        self.__user_controller.get_user_by_id("user_id")
        self.assertTrue(self.__user_business_instance.get_user_by_id.called)

    def test_should_login_an_user(self):
        login_json = {"login": "login", "password": "password"}
        user = UserLogin("user_id", "name", "login", "password")
        self.__user_business_instance.get_access_token.return_value = user

        response = self.__user_controller.login(login_json)

        self.assertTrue(self.__user_business_instance.authenticate.called)
        self.assertTrue(self.__user_business_instance.get_access_token.called)
        self.assertEqual(200, response.status_code)

    def test_should_validate_access_token(self):
        access_token_json = {"login": "login", "access_token": "access_token"}

        response = self.__user_controller.validate_token(access_token_json)

        self.assertTrue(self.__user_business_instance.get_user_by_login.called)
        self.assertTrue(self.__user_business_instance.validate_access_token.called)
        self.assertEqual(200, response.status_code)


if __name__ == "__main__":
    unittest.main()
