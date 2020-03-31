"""
 Created by YefanSulayman on 2020/3/31 16:14.
"""
from flask import Blueprint

from app.api.v1 import user, book

__author__ = 'YefanSulayman'


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    # 红图注册到蓝图
    user.api.register(bp_v1)
    book.api.register(bp_v1)
    return bp_v1
