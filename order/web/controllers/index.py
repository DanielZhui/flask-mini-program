from flask import Blueprint, g
from common.libs.Helper import ops_render


route_index = Blueprint('index', __name__)

@route_index.route('/')
def index():
    current_user = g.current_user
    return ops_render('index/index.html')