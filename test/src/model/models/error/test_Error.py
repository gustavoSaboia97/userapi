import unittest

from src.models.models import Error


class TestError(unittest.TestCase):

    def setUp(self):
        self.__error = Error("Error")

    def test_should_set_error_message(self):
        self.assertEqual(self.__error.message, "Error")


if __name__ == "__main__":
    unittest.main()
