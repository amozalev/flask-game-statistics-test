from flask import Blueprint, request, render_template, current_app
from sqlalchemy.exc import SQLAlchemyError
from .models import *
from .forms import DatesForm
import json

api = Blueprint('api', __name__, template_folder='templates')


@api.route('/', methods=['GET', 'POST'])
def index():
    dates_form = DatesForm(request.form)
    return render_template('index.html',
                           dates_form=dates_form)


@api.route('/get_devices_per_day', methods=['POST'])
def get_devices_per_day():
    dates_form = DatesForm(request.form)

    date_start = request.form['date_start']
    date_end = request.form['date_end']

    # data = request.form
    # for i, j in data.items():
    #     date_start = i[]
    #     print(i, j)
    print(date_start, date_end)

    return render_template('index.html',
                           dates_form=dates_form)




@api.route('/events', methods=['POST', 'GET'])
def event():
    # json_data = request.get_json()

    json_data = [{'device_id': '123abc', 'name': 'AppStart', 'timestamp': '2018-03-01 12:00'},
                 {'device_id': '987654dfg', 'name': 'LevelStart', 'timestamp': '2018-03-01 11:10', 'level_name': 1}]

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
