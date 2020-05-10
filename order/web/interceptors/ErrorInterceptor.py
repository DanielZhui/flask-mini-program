from application import app
from common.libs.Helper import ops_render
from common.libs.log.LogService import LogService

@app.errorhandler(404)
def handel_not_found(error):
    LogService.addErrorLog(str(error))
    return ops_render('error/error.html', {'status': 404, 'msg': '很抱歉!你访问的页面不存在'})