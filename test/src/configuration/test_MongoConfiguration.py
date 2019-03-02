import unittest

from pymongo.database import Database

from src.configuration.MongoConfiguration import MongoConfiguration


class TestMongoConfiguration(unittest.TestCase):

    def setUp(self):
        self.__mongo_configuration = MongoConfiguration()

    def test_should_return_mongo_database(self):
        self.assertEqual(type(self.__mongo_configuration.database), Database)


if __name__ == "__main__":
    unittest.main()
