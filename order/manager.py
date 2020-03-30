from app import app, manager
from flask_script import Server
import www


## web server
manager.add_command('runserver', Server(host='127.0.0.1', port=app.config['SERVER_PORT']), use_debug=True)

def main():
    manager.run()

if __name__ == "__main__":
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()