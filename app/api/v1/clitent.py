"""
 Created by YefanSulayman on 2020/3/31 17:34.
"""
from flask import request

from app.lib.enums import ClientTypeEnum
from app.lib.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClitentForm

__author__ = 'YefanSulayman'

api = Redprint('client')


@api.route('register', methos=['POST'])
def create_client():
    data = request.json
    # 如果时json 的话 需要data=data 才行
    form = ClitentForm(data=data)
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email(form),
            ClientTypeEnum.USER_MINA: __register_user_by_mini
        }


def __register_user_by_email(form):
    # form 中没有nickname
    User.register_by_email(,form.account.data,form.secret.data)
    pass


def __register_user_by_mini():
    pass
