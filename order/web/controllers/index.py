from flask import Blueprint


route_index = Blueprint('index', __name__)

@route_index.route('/')
def index():
    return 'welcome to order system'