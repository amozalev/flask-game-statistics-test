import unittest
from manage import app
from app.api.models import db


class Test(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
