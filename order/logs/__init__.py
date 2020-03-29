import logging
from logging.handlers import RotatingFileHandler


# 日志相关配置
# 设置日志的记录等级
def setup_log(level):
    logging.basicConfig(level=level)
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handle = RotatingFileHandler('logs/project.log', maxBytes=1024*1024*300, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为日志记录器设置日志记录格式
    file_log_handle.setFormatter(formatter)
    # 为全局的日志工具对象（flaskapp使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handle)