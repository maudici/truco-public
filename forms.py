# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class PlayerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Add Player')

class GameForm(FlaskForm):
    winner1 = SelectField('Winner 1', [DataRequired()], choices=[], default='Select player')
    winner2 = SelectField('Winner 2', [DataRequired()], choices=[], default='Select player')
    loser1 = SelectField('Loser 1', [DataRequired()], choices=[], default='Select player')
    loser2 = SelectField('Loser 2', [DataRequired()], choices=[], default='Select player')
    submit = SubmitField('Record Game')

class FlowerForm(FlaskForm):
    player = SelectField('Player', [DataRequired()], choices=[], default='Select player')
    submit = SubmitField('Flor Quemada')
