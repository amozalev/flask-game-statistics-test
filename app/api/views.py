from flask import Blueprint, request, render_template, current_app
from flask_login import login_required
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from .models import *
from .forms import DatesForm
from datetime import *
import json

api = Blueprint('api', __name__, template_folder='templates')


@api.route('/', methods=['GET', 'POST'])
@login_required
def index():
    dates_form = DatesForm(request.form)
    return render_template('index.html',
                           dates_form=dates_form,
                           data=None)


@api.route('/get_devices_per_day', methods=['POST'])
@login_required
def get_devices_per_day():
    dates_form = DatesForm(request.form)

    date_start = datetime.now()
    date_end = datetime.now()

    if request.form['date_start'] and request.form['date_end']:
        date_start = request.form['date_start']
        date_end = request.form['date_end']

    query = db.session.query(func.Date(Event.timestamp), func.count(Device.name)). \
        join(Device). \
        filter(Event.timestamp >= "2018-02-01",
               Event.timestamp <= "2018-03-30"). \
        group_by(func.Date(Event.timestamp)). \
        order_by(func.Date(Event.timestamp))

    data = list()
    data.append(['Date', "Устройства"])
    for i in query:
        dttm = datetime.strftime(i[0], "%Y-%m-%d")
        data.append([dttm, i[1]])

    return render_template('index.html',
                           dates_form=dates_form,
                           data={'data': json.dumps(data)})


@api.route('/events', methods=['POST'])
@login_required
def event():
    json_data = request.get_json()

    json_data = [{'device_id': '1', 'name': 'AppStart', 'timestamp': '2018-03-01 12:00'},
                 {'device_id': '2', 'name': 'LevelStart', 'timestamp': '2018-03-01 11:10', 'level_name': 1},
                 {'device_id': '3', 'name': 'LevelStart', 'timestamp': '2018-03-01 11:10', 'level_name': 1},
                 {'device_id': '4', 'name': 'LevelStart', 'timestamp': '2018-02-15 11:10', 'level_name': 2},
                 {'device_id': '1', 'name': 'LevelStart', 'timestamp': '2018-03-04 12:10', 'level_name': 1},
                 {'device_id': '2', 'name': 'LevelStart', 'timestamp': '2018-02-10 11:10', 'level_name': 4},
                 {'device_id': '3', 'name': 'LevelStart', 'timestamp': '2018-02-01 11:10', 'level_name': 1},
                 {'device_id': '4', 'name': 'LevelStart', 'timestamp': '2018-02-10 11:10', 'level_name': 4},
                 {'device_id': '1', 'name': 'LevelStart', 'timestamp': '2018-03-02 10:10', 'level_name': 1},
                 {'device_id': '2', 'name': 'LevelStart', 'timestamp': '2018-02-01 15:10', 'level_name': 3},
                 {'device_id': '3', 'name': 'LevelStart', 'timestamp': '2018-02-09 19:00', 'level_name': 2},
                 {'device_id': '4', 'name': 'LevelStart', 'timestamp': '2018-02-10 12:10', 'level_name': 1},
                 {'device_id': '1', 'name': 'LevelStart', 'timestamp': '2018-02-18 16:10', 'level_name': 3},
                 {'device_id': '2', 'name': 'LevelStart', 'timestamp': '2018-03-01 11:10', 'level_name': 1},
                 {'device_id': '3', 'name': 'LevelStart', 'timestamp': '2018-03-03 13:10', 'level_name': 1},
                 {'device_id': '4', 'name': 'LevelStart', 'timestamp': '2018-04-01 11:10', 'level_name': 2},
                 {'device_id': '1', 'name': 'LevelStart', 'timestamp': '2018-02-01 12:10', 'level_name': 1}
                 ]

    for event in json_data:
        # Проверка на наличие event_type в Events
        event_query = EventType.query.filter_by(name=event['name']).first()
        if event_query is None:
            new_event_type = EventType(name=event['name'])
            try:
                db.session.add(new_event_type)
                db.session.commit()
            except SQLAlchemyError as error:
                db.session.rollback()
                current_app.logger.error('Error during the new_event_type insertion : %s', error, exc_info=True)
            event_query = EventType.query.filter_by(name=event['name']).first()
        event_type_id = event_query.id

        # Проверка на наличие device_id в Devices
        device_query = Device.query.filter_by(name=event['device_id']).first()
        if device_query is None:
            new_device = Device(name=event['device_id'])
            try:
                db.session.add(new_device)
                db.session.commit()
            except SQLAlchemyError as error:
                db.session.rollback()
                current_app.logger.error('Error during the new_device insertion : %s', error, exc_info=True)
            device_query = Device.query.filter_by(name=event['device_id']).first()
        device_id = device_query.id

        if 'level_name' in event:
            level_name = event['level_name']
        else:
            level_name = None

        # Добавление нового event
        try:
            new_event = Event(device_id=device_id,
                              event_type_id=event_type_id,
                              timestamp=event['timestamp'],
                              level_name=level_name)
            db.session.add(new_event)
            db.session.commit()
        except SQLAlchemyError as error:
            db.session.rollback()
            current_app.logger.error('Error during the event insertion : %s', error, exc_info=True)

    return 'events'
