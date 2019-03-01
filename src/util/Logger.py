from flask import Flask
import logging


class Logger:
    
    def __init__(self):
        self.__app = Flask(__name__)
        self.__gunicorn_logger = logging.getLogger('gunicorn.error')
        self.__app.logger.handlers = self.__gunicorn_logger.handlers
        self.__app.logger.setLevel(self.__gunicorn_logger.level)

    def get_logger(self):
        return self.__app.logger
