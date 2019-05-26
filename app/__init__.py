from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap


app = Flask(__name__)

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

# Setting up configuration
app.config.from_object(DevConfig)

from app import views
from app import error