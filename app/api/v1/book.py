"""
 Created by YefanSulayman on 2020/3/31 16:14.
"""
from app.lib.redprint import Redprint

__author__ = 'YefanSulayman'

api = Redprint('book')


@api.route('', methods=['GET'])
def book():
    return {'book': 'quran'}
