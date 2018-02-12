from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy.dialects.postgresql import TIMESTAMP

db = SQLAlchemy()


class Device(db.Model):
    __tablename__ = 'device'
    id = db.Column(db.Integer, db.Sequence('device_id_seq'), primary_key=True, nullable=False)
    name = db.Column(db.Text)
    event = db.relationship('Event', backref='device', lazy='dynamic')

    def __str__(self):
        return '{}'.format(self.name)


class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, db.Sequence('event_id_seq'), primary_key=True, nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'), nullable=False)
    name = db.Column(db.Text)
    timestamp = db.Column(db.TIMESTAMP)

    def __str__(self):
        return '{}, {}, {}'.format(self.name, self.timestamp, self.device_id)


class EventType(db.Model):
    id = db.Column(db.Integer, db.Sequence('event_type_id_seq'), primary_key=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
