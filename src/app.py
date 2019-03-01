from flask import Flask

from src.routes.start_routes import app_blueprint
from src.routes.user_routes import user_blueprint

app = Flask(__name__)

app.register_blueprint(app_blueprint)
app.register_blueprint(user_blueprint)
