import re

from flask import g, request, redirect

from application import app
from common.models.User import User
from common.libs.user.UserService import UserService

@app.before_request
def before_request():
    path = request.path
    # 忽略静态文件路径
    ignore_url = app.config['IGNORE_URLS']
    ingore_static_url = app.config['IGNORE_STATIC_URLS']
    # 正则匹配当前路径是否是需要忽略的路径
    pattern = re.compile('|'.join(ingore_static_url))

    if path == '/user/login':
        return

    if pattern.match(path):
        return
    # 验证 cookie 中当前用户是已经否登录
    user_info = check_login()
    if not user_info:
        return redirect('/user/login')
    return

def check_login():
    cookies = request.cookies
    auth_cookie = cookies[app.config['AUTH_COOKIE_NAME']] if app.config['AUTH_COOKIE_NAME'] in cookies else None

    if not auth_cookie:
        return

    auth_info = auth_cookie.split('#')
    if len(auth_info) !=2:
        return

    try:
        user_info = User.query.filter_by(uid=auth_info[1]).first()
    except Exception as e:
        return
    
    if not user_info:
        return
    
    if auth_info[0] != UserService.geneAuthCode(user_info):
        return

    if user_info.status != 1:
        return

    return user_info