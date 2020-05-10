import json
from flask import request, g

from application import app, db
from common.libs.Helper import getCurrentDate
from common.models.log.AppLog import AppAccessLog, AppErrorLog

class LogService():
    @staticmethod
    def addAccessLog():
        target = AppAccessLog()
        target.target_url = request.url
        target.referrer_url = request.referrer
        target.ip = request.remote_addr
        target.query_parma = json.dumps(request.values.to_dict())
        if 'current_user' in g and g.current_user is not None:
            target.uid = g.current_user.uid
        target.user_agent = request.headers.get('User-Agent')
        target.created_time = getCurrentDate()
        db.session.add(target)
        db.session.commit()
        return True