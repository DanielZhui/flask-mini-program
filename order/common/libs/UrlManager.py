import time
from application import app

class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl(path):
        return path
    
    @staticmethod
    def buildStaticUrl(path):
        time_stamp = int(time.time())
        release_version = app.config.get('RELEASE_VERSION')
        version = '{}'.format(time_stamp) if not release_version else release_version
        # js 文件加上版本号只要版本号更新 js 刷新生效, 而无需强制刷新
        path = '/static' + path + '?release=' + version
        return UrlManager.buildUrl(path)

    @staticmethod
    def buildImage(path):
        pass
