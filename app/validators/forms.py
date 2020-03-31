"""
 Created by YefanSulayman on 2020/3/31 16:53.
"""
from wtforms import Form, StringField, IntegerField, PasswordField, BooleanField
from wtforms.validators import DataRequired, length, email, EqualTo

from app.lib.enums import ClientTypeEnum

__author__ = 'YefanSulayman'


class ClitentForm(Form):
    account = StringField(validators=[DataRequired(), length(
        min=5, max=40
    )])
    email = StringField(validators=[email(), DataRequired()])
    secret = StringField()
    type = IntegerField(validators=[StringField()])
    password = PasswordField('New Password', [DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [DataRequired()])

    def ValidateType(self, value):
        try:
            # 查看是否时枚举中的值
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client
