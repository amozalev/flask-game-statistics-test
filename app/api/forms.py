from flask_wtf import FlaskForm
from wtforms import DateField


class DatesForm(FlaskForm):
    date_start = DateField('date_start')
    date_end = DateField('date_end')
