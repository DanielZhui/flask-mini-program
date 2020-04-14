from application import app

'''
拦截器部分
'''
from web.interceptors import AuthInterceptor

'''
服务蓝图部分
'''
from web.controllers.index import route_index
from web.controllers.user.User import route_user
from web.controllers.static import route_static
from web.controllers.account.Account import route_account

app.register_blueprint(route_index, url_prefix='/')
app.register_blueprint(route_user, url_prefix='/user')
app.register_blueprint(route_static, url_prefix='/static')
app.register_blueprint(route_account, url_prefix='/account')