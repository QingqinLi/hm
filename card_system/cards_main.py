#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3
from card_system import cards_tools
# 无限循环，由用户决定什么时候结束程序
cards_tools.show_menu()
while True:
    try:
        # 可以不用int转换，直接判断用户输入的是不是字符串类型的数字，避免因为类型的原因导致程序报错
        select_operation = int(input("请选择要进行的操作："))
    except ValueError:
        print("请重新选择要进行的操作")
        continue
    print("您选择的操作是：[%s]" % select_operation)
    if select_operation in [1, 2, 3]:
        # 正确的选择
        # pass关键字，是一个占位符，能够保证程序的代码结构正确，但没有任何的实际操作
        if select_operation == 1:
            cards_tools.new_card()
        elif select_operation == 2:
            cards_tools.show_cards()
        elif select_operation == 3:
            cards_tools.search_card()
    elif select_operation == 0:
        # 退出系统
        print("欢迎再次使用【名片管理系统】")
        break
    else:
        print("请重新选择要进行的操作")
