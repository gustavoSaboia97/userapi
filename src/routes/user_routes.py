from flask import Blueprint, request

from src.controllers.GlobalExceptionHandlerController import GlobalExceptionHandlerController
from src.controllers.UserController import UserController
from src.exceptions.exceptions import UserApiException

user_blueprint = Blueprint("user_blueprint", __name__)

user_controller = UserController()
exception_handler = GlobalExceptionHandlerController()


@user_blueprint.route("/api/user/",  methods=['POST', ])
def new_user():
    user_json = request.json
    return user_controller.add_new_user(user_json)


@user_blueprint.route("/api/user/", methods=['GET', ])
def get_users():
    return user_controller.get_users()


@user_blueprint.route("/api/user/<string:user_id>/",  methods=['GET', ])
def get_user(user_id):
    return user_controller.get_user_by_id(user_id)


@user_blueprint.route("/api/user/login/", methods=['POST', ])
def user_login():
    login_json = request.json
    return user_controller.login(login_json)


@user_blueprint.route("/api/user/login/validate/", methods=['POST', ])
def user_access_token_verification():
    access_token_json = request.json
    return user_controller.validate_token(access_token_json)


@user_blueprint.errorhandler(UserApiException)
def user_api_error_handler(error):
    return exception_handler.user_api_errors(error)


@user_blueprint.errorhandler(Exception)
def unknown_error_handler(error):
    return exception_handler.unknown_errors(error)
