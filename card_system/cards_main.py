# 无限循环，由用户决定什么时候结束程序
while True:
    try:
        select_operation = int(input("请选择要进行的操作："))
    except ValueError:
        print("请重新选择要进行的操作")
        continue
    print("您选择的操作是：[%s]" % select_operation)
    if select_operation in [1, 2, 3]:
        # 正确的选择
        # pass关键字，是一个占位符，能够保证程序的代码结构正确，但没有任何的实际操作
        pass
    elif select_operation == 0:
        # 退出系统
        print("欢迎再次使用【名片管理系统】")
        break
    else:
        print("请重新选择要进行的操作")
