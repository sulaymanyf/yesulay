from flask import Flask as Flask


def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    # 蓝图注册到app
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    #  需要使用with语句 创建上下文环境
    with app.app_context():
        db.create_all()


def create_app():
    print("sss")
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    register_blueprints(app)
    register_plugin(app)
    return app
