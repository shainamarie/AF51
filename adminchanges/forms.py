from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from app import User



class CreateAccount(FlaskForm):
    firstname = StringField('FIRST NAME', validators=[DataRequired(), Length(min=1, max=50)])
    middlename = StringField('MIDDLE NAME', validators=[DataRequired(), Length(min=1, max=50)])
    lastname = StringField('LAST NAME', validators=[DataRequired(), Length(min=1, max=50)])
    username = StringField('USERNAME', validators=[DataRequired(), Length(min=4, max=25)])
    officerrole = StringField('Officer Type of Role', validators=[DataRequired(), Length(min=3, max=50)])

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username Already Exists')

    def validate_password(self, field):
        if User.query.filter_by(password=field.data).first():
            raise ValidationError('Password Already Taken')

class EditForm(FlaskForm):
    firstname = StringField('FIRST NAME', validators=[DataRequired(), Length(min=1, max=50)])
    middlename = StringField('MIDDLE NAME', validators=[DataRequired(), Length(min=1, max=50)])
    lastname = StringField('LAST NAME', validators=[DataRequired(), Length(min=1, max=50)])
    officerrole = StringField('Officer Type of Role', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('PASSWORD', validators=[DataRequired(), Length(min=6, max=32)])
    repeatpass = PasswordField('REPEAT PASSWORD', validators=[DataRequired(), EqualTo('password', message="Password must MATCH")])

    def validate_password(self, field):
        if User.query.filter_by(password=field.data).first():
            raise ValidationError('Password Already Taken')




