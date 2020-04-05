import os
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

class Application(Flask):
    def __init__(self, import_name, template_folder=None, root_path=None, static_path=None):
        super(Application, self).__init__(import_name, template_folder=template_folder, root_path=root_path)
        self.config.from_pyfile('config/base_setting.py')
        db.init_app(self)

BASE_DIR = os.getcwd()
db = SQLAlchemy()
app = Application(__name__, template_folder=BASE_DIR + '/web/templates', root_path=BASE_DIR)
manager = Manager(app)
