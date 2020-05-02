# This creates the flask app instance

from flask import Flask
from flask_socketio import SocketIO

from config import Config

# Create a flask app instance
app = Flask(__name__)
app.config.from_object(Config)

# Attach socketio support to app
socketio = SocketIO(app)

# import all the modules to get them hooked in
from app import routes, models, events
