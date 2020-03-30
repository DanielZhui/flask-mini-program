from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from web.controllers.index import route_index

# flask 源码解析, 类集成 以及配置文件的加载
class Application(Flask):
    def __init__(self, import_name):
        super(Application, self).__init__(import_name)
        self.config.from_pyfile('config/base_setting.py')
        db.init_app(self)

db = SQLAlchemy()
app = Application(__name__)
app.register_blueprint(route_index, url_prefix='/')
manager = Manager(app)
