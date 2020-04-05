from flask import Blueprint, request, render_template

route_user = Blueprint('user_page', __name__)

@route_user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return 'get request'
    render_template('user/login.html')