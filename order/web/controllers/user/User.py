import json
from flask import Blueprint, request, redirect, jsonify, make_response, g
from application import app, db

from common.models.User import User
from common.libs.user.UserService import UserService
from common.libs.Helper import ops_render

route_user = Blueprint('user_page', __name__)

@route_user.route('/login', methods=['GET', 'POST'])
def login():
    # 请求 login 页面时
    if request.method == 'GET':
        return ops_render('user/login.html')
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
    # cookie 的value: 加密字符串#uid 这样设计的目的是方便后面拦截器获取用户信息, cookie 有效期设置为一天
    response.set_cookie(app.config['AUTH_COOKIE_NAME'], '{}#{}'.format(UserService.geneAuthCode(user_info), user_info.uid), 24 * 60 * 60)
    return response


@route_user.route('/logout')
def logout():
    response = make_response(redirect('/user/login'))
    response.delete_cookie(app.config['AUTH_COOKIE_NAME'])
    return response

@route_user.route('/edit', methods=['GET', 'POST'])
def edit():
    resp = {'code': 200, 'msg': '修改成功', 'data': {}}
    request_method = request.method
    if request_method == 'GET':
        return ops_render('user/edit.html')
    if request_method == 'POST':
        req = request.values
        nickname = req['nickname'] if 'nickname' in req else ''
        email = req['email'] if 'email' in req else ''

        if not nickname or len(nickname) < 1:
            resp['code'] = -1
            resp['msg'] = '请输入符合规范的姓名'
            return jsonify(resp)

        if not email or len(email) < 1:
            resp['code'] = -1
            resp['msg'] = '请输入符合规范的邮箱'
            return jsonify(resp)

        user_info = g.current_user
        user_info.nickname = nickname
        user_info.email = email
        # 更新当前用户的用户信息
        db.session.add(user_info)
        db.session.commit()
        return jsonify(resp)

@route_user.route('/reset-pwd', methods=['GET', 'POST'])
def resetPwd():
    request_method = request.method
    if request_method == 'GET':
        return ops_render('user/reset_pwd.html')
    if request_method == 'POST':
        resp = {'code': 200, 'msg': '修改成功', 'data': {}}
        req_data = request.values
        old_password = req_data['old_password'] if 'old_password' in req_data else ''
        new_password = req_data['new_password'] if 'new_password' in req_data else ''

        if not old_password or len(old_password) < 6:
            resp['code'] = -1
            resp['msg'] = '原始密码长度应不小于6'
            return jsonify(resp)

        if not new_password or len(new_password) < 6:
            resp['code'] = -1
            resp['msg'] = '新密码密码长度应不小于6'
            return jsonify(resp)

        if old_password == new_password:
            resp['code'] = -1
            resp['msg'] = '新旧密码不能完全相同'
            return jsonify(resp)

        user_info = g.current_user
        user_salt = user_info.login_salt
        login_pwd = user_info.login_pwd
        request_pwd = UserService.genePwd(old_password, user_salt)
        if request_pwd != login_pwd:
            resp['code'] = -1
            resp['msg'] = '你输入的原始密码不正确,请确认后重新输入'
            return jsonify(resp)

        user_info.login_pwd = UserService.genePwd(new_password, user_salt)
        db.session.add(user_info)
        db.session.commit()

        # 设置新cookie
        response = make_response(json.dumps(resp))
        response.set_cookie(app.config['AUTH_COOKIE_NAME'], '{}#{}'.format(UserService.geneAuthCode(user_info), user_info.uid), 24 * 60 * 60)
        
        return response