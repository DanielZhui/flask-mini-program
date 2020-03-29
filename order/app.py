from flask import Flask, url_for
from index import route

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
    app.run()