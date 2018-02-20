import os
import logging


class Config(object):
    # Конечно же, это только для разработки
    HOST = '0.0.0.0'
    PORT = 8000

    TESTING = False
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = os.getenv('GAME_STAT_CSRF_SESSION_KEY')
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('GAME_STAT_DB')

    # Logging
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'application.log'
    LOGGING_LEVEL = logging.DEBUG
    LOG_FILE_SIZE = 10 * 1024 * 1024

    # Flask login
    SESSION_PROTECTION = 'strong'

    DATE_START = "2018-02-01"
    DATE_END = "2018-03-30"
