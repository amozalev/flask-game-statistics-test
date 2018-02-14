import os
from datetime import timedelta
import logging


class Config(object):
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = os.getenv('GAME_STAT_CSRF_SESSION_KEY')
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'dfgo78'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('GAME_STAT_DB')

    # Logging
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'application.log'
    LOGGING_LEVEL = logging.DEBUG
    LOG_FILE_SIZE = 10 * 1024 * 1024
