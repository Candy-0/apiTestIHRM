# 导包
import logging.handlers
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOST = "http://182.92.81.159"
HEADERS = {"Content-Type":"application/json"}
EMP_ID = 0

def init_login():
    # 实例化日志器
    logger = logging.getLogger()
    # 自定义日志的输出方式
    logging.basicConfig(level=logging.INFO)
    # 实例化处理器
    # 1.控制台
    sh = logging.StreamHandler()
    # 2.文件
    filename = BASE_DIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(filename, when="M", interval=1, backupCount=7)
    # 设置格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 将格式化器添加到处理器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将处理器添加到日志器
    logger.addHandler(sh)
    logger.addHandler(fh)
