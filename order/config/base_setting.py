SERVER_PORT = 5000
DEBUG = True
SQLALCHEMY_ECHO = False

AUTH_COOKIE_NAME = 'flask_order'

# 忽略的路径
IGNORE_URLS = [
    '^/user/login$'
]

IGNORE_STATIC_URLS = [
    '^/static',
    '^/favicon.ico'
]