import unittest
from manage import app
from app.api.models import db
import json
import os
import config


class Test(unittest.TestCase):
    def setUp(self):
        app.config['LOGIN_DISABLED'] = True
        app.config['SECRET_KEY'] = 'secret_key'
        app.config['CSRF_SESSION_KEY'] = 'secret_key'
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('GAME_STAT_DB')
        app.login_manager.init_app(app)

        self.app = app.test_client()
        self.app.testing = True

        with app.app_context():
            '''
            Необходимо использовать raw sql для удаления sequences, в связи с тем, что
            db.drop_all() пытается удалить sequence перед удалением зависимой от неё таблицы,
            что приводит к ошибке. Это наиболее простое решение.
            '''
            db.engine.execute('DROP SEQUENCE IF EXISTS device_id_seq CASCADE;')
            db.engine.execute('DROP SEQUENCE IF EXISTS event_id_seq CASCADE;')
            db.engine.execute('DROP SEQUENCE IF EXISTS event_type_id_seq CASCADE;')
            db.drop_all()
            db.create_all()
            db.session.commit()

    def tearDown(self):
        pass

    def test_api_events(self):
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

        response = self.app.post('/events', data=json.dumps(json_data), follow_redirects=True)
        resp = json.loads(response.data)
        self.assertEqual(resp['success'], True)

    def test_api_get_data(self):
        pass


if __name__ == '__main__':
    unittest.main()
