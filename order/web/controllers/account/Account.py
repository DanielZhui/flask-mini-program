from sqlalchemy import or_
from flask import Blueprint, jsonify, request, redirect

from common.libs.Helper import ops_render, getCurrentDate, iPagination
from common.models.User import User
from common.models.log.AppLog import AppAccessLog
from common.libs.user.UserService import UserService
from application import db, app

route_account = Blueprint('account_page', __name__)

@route_account.route('/index')
def index():
    resp_data = {}
    req_data = request.values
    page = req_data['p'] if 'p' in req_data and req_data['p'] else 1
    page = int(page)
    query = User.query

    if 'mix_kw' in req_data and req_data['mix_kw']:
        rule = or_(User.nickname.ilike('%{}%'.format(req_data['mix_kw'])), User.mobile.ilike('%{}%'.format(req_data['mix_kw'])))
        query = query.filter(rule)

    if 'status' in req_data and int(req_data['status']) > -1:
        query = query.filter(User.status == int(req_data['status']))

    page_params = {
        'total': query.count(),
        'page_size': app.config['PAGE_SIZE'],
        'page': page,
        'display': app.config['PAGE_DISPLAY'],
        'url': request.full_path.replace('&p={}'.format(page), '')
    }

    pages = iPagination(page_params)
    offset = (page - 1) * app.config['PAGE_SIZE']
    limit = app.config['PAGE_SIZE'] * page
    users = query.order_by(User.uid.desc()).all()[offset: limit]
    resp_data['pages'] = pages
    resp_data['users'] = users
    resp_data['search_con'] = req_data
    resp_data['status_mapping'] = app.config['STATUS_MAPPING']
    return ops_render('/account/index.html', resp_data)

@route_account.route('/info', methods=['GET', 'POST'])
def info():
    request_method = request.method
    if request_method == 'GET':
        resp_data = {}
        request_args = request.args
        uid = request_args['id'] if 'id' in request_args else ''
        if not uid:
            return redirect('/account/index')
        user = User.query.filter_by(uid=uid).first()
        resp_data['user'] = user
        # 获取当前用户访问记录
        access_log = AppAccessLog.query.filter_by(uid=uid).order_by(AppAccessLog.id.desc()).limit(10).all()
        resp_data['access_log'] = access_log
        return ops_render('/account/info.html', resp_data)

# 新增用户和修改用户资料统一放在这个 set 这个逻辑中实现
@route_account.route('/set', methods=['GET', 'POST'])
def set():
    # 这里用来区别是添加用户还是修改用户资料
    default_pwd = '******'
    request_method = request.method
    if request_method == 'GET':
        resp_data= {}
        req = request.args
        uid = int(req.get('id', 0))
        info = None
        if uid:
            info = User.query.filter_by(uid=uid).first()
        resp_data['info'] = info
        return ops_render('/account/set.html', resp_data)

    resp_data = {'cade': 200, 'msg': '操作成功', 'data': {}}
    request_data = request.values
    uid = request_data['id'] if 'id' in request_data else 0
    nickname = request_data['nickname'] if 'nickname' in request_data else ''
    mobile = request_data['mobile'] if 'mobile' in request_data else ''
    email = request_data['email'] if 'email' in request_data else ''
    login_name = request_data['login_name'] if 'login_name' in request_data else ''
    login_pwd = request_data['login_pwd'] if 'login_pwd' in request_data else ''

    if not nickname or len(nickname) < 1:
        resp_data['code'] = -1
        resp_data['msg'] = "请输入符合规范的昵称"
        return jsonify(resp_data)

    if not email or len(email) < 1:
        resp_data['code'] = -1
        resp_data['msg'] = "请输入符合规范的邮箱"
        return jsonify(resp_data)

    if not login_name or len(login_name) < 1:
        resp_data['code'] = -1
        resp_data['msg'] = "请输入符合规范的用户名"
        return jsonify(resp_data)

    if not login_pwd or len(login_pwd) < 1:
        resp_data['code'] = -1
        resp_data['msg'] = "请输入符合规范的登录密码"
        return jsonify(resp_data)

    # 判断新增用户名是否存在
    has_in = User.query.filter(User.login_name == login_name, User.uid != uid).first()
    if has_in:
        resp_data['code'] = -1
        resp_data['msg'] = '登录名已存在, 请换一个试试'
        return jsonify(resp_data)

    user_info = User.query.filter_by(uid=uid).first()
    if user_info:
        model_user = user_info
    else:
        model_user = User()
        model_user.create_time = getCurrentDate()
        model_user.login_salt = UserService.get_salt()

    model_user.nickname = nickname
    model_user.email = email
    model_user.mobile = mobile
    # TODO:用户头像以及用户状态
    model_user.sex = model_user.status =1
    model_user.avatar = 'www'
    model_user.login_name = login_name
    if login_pwd != default_pwd:
        model_user.login_pwd = UserService.genePwd(login_pwd, model_user.login_salt)
    
    model_user.update_time = getCurrentDate()
    db.session.add(model_user)
    db.session.commit()
    return jsonify(resp_data)
        
# 删除用户和恢复用户统一放在这个逻辑中去实现
@route_account.route('/ops', methods=['POST'])
def ops():
    resp_data = {'code': 200, 'msg': '操作成功', 'data': {}}
    req = request.values

    id = req['id'] if 'id' in req else 0
    act = req['act'] if 'act' in req else ''
    if not id:
        resp_data['code'] = -1
        resp_data['msg'] = '请选择正确的账号'
        return jsonify(resp_data)

    if act not in ['remove', 'recover']:
        resp_data['code'] = -1
        resp_data['msg'] = '操作有误请重试'
        return jsonify(resp_data)

    user_info = User.query.filter_by(uid=id).first()
    if not user_info:
        resp_data['code'] = -1
        resp_data['msg'] = '该账号不存在'
        return jsonify(resp_data)

    if act == 'remove':
        user_info.status = 0
    else:
        user_info.status = 1
    
    user_info.update_time = getCurrentDate()
    db.session.add(user_info)
    db.session.commit()
    return jsonify(resp_data)