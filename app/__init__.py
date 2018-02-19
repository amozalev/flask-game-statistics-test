from flask import Flask, url_for
from flask_admin import Admin
from flask_login import LoginManager
from flask_migrate import Migrate
from app.api.views import api as api_blueprint
from app.auth import auth as auth_blueprint
from .api.models import db
from app.admin.views import admin as admin_blueprint
from app.admin.views import MyAdminIndexView
import logging
from logging.handlers import RotatingFileHandler
import config
from .api.models import *

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(config.Config.LOGGING_LEVEL)
handler = RotatingFileHandler("application.log", maxBytes=config.Config.LOG_FILE_SIZE)
formatter = logging.Formatter(config.Config.LOGGING_FORMAT)
handler.setFormatter(formatter)

login_manager = LoginManager()
login_manager.session_protection = config.Config.SESSION_PROTECTION
login_manager.login_view = 'auth.login'

# Flask-admin index configuration
admin = Admin(template_mode='bootstrap3',
              name='Game statistics',
              index_view=MyAdminIndexView(url='/admin', template='my_index.html'))


def create_app():
    # Flask init
    app = Flask(__name__)
    app.config.from_object(config.Config)

    # Flask Migrate init
    migrate = Migrate(app, db)

    # Flask Admin init
    admin.init_app(app)

    from .auth import views

    login_manager.init_app(app)

    # Registering blueprints
    app.register_blueprint(api_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(auth_blueprint)


    db.init_app(app)
    # with app.app_context():
    #     db.metadata.drop_all(db.engine, tables=[
    #         EventType.__table__
    #     ])

    return app
