from flask import Blueprint, render_template

api = Blueprint('api', __name__, template_folder='templates')


@api.route('/')
def index():
    print('hello')
    # return render_template('index.html')
    return 'Hello!'
