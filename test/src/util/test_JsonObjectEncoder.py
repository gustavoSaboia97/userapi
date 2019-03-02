import unittest

from unittest.mock import MagicMock

from src.models.models import User
from src.util.JsonObjectEncoder import JsonObjectEncoder


class TestJsonObjectEncoder(unittest.TestCase):

    def setUp(self):
        self.__user = User("user_id", "user_password")
        self.__json_object_encoder = JsonObjectEncoder()

    def test_should_encode_to_dict(self):
        self.__user.to_dict = MagicMock()
        self.__json_object_encoder.default(self.__user)
        self.assertTrue(self.__user.to_dict.called)


if __name__ == "__main__":
    unittest.main()
