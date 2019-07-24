"""
__name__ 当前文件指的是__name__所在的文件
执行当前文件，__name__就是__main__,当前文件被导入，name是自己的模块名
sys.path : 一个模块能不能被导入，就是看sys.path中是否有这个模块对应的绝对路径
若导入不成功：
    print(sys.path)
    import module
    修改sys.path
    修改import语句
不要循环导入
所有的模块导入，相当于把要导入的模块中的代码放到被直接执行的文件下执行了

导入的包开始的包也必须在sys.path的路径中
    从包中导入模块：
        import 包.包....模块
        from 包.包 import 模块
    直接导入包
        相当于执行了__init__.py
        在init中做一些导入设置，才能保证导入包的时候能够使用这些包中的模块

"""
import os

file_path = '/Users/qing.li/PycharmProjects/hm/old_boy/基础知识/00_基础知识.py'

filename = os.path.basename(file_path)
print(filename)