import unittest

from src.business.AccessTokenBusiness import AccessTokenBusiness
from src.models.models import UserLogin

from unittest.mock import patch


class TestAccessTokenBusiness(unittest.TestCase):

    def setUp(self):
        self.__user = UserLogin("user_id", "name", "login", "password")
        self.__access_token_business = AccessTokenBusiness()

    @patch('src.business.AccessTokenBusiness.hashlib')
    def test_should_create_access_token(self, hashlib_mock):
        hashlib_instance = hashlib_mock.new.return_value

        self.__access_token_business.create_access_token(self.__user)

        self.assertTrue(hashlib_mock.new.called)
        self.assertTrue(hashlib_instance.update.called)
        self.assertTrue(hashlib_instance.hexdigest.called)


if __name__ == "__main__":
    unittest.main()
