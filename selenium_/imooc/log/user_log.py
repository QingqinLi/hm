import logging
import os
import time
import datetime

# logger = logging.getLogger()
# # 后续使用logger输出
# logger.setLevel(logging.DEBUG)
# # 给logging模块
# # 控制台输出日志
# # console = logging.StreamHandler()
# # logger.addHandler(console)
#
#
# # 根据日期命名文件
# base = os.path.dirname(os.path.abspath(__file__)) # 当前文件的路径
# log_dir = os.path.join(base, 'logs')
# file_time = datetime.datetime.now().strftime("%Y-%m-%d")
# file_path = os.path.join(log_dir, file_time) + '.log'
# print(file_path)
#
# # 文件输出日志
# file_handle = logging.FileHandler(file_path, 'a', encoding='utf-8')
# # logger.addHandler(file_handle)
#
# # 定义日志输出的格式， 添加一些格式到handle这种
# formatter = logging.Formatter('%(asctime)s  %(filename)s ---> %(funcName)s %(lineno)s: %(levelname)s----> %(message)s')
# file_handle.setFormatter(formatter)
# logger.addHandler(file_handle)
#
#
# logger.debug("teste")
#
# # 要关闭
# # console.close()
# # logger.removeHandler(console)
#
# file_handle.close()
# logger.removeHandler(file_handle)
#
# # 输出到日志文件中， 代码部署到线上/服务器， 脱离编译器，需要日志文件
#
# # 把日志按照一定的格式输出


class UserLog:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        base = os.path.dirname(os.path.abspath(__file__))
        file_base = os.path.join(base, 'logs')
        file_today = datetime.datetime.now().strftime("%Y-%m-%d") + '.log'
        file_path = os.path.join(file_base, file_today)

        self.file_handle = logging.FileHandler(file_path, 'a', encoding='utf-8')

        formatter = logging.Formatter('%(asctime)s  %(filename)s ---> %(funcName)s %(lineno)s: %(levelname)s----> %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

        # 避免关闭logger导致log不能写入的问题，不关闭可能导致性能的问题
        """
        解决方案：
            1、写成方法，不用类
            2、装饰器
            3、把关闭的操作写在另外的函数
        """
        # file_handle.close()
        # self.logger.removeHandler(file_handle)

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.file_handle.close()
        self.logger.removeHandler(self.file_handle)



log = UserLog()



