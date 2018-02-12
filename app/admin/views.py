from flask import Blueprint
from flask_admin import AdminIndexView, expose

admin = Blueprint('adminpanel', __name__, template_folder='templates')


# @admin.route('/')
# def index():
#     print('hello admin')
#     # return render_template('index.html')
#     return 'Hello!'


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        return super(MyAdminIndexView, self).index()
