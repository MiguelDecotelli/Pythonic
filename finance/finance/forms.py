from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo
from finance.models import User
from finance.my_functions import apology

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder":"Username", "autocomplete": False})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder":"Password"})
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder":"Username", "autocomplete": False})
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Password must match!')], render_kw={"placeholder":"Password"})
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()], render_kw={"placeholder":"Confirm password"})
    submit = SubmitField('Register')

    def check_username(self, field):
        # Check if not None for that username!
        if User.query.filter_by(username=field.data).first():
            return apology('Sorry, that username is taken!')
        
class QuoteForm(FlaskForm):
    symbol = StringField('Symbol', validators=[DataRequired()], render_kw={"placeholder":"Symbol", "autocomplete": False, "autofocus": True})
    submit = SubmitField('Quote')

class BuyForm(FlaskForm):
    symbol = StringField('Symbol', validators=[DataRequired()], render_kw={"placeholder":"Symbol", "autocomplete": False, "autofocus": True})
    shares = IntegerField('Shares', validators=[DataRequired()], render_kw={"placeholder":"Shares", "min":1, "autocomplete": False})
    submit = SubmitField('Buy')

class SellForm(FlaskForm):
    symbol = StringField('Symbol', validators=[DataRequired()], render_kw={"placeholder":"Symbol", "autocomplete": False, "autofocus": True})
    shares = IntegerField('Shares', validators=[DataRequired()], render_kw={"placeholder":"Shares", "min":1, "autocomplete": False})
    submit = SubmitField('Sell')