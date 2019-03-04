import unittest

from src.controllers.GlobalExceptionHandlerController import GlobalExceptionHandlerController
from src.exceptions.exceptions import UserApiException


class TestGlobalExceptionHandlerController(unittest.TestCase):

    def setUp(self):
        self.__exeption_handler = GlobalExceptionHandlerController()

    def test_should_return_an_response_with_error(self):
        user_api_exception = UserApiException("User Not Found", 404)
        response = self.__exeption_handler.user_api_errors(user_api_exception)
        self.assertEqual(404, response.status_code, "Wrong status code, expected 404")

    def test_should_return_status_500_unknow_error(self):
        response = self.__exeption_handler.unknown_errors(Exception())
        self.assertEqual(500, response.status_code, "Wrong status code, expected 500")
