from application import db

class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nikename = db.Column(db.String(64), nullable=False)
    mobile = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    # flask 有无类似 django choice 选项
    sex = db.Column(db.Integer, nullable=False)
    avatar = db.Column(db.String(200), nullable=False)
    login_name = db.Column(db.String(32), nullable=False)
    login_pwd = db.Column(db.String(32), nullable=False)
    login_salt = db.Column(db.String(32), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)