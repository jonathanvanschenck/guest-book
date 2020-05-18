# This holds the configuration (environment variables) information for the flask app

from dotenv import load_dotenv
import os
basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

class Config(object):
    # Security keys
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # SQL params
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                                'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
