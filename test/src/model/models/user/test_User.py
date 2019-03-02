import unittest
from src.models.models import User


class TestUserLogin(unittest.TestCase):

    def setUp(self):
        self.__user = User('user_id', 'user_name')

    def test_should_set_correct_user_login(self):
        self.assertEqual(self.__user.user_id, "user_id", "Wrong User Id")
        self.assertEqual(self.__user.name, "user_name", "Wrong User Id")

    def test_should_return_dict(self):
        data = self.__user.to_dict()
        self.assertEqual(data["id"], "user_id", "Wrong User Login Dict Return")
        self.assertEqual(data["name"], "user_name", "Wrong User Login Dict Return")


if __name__ == "__main__":
    unittest.main()
