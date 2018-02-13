from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Device(db.Model):
    __tablename__ = 'device'
    id = db.Column(db.Integer, db.Sequence('device_id_seq'), primary_key=True, nullable=False)
    name = db.Column(db.Text)
    event = db.relationship('Event', backref='device', lazy='dynamic')

    def __repr__(self):
        return '{}'.format(self.name)


class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, db.Sequence('event_id_seq'), primary_key=True, nullable=False)
    device_id = db.Column(db.Text, db.ForeignKey('device.id'), nullable=False)
    event_type_id = db.Column(db.Integer, db.ForeignKey('event_type.id'), nullable=False)
    timestamp = db.Column(db.TIMESTAMP)
    level_name = db.Column(db.Text, nullable=True)

    def __str__(self):
        return '{}, {}, {}'.format(self.name, self.timestamp, self.device_id)


class EventType(db.Model):
    __tablename__ = 'event_type'
    id = db.Column(db.Integer, db.Sequence('event_type_id_seq'), primary_key=True)
    name = db.Column(db.Text, nullable=False)
    event = db.relationship('Event', backref='event_type', lazy='dynamic')

    def __repr__(self):
        return '{}'.format(self.name)
