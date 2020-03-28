from flask import Blueprint

route = Blueprint('index', __name__)

@route.route('/')
def index():
    return 'hello blueprint...'