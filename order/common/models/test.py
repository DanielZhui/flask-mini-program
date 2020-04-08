import time
from application import db


class ServiceJob(db.Model):
    __tablename__ = 'service_job'
    id = db.Column(db.BigInteger, primary_key=True)
    job_id = db.Column(db.String(32), nullable=False)
    status = db.Column(db.String(32), nullable=False)
    result = db.Column(db.String(200), nullable=False)
