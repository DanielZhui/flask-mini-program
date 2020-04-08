import os
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import pymysql

class Application(Flask):
    def __init__(self, import_name, template_folder=None, root_path=None):
        super(Application, self).__init__(import_name, template_folder=template_folder, root_path=root_path, static_folder=None)
        self.config.from_pyfile('config/base_setting.py')
        env = os.environ.get('ENV')
        if env:
            config_file = 'config/{}_setting.py'.format(env)
            self.config.from_pyfile(config_file, silent=True)
        db.init_app(self)

BASE_DIR = os.getcwd()
db = SQLAlchemy()
app = Application(__name__, template_folder=BASE_DIR + '/web/templates', root_path=BASE_DIR)
manager = Manager(app)

'''
增加函数模版
'''
from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')