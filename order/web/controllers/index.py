from flask import Blueprint, render_template


route_index = Blueprint('index', __name__)

@route_index.route('/')
def index():
    # return 'welcome to order system'
    return render_template('index/index.html')