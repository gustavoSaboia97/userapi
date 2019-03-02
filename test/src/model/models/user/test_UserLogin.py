import unittest

from src.models.models import UserLogin


class TestUserLogin(unittest.TestCase):

    def setUp(self):
        self.__user_login = UserLogin("user_id", "user_name", "login", "password")

    def test_should_set_correct_user_login(self):
        expected_hash = "password".__hash__()
        self.assertEqual(self.__user_login.user_id, "user_id", "Wrong User Id")
        self.assertEqual(self.__user_login.name, "user_name", "Wrong User Id")
        self.assertEqual(self.__user_login.login, "login", "Wrong Login")
        self.assertEqual(self.__user_login.password, expected_hash, "Wrong Password")

    def test_should_return_dict(self):
        data = self.__user_login.to_dict()
        self.assertEqual(data["id"], "user_id", "Wrong User Login Dict Return")
        self.assertEqual(data["name"], "user_name", "Wrong User Login Dict Return")
        self.assertEqual(data["login"], "login", "Wrong User Login Dict Return")


if __name__ == "__main__":
    unittest.main()
