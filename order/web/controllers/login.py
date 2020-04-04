from flask import Blueprint

login_page = Blueprint('login', __name__)

@login_page.route('/login')
def login():
    return 'login success...'