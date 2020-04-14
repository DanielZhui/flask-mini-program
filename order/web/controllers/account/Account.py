from flask import Blueprint, jsonify, request, redirect

from common.libs.Helper import ops_render
from common.models.User import User

route_account = Blueprint('account_page', __name__)

@route_account.route('/index')
def index():
    resp_data = {}
    users = User.query.order_by(User.uid.desc()).all()
    print(users)
    resp_data['users'] = users
    return ops_render('/account/index.html', resp_data)

@route_account.route('/info', methods=['GET', 'POST'])
def info():
    request_method = request.method
    if request_method == 'GET':
        resp_data = {}
        request_args = request.args
        print(request_args)
        uid = request_args['id'] if 'id' in request_args else ''
        if not uid:
            return redirect('/account/index')
        user = User.query.filter_by(uid=uid).first()
        resp_data['user'] = user
        return ops_render('/account/info.html', resp_data)

@route_account.route('/set')
def set():
    pass

@route_account.route('/delete')
def delete():
    pass