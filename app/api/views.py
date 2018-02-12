from flask import Blueprint, render_template

api = Blueprint('api', __name__, template_folder='templates')


@api.route('/')
def index():
    print('hello')
    # return render_template('index.html')
    return 'Hello!'


@api.route('/events', methods=['POST'])
def event(json_data):
    # json_data = ['AppStart': {
    #                              'device_id': 2, 'name': 3, 'timestamp': '2018-03-01'},
    #                          'LevelStart': {'level_name': 1, 'device_id': 2, 'name': 3, 'timestamp': '2018-03-01'}]
    # for event in json_data:
    #     pass
    pass
