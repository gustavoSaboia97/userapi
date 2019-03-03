import unittest

from src.models.models import Health


class TestHealth(unittest.TestCase):

    def setUp(self):
        self.__health = Health()

    def test_should_return_health_json(self):
        self.assertEqual("{\"project\": \"User Management\", \"status\": \"UP\"}", str(self.__health))


if __name__ == "__main__":
    unittest.main()
