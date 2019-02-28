from flask import Blueprint

from src.models.models import Health

app_blueprint = Blueprint("app_blueprint", __name__)


@app_blueprint.route("/")
def welcome():
    return "Welcome To This User Management Service"


@app_blueprint.route("/api")
def presentation():
    return "API responsible for controlling Users Access"


@app_blueprint.route("/api/health")
def get_health_status():
    return str(Health())
