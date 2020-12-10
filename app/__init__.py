from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


# initialzing application
app = Flask(__name__)


# Setting up configurations
app.config.from_object(DevConfig)

# initializing flask extensions
bootstrap.init_app(app)

from app import views

