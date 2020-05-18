# This creates the flask app instance

from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Import the configuration sets
from config import Config

# Create flask app instance
app = Flask(__name__)
app.config.from_object(Config)

# Attach socketio support to app
socketio = SocketIO(app)

# Attach db support to app
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import the modules to get them hooked in
from app import models, routes, events
