import unittest

from src.business.Validator import Validator
from src.models.models import UserLogin


class TestValidator(unittest.TestCase):

    def setUp(self):
        self.__user = UserLogin("user_id", "name", "login", "password")

    def test_should_return_false_to_correct_credentials(self):
        user = UserLogin("user_id", "name", "login", "password")
        user_login_information = UserLogin("user_id", "name", "login", "password")

        response = Validator.is_wrong_credentials(user, user_login_information)

        self.assertEqual(False, response)

    def test_should_return_true_to_wrong_login(self):
        user = UserLogin("user_id", "name", "login", "password")
        user_login_information = UserLogin("user_id", "name", "login2", "password")

        response = Validator.is_wrong_credentials(user, user_login_information)

        self.assertEqual(True, response)

    def test_should_return_true_to_wrong_password(self):
        user = UserLogin("user_id", "name", "login", "password")
        user_login_information = UserLogin("user_id", "name", "login", "password2")

        response = Validator.is_wrong_credentials(user, user_login_information)

        self.assertEqual(True, response)

    def test_should_return_false_to_correct_access_token(self):
        user = UserLogin("user_id", "name", "login", "password")
        user.access_token = "access_token"
        user_login_information = UserLogin("user_id", "name", "login", "password")
        user_login_information.access_token = "access_token"

        response = Validator.is_wrong_access_token(user, user_login_information)

        self.assertEqual(False, response)

    def test_should_return_true_to_wrong_access_token(self):
        user = UserLogin("user_id", "name", "login", "password")
        user.access_token = "access_token"
        user_login_information = UserLogin("user_id", "name", "login", "password")
        user_login_information.access_token = "access_token2"

        response = Validator.is_wrong_access_token(user, user_login_information)

        self.assertEqual(True, response)


if __name__ == "__main__":
    unittest.main()
