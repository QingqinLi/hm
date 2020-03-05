"""
异常：
    异常和错误的区别：
        Error: 语法错误 比较明显的错误 在编译代码阶段就能检测出来
        Iterayion 异常 在执行代码的过程中引发的异常
    异常发生之后程序就不再继续执行了
    万能异常 Exception 不建议使用, 万能异常和其他分支合作，万能异常要放在其他except的后面
    else-没有报错的时候执行 finally--一定会执行 在文件操作的时候，通常会在finally中执行关闭文件的操作，避免因异常导致的文件未关闭
    常见：
        # try/except
        # try/except/else
        # try/except/else/finally
        # try/except/finally
        # try/finally
    主动抛出异常：
    断言
    尽量少用异常处理
    使用异常一般会在最外层加一个大的异常处理
"""
l = ['登录','注册','退出']
for i in enumerate(l,1):
    print(i[0],i[1])
#
# while 1:
#     try:
#         num = input(">>>")
#         if num.upper() == 'Q':
#             break
#         print(l[int(num)-1])
#     except (IndexError, ValueError):
#         print("请输入一个数字")

# 万能异常 Exception
# try:
#     nam
#     dic= {}
#     dic['key']
# except Exception as e:
#     print(e, e.__traceback__.tb_lineno)

# try:
#     name
#     [][3]
#     import a
# except NameError: print("NameError")
# except IndexError: print("IndexError")
# except Exception: print("Exception")

# # 异常处理的其他机制
# try:
#     a = 1
#     name
#     [][3]
# except NameError:
#     print('name error')
# except Exception:
#     print('万能异常')
# else:  # try中的代码正常执行 没有异常的时候会执行else中的代码
#     print('执行else了')
# finally:  # 无论如何都会执行 操作系统资源归还的工作
#     print('执行finally了')

# 主动抛异常
# try:
#     num = int(input('>>>'))
# except Exception:
#     print('在出现了异常之后做点儿什么,再让它抛异常')
#     raise  # 原封不动的抛出try语句中出现的异常

# 自定义异常


# class EvaException(Exception):
#     def __init__(self,msg):
#         self.msg = msg

try:
    num = int(input('>>>'))
except Exception:
    print('在出现了异常之后做点儿什么,再让它抛异常')
    raise NameError('这是一个name error的异常')


# 断言  使用assert raise主动抛出异常
code = int(input(">>>"))
assert code
if code:
    print("123")
else:
    raise AssertionError