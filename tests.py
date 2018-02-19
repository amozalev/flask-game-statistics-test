import unittest
from manage import app
from app.api.models import db


class Test(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.init_app(self.app)
        db.drop_all()
        db.session.commit()

    def tearDown(self):
        db.create_all()
        db.session.commit()


if __name__ == '__main__':
    unittest.main()
