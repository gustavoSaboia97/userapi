import unittest

from src.models.models import UserAccessToken


class TestUserAccessToken(unittest.TestCase):

    def setUp(self):
        self.__user_access_token = UserAccessToken("user_id", "user_name")

    def test_should_set_correct_user_access_token_data(self):
        self.assertEqual(self.__user_access_token.user_id, "user_id", "Wrong User Access Token ID")
        self.assertEqual(self.__user_access_token.name, "user_name", "Wrong User Access Token Name")

    def test_should_set_access_token_as_string(self):
        self.assertEqual(type(self.__user_access_token.access_token), str, "Wrong Access Token Type")

    def test_should_return_dict(self):
        data = self.__user_access_token.to_dict()
        self.assertEqual(data["id"], "user_id", "Wrong User Login Dict Return")
        self.assertEqual(data["name"], "user_name", "Wrong User Login Dict Return")


if __name__ == "__main__":
    unittest.main()
