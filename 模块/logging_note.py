import logging
import time

# 通过logging.basicConfig进行参数设定

logging.basicConfig(
    # 默认是warning级别才会输出,level可以设置
    level=logging.DEBUG,
    # log默认在终端输出，filenname可以指定输出的文件地址
    filename='logging_'+time.ctime()+'.text'

)

logging.debug('yy debug message')
logging.info('yy info message')
logging.warning('yy warning message')
logging.error('yy error message')
logging.critical('yy critical message')

