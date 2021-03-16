from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class RegForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    second_password = PasswordField('Повторите пароль', validators=[DataRequired(),
                                                                    EqualTo(fieldname='password',
                                                                            message='Пароли не совпадают.')])
    submit = SubmitField('Зарегистрироваться')
