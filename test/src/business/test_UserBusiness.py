import unittest

from unittest.mock import patch

from src.business.UserBusiness import UserBusiness
from src.exceptions.exceptions import UserAlreadyExistsException, UserNotFoundException, \
    AccessTokenException, AuthenticationException
from src.models.models import UserLogin


class TestUserBusiness(unittest.TestCase):

    @patch('src.business.UserBusiness.UserRepository')
    def setUp(self, user_repository_mock):
        self.__user_repository_instance = user_repository_mock.return_value
        self.__user_business = UserBusiness()

    def test_should_raise_that_user_exists(self):
        user = UserLogin(None, "name", "login", "password")
        new_user = UserLogin("user_id", "name", "login", "password")
        self.__user_repository_instance.get_user_by_login.return_value = new_user

        self.assertRaises(UserAlreadyExistsException, self.__user_business.add_new_user, user)

    def test_should_add_new_user(self):
        user = UserLogin(None, "name", "login", "password")
        new_user = UserLogin("user_id", "name", "login", "password")
        self.__user_repository_instance.get_user_by_login.return_value = None
        self.__user_repository_instance.add_new_user.return_value = new_user

        response = self.__user_business.add_new_user(user)

        self.assertTrue(self.__user_repository_instance.get_user_by_login.called)
        self.assertTrue(self.__user_repository_instance.add_new_user.called)
        self.assertEqual(new_user, response)

    def test_should_get_all_users(self):
        self.__user_repository_instance.get_users.return_value = []

        response = self.__user_business.get_users()

        self.assertTrue(self.__user_repository_instance.get_users.called)
        self.assertEqual([], response)

    def test_should_get_user_by_id(self):
        user = UserLogin("user_id", "name", "login", "password")
        self.__user_repository_instance.get_user_by_id.return_value = user

        response = self.__user_business.get_user_by_id("user_id")

        self.assertTrue(self.__user_repository_instance.get_user_by_id.called)
        self.assertEqual(user, response)

    def test_should_raise_user_not_found(self):
        self.__user_repository_instance.get_user_by_id.return_value = None

        self.assertRaises(UserNotFoundException, self.__user_business.get_user_by_id, "user_id")

    def test_should_pass_into_authentication(self):
        user = UserLogin("user_id", "name", "login", "password")
        user_login_information = UserLogin("user_id", "name", "login", "password")

        self.__user_repository_instance.get_user_by_id.return_value = user_login_information

        self.__user_business.authenticate(user)

        self.assertTrue(self.__user_repository_instance.get_user_by_id.called)

    def test_should_raise_authentication_exception(self):
        user = UserLogin("user_id", "name", "login", "password")
        user_login_information = UserLogin("user_id", "name", "login", "password2")

        self.__user_repository_instance.get_user_by_id.return_value = user_login_information

        self.assertRaises(AuthenticationException, self.__user_business.authenticate, user)

    def test_should_get_access_token(self):
        user = UserLogin("user_id", "name", "login", "password")

        self.__user_repository_instance.set_access_token.return_value = user

        response = self.__user_business.get_access_token(user)

        self.assertTrue(self.__user_repository_instance.set_access_token.called)
        self.assertEqual(user, response)

    def test_should_raise_access_token_exception(self):
        user = UserLogin("user_id", "name", "login", "password")

        self.__user_repository_instance.set_access_token.return_value = None

        self.assertRaises(AccessTokenException, self.__user_business.get_access_token, user)


if __name__ == "__main__":
    unittest.main()
