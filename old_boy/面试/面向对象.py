"""
1、谈谈你对面向对象的理解
对象 = 数据 + 方法
2、python面向对象中的继承有什么特点
3、面向对象的深度优先和广度优先是什么
必须得理解：
    MRO
    深度优先 广度优先 c3算法 http://python.jobbole.com/85685/
4、面向对象的super的作用
    在子类中执行父类的方法
5、列举面向对象中特殊成员（带下划线的特殊方法，__new__, __init__, __call__等）
    __new__(): 开辟空间，创建对象
    __init__():初始化对象，对象属性的赋值
    __call__():对象（）直接执行的代码
    __repr__():解释器环境下直接输入对象展示的内容
    __str__():print（）执行的
    __len__():len（）
    __del__():析构函数
    __hash__():
    __eq__():
    __setitem__():
    __getitem__():
    __delitem__():
6、静态方法和类方法的区别？
静态方法：
@staticmethod：与类中的内容无关的
类方法：
@classmethod（cls）：用类名直接调用的函数
    """
