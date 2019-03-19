import unittest

from src.business.Validator import Validator
from src.models.models import UserLogin
from src.exceptions.exceptions import CannotBeBlankException


class TestValidator(unittest.TestCase):

    def setUp(self):
        self.__user = UserLogin("user_id", "name", "login", "password")

    def test_should_raise_blank_exception_user_add_with_none_name(self):
        user_json = {"login": "login", "password": "password"}
        self.assertRaises(CannotBeBlankException, Validator.validate_user_dict_add_user, user_json)

    def test_should_raise_blank_exception_user_add_with_blank_name(self):
        user_json = {"name": "  ", "login": "login", "password": "password"}
        self.assertRaises(CannotBeBlankException, Validator.validate_user_dict_add_user, user_json)

    def test_should_raise_blank_exception_user_add_with_none_login(self):
        user_json = {"name": "name", "password": "password"}
        self.assertRaises(CannotBeBlankException, Validator.validate_user_dict_add_user, user_json)

    def test_should_raise_blank_exception_user_add_with_blank_login(self):
        user_json = {"name": "name", "login": "  ", "password": "password"}
        self.assertRaises(CannotBeBlankException, Validator.validate_user_dict_add_user, user_json)

    def test_should_raise_blank_exception_user_add_with_none_password(self):
        user_json = {"name": "name", "login": "login"}
        self.assertRaises(CannotBeBlankException, Validator.validate_user_dict_add_user, user_json)

    def test_should_raise_blank_exception_user_add_with_blank_password(self):
        user_json = {"name": "name", "login": "login", "password": "  "}
        self.assertRaises(CannotBeBlankException, Validator.validate_user_dict_add_user, user_json)

    def test_should_raise_blank_exception_user_login_with_none_login(self):
        user_login = {"password": "password"}
        self.assertRaises(CannotBeBlankException, Validator.validate_user_dict_add_user, user_login)

    def test_should_raise_blank_exception_user_login_with_blank_login(self):
        user_login = {"login": "  ", "password": "password"}
        self.assertRaises(CannotBeBlankException, Validator.validate_user_dict_login, user_login)

    def test_should_raise_blank_exception_user_login_with_none_password(self):
        user_login = {"login": "login"}
        self.assertRaises(CannotBeBlankException, Validator.validate_user_dict_add_user, user_login)

    def test_should_raise_blank_exception_user_login_with_blank_password(self):
        user_login = {"login": "login", "password": "  "}
        self.assertRaises(CannotBeBlankException, Validator.validate_user_dict_login, user_login)

    def test_should_raise_blank_exception_access_token_with_none_login(self):
        user_login = {"access_token": "access_token"}
        self.assertRaises(CannotBeBlankException, Validator.validate_user_dict_add_user, user_login)

    def test_should_raise_blank_exception_access_token_with_blank_login(self):
        user_login = {"login": "  ", "access_token": "access_token"}
        self.assertRaises(CannotBeBlankException, Validator.validate_user_dict_login, user_login)

    def test_should_raise_blank_exception_access_token_with_none_access_token(self):
        user_login = {"login": "login"}
        self.assertRaises(CannotBeBlankException, Validator.validate_user_dict_add_user, user_login)

    def test_should_raise_blank_exception_access_token_with_blank_access_token(self):
        user_login = {"login": "login", "access_token": "  "}
        self.assertRaises(CannotBeBlankException, Validator.validate_user_dict_login, user_login)

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
