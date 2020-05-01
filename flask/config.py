# This holds the configuration (environment variables) information for the flask app

from dotenv import load_dotenv
import os
basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

class Config(object):
    # Security keys
    SECRET_KEY = os.environ.get('SECRET_KEY')
