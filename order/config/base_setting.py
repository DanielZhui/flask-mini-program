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

# 每页显示的数量
PAGE_SIZE = 3
# 分页器展示的页码
PAGE_DISPLAY = 10

STATUS_MAPPING = {
    '1': '正常',
    '0': '已删除'
}

RELEASE_VERSION = '1.0.0'