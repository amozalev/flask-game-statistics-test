from flask import Flask, url_for
from flask_admin import Admin
from app.api.views import api as api_blueprint
from app.admin.views import admin as admin_blueprint
from app.admin.views import MyAdminIndexView

# Flask-admin configuration
admin = Admin(template_mode='bootstrap3',
              name='Game statistics',
              index_view=MyAdminIndexView(url='/admin', template='my_index.html'))


def create_app():
    app = Flask(__name__)

    admin.init_app(app)

    # Registering blueprints
    app.register_blueprint(api_blueprint)
    app.register_blueprint(admin_blueprint)

    return app
