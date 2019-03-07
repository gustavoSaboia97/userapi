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

    def test_should_set_correct_user_login(self):
        expected_hash = "password".__hash__()
        self.assertEqual(self.__user_login.user_id, "user_id", "Wrong User Id")
        self.assertEqual(self.__user_login.name, "user_name", "Wrong User Id")
        self.assertEqual(self.__user_login.login, "login", "Wrong Login")
        self.assertEqual(self.__user_login.password, expected_hash, "Wrong Password")

    def test_should_set_int_password(self):
        expected_hash = "password".__hash__()
        self.__user_login.password = expected_hash
        self.assertEqual(expected_hash, self.__user_login.password)

    def test_should_return_dict(self):
        data = self.__user_login.to_dict()
        self.assertEqual("user_id", data["id"], "Wrong User Login Dict Return")
        self.assertEqual("user_name", data["name"], "Wrong User Login Dict Return")
        self.assertEqual("login", data["login"], "Wrong User Login Dict Return")


if __name__ == "__main__":
    unittest.main()
