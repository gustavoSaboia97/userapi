from flask import Blueprint, request

from src.controllers.UserController import UserController

user_blueprint = Blueprint("user_blueprint", __name__)

user_controller = UserController()

# @user_blueprint.route("/api/user",  methods=['POST', ])
# def new_user():
#     name = request.form['user_name']
#     login = request.form['user_login']
#     password = request.form['user_password']

#     user_controller = UserController()

#     return user_controller.add_new_user(name, login, password)


@user_blueprint.route("/api/user/", methods=['GET', ])
def get_users():
    return user_controller.get_users()


@user_blueprint.route("/api/user/<string:user_id>/",  methods=['GET', ])
def get_user(user_id):
    return "Returns Specific User data" + user_id


@user_blueprint.route("/api/user/login/", methods=['POST', ])
def user_login():
    return "User Login returns Access Token"


@user_blueprint.route("/api/user/access/", methods=['GET', ])
def user_access_token_verification():
    return "Verify if it is a valid access token"
