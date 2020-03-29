import time
from flask import Flask, url_for
from index import route

from logs import setup_log

app = Flask(__name__)
app.register_blueprint(route, url_prefix='/api')


@app.route('/')
def index():
    url = url_for('index')
    print(url)
    return 'hello world', url

@app.route('/home')
def home():
    url = url_for('home')
    print(url)
    return 'welcome to home'

if __name__ == "__main__":
    log_level = 'DEBUG'
    setup_log(log_level)
    app.run(debug=True)