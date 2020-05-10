from application import db

class AppAccessLog(db.Model):
    __tablename__ = 'app_access_log'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.BigInteger, nullable=False)
    referrer_url = db.Column(db.String(255), nullable=False)
    target_url = db.Column(db.String(255), nullable=False)
    query_parma = db.Column(db.Text, nullable=False)
    user_agent = db.Column(db.String(255), nullable=False)
    ip = db.Column(db.String(32), nullable=False)
    created_time = db.Column(db.DateTime, nullable=True)
    

class AppErrorLog(db.Model):
    __tablename__ = 'app_error_log'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.BigInteger, nullable=False)
    referrer_url = db.Column(db.String(255), nullable=False)
    target_url = db.Column(db.String(255), nullable=False)
    query_parma = db.Column(db.Text, nullable=False)
    user_agent = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_time = db.Column(db.DateTime, nullable=False)