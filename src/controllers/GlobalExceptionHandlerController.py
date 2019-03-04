from src.exceptions.exceptions import UserApiException
from src.util.Logger import Logger
from json import dumps
from flask import Response


class GlobalExceptionHandlerController:

    def __init__(self):
        self.__logger = Logger().get_logger()

    def user_api_errors(self, error: UserApiException):
        self.__logger.error(f"Error during process: {error.message}")
        error_json = dumps(error.to_dict())

        return Response(error_json, status=error.status_code)

    def unknown_errors(self, error: Exception):
        self.__logger.error(f"Unknown exception: {str(error)}")

        return Response(str(error), status=500)
