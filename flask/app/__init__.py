# This creates the flask app instance

from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

# Create a flask app instance
app = Flask(__name__)
app.config.from_object(Config)

# Attach socketio support to app
socketio = SocketIO(app)

# Attach db support to app
db = SQLAlchemy(app)
migrate = Migrate(app,db)

# import all the modules to get them hooked in
from app import routes, models, events
