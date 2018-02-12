from flask import Flask, url_for
from flask_admin import Admin
from flask_migrate import Migrate
from app.api.views import api as api_blueprint
from .api.models import db
from app.admin.views import admin as admin_blueprint
from app.admin.views import MyAdminIndexView
import config

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

    # Registering blueprints
    app.register_blueprint(api_blueprint)
    app.register_blueprint(admin_blueprint)

    db.init_app(app)

    return app
