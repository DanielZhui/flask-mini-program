import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Server

import www
from application import app, db, manager
# 导入模型
from common.models import User
from common.models.log import AppLog

## manager cmd
Migrate(app, db)
manager.add_command('runserver', Server(host='127.0.0.1', port=app.config['SERVER_PORT']), use_debug=True)
manager.add_command('db', MigrateCommand)

def main():
    manager.run()

if __name__ == "__main__":
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()