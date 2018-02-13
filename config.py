import os
from datetime import timedelta
import logging


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:somePass9@localhost/game_stat'

    # Logging
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'application.log'
    LOGGING_LEVEL = logging.DEBUG
    LOG_FILE_SIZE = 10 * 1024 * 1024
