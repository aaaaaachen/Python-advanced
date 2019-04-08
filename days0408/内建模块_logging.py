# 1 导入模块
import logging
# 2 创建日志模块
loginLogger = logging.getLogger('main')
# 2.1 设置日志等级
loginLogger.setLevel(logging.ERROR)
# 3 创建日志输出类型
fileHandler = logging.FileHandler('loginregist.txt',encoding='utf-8')
# 3.1 文件日志等级
fileHandler.setLevel(logging.ERROR)
# 4 指定日志格式
fileformatter = logging.Formatter('%(name)s-%(levelno)s-%(lineno)d-%(asctime)s-%(message)s')
# 5 将文件绑定日志格式
fileHandler.setFormatter(fileformatter)

streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.ERROR)
streamHandler.setFormatter(fileformatter)

# 6 将日志处理方式添加到日志工具
loginLogger.addHandler(fileHandler)
loginLogger.addHandler(streamHandler)

loginLogger.debug("debug.....")
loginLogger.error("error.....")
loginLogger.warning("worning....")
loginLogger.info("info.....")

