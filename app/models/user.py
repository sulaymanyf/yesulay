"""
 Created by YefanSulayman on 2020/3/31 17:44.
"""
from tokenize import String

from sqlalchemy import Column, Integer, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash

from app.lib.error_code import AuthFailed
from app.models.base import Base, db

__author__ = 'YefanSulayman'


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    # auth 管理员或普通用户 1 普通 2 管理员
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(100))

    def keys(self):
        return ['id', 'email', 'nickname', 'auth']

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod  # 对象里面创建对象 时加上静态方法(类方法) 如果不喜欢静态方法 可以放在app/api/v1/clitent.py __register_user_by_email 方法中
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)

    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(email=email).first_or_404()
        if not user.check_password(password):
            raise AuthFailed()
        scope = 'AdminScope' if user.auth == 2 else 'UserScope'
        return {'uid': user.id, 'scope': scope}

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

    # def _set_fields(self):
    #     # self._exclude = ['_password']
    #     self._fields = ['_password', 'nickname']
