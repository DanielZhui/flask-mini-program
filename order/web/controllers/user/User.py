from flask import Blueprint, request, render_template, redirect, jsonify

route_user = Blueprint('user_page', __name__)

@route_user.route('/login', methods=['GET', 'POST'])
def login():
    # 请求 login 页面时
    if request.method == 'GET':
        return render_template('user/login.html')

    # 对请求参数进行校验
    resp = {'code': 200, 'msg': '登录成功', 'data': {}}
    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''

    if not login_name or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入正确的用户名'
        return jsonify(resp)
    
    if not login_pwd or len(login_pwd) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入正确的用户名或密码'
        return jsonify(resp)

    return jsonify(resp)
