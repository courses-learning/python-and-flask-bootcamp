from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    desc = StringField('Description of task: ')
    submit = SubmitField('Add')


class DelForm(FlaskForm):

    id = IntegerField('ID number of task to remove: ')
    submit = SubmitField('Remove')


class PersonForm(FlaskForm):

    name = StringField('Name: ')
    assigned_task = IntegerField('Single task ID: ')
    submit = SubmitField('Submit')
