import json
from flask import Blueprint, request, render_template, redirect, jsonify, make_response
from application import app

from common.models.User import User
from common.libs.user.UserService import UserService

route_user = Blueprint('user_page', __name__)

@route_user.route('/login', methods=['GET', 'POST'])
def login():
    # 请求 login 页面时
    if request.method == 'GET':
        return render_template('user/login.html')

    resp = {'code': 200, 'msg': '登录成功', 'data': {}}
    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''

    # 对请求参数进行校验
    if not login_name or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入正确的用户名'
        return jsonify(resp)
    
    if not login_pwd or len(login_pwd) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入正确的用户名或密码'
        return jsonify(resp)

    user_info = User.query.filter_by(login_name=login_name).first()
    if not user_info:
        resp['code'] = -1
        resp['msg'] = '请输入正确的用户名或密码'
        return jsonify(resp)

    # 比较登录用户密码和数据库保存密码(加密后的密码)是否一致
    salt_pwd = UserService.genePwd(login_pwd, user_info.login_salt)
    if user_info.login_pwd != salt_pwd:
        resp['code'] = -1
        resp['msg'] = '请输入正确的用户名或密码!'
        return jsonify(resp)

    # 判断用户是否为有效用户
    if user_info.status != 1:
        resp['code'] = -1
        resp['msg'] = '账号已失效,请重试'
        return jsonify(resp)

    # 当所有验证通过时设置当前登录用户 cookie 信息(加密)
    response = make_response(json.dumps(resp))
    # cookie 有效期设置为一天
    response.set_cookie(app.config['AUTH_COOKIE_NAME'], UserService.geneAuthCode(user_info), 24 * 60 * 60)
    return response
