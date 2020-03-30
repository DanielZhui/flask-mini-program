from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from index import route
import pymysql

from logs import setup_log

app = Flask(__name__)
app.register_blueprint(route, url_prefix='/api')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:macadmin@localhost:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
SQLALCHEMY_ECHO = True
db = SQLAlchemy(app)

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

@app.route('/create')
def create():
    # models
    class Person(db.Model):
        __tablename__ = 'persons'
        __table_args__ = {'extend_existing': True}
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(16))

    class Tag(db.Model):
        __tablename__ = "tag"
        __table_args__ = {'extend_existing': True}
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), unique=True)

    db.create_all()
    # db.drop_all()
    return 'success...'


if __name__ == "__main__":
    log_level = 'DEBUG'
    setup_log(log_level)
    app.run(debug=True)