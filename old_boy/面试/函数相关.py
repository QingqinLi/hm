"""
闭包：
    高阶函数除了可以接收函数作为参数，还可以把函数作为结果值返回，使用闭关的时候要注意不要引用任何循环变量，或者后续会发生变化的变量，
闭包--返回一个函数，延迟执行，闭包是嵌套在函数中的，闭包是内层函数对外层函数的变量的引用，闭包需要将其作为一个对象返回，而且必须逐层返回，数据不会随着函数执行完毕而消失
闭包的定义：在函数内部定义一个函数的时候，这个内部函数使用了外部函数的临时变量，且外部函数的返回值是是内部函数的引用
# 编写代码实现func函数，使其实现以下效果：
foo = func(8)

print(foo(8))  # 输出64
print(foo(-1))  # 输出-8

课后思考：用两个栈实现消息队列的功能？
"""


def func(num):
    def sum_num(num2):
        return num * num2
    return sum_num


foo = func(8)
print(foo(8))