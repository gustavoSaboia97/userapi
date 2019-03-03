import unittest

from pymongo.database import Database

from src.configuration.MongoConfiguration import MongoConfiguration


class TestMongoConfiguration(unittest.TestCase):

    def setUp(self):
        self.__mongo_configuration = MongoConfiguration()

    def test_should_return_mongo_database(self):
        self.assertEqual(Database, type(self.__mongo_configuration.database))


if __name__ == "__main__":
    unittest.main()
