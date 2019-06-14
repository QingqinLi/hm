# 定义一个全局变量
cards_list = []


def show_menu():
    """
    显示欢迎菜单
    :return:
    """
    print("*" * 50)
    print("")
    print("【1】新增名片")
    print("【1】展示名片")
    print("【1】搜索名片")
    print("")
    print("*" * 50)


def new_card():
    """
    定义一个新的名片
    :return:
    """
    name = input("请输入姓名：")
    age = input("请输入年龄:")
    phone = input("请输入电话号码:")

    card_dict = {'name': name,
                 'age': age,
                 'phone': phone,
                 }
    cards_list.append(card_dict)

    print("新增名片成功")
    print("=" * 50)


def show_cards():
    """
    展示所有的名片
    :return:
    """
    if len(cards_list) == 0:
        print("当前无名片")
        print("=" * 50)
        return
    print("姓名\t\t年龄\t\t电话")
    for card in cards_list:
        print(card['name'] + "\t\t" + card["age"] + "\t\t" + card["phone"])

    print("已展示名片")
    print("=" * 50)


def search_card():
    """
    搜索卡片
    :return:
    """
    card_name = input("请输入要搜索的名片姓名：")
    for card in cards_list:
        if card['name'] == card_name:
            print("姓名\t\t年龄\t\t电话")
            print(card['name'] + "\t\t" + card["age"] + "\t\t" + card["phone"])
            card_info = card
            select = input("请选择您要进行的操作："
                           "【1】修改名片\t"
                           "【2】删除名片:")
            print(select)
            if select == '1':
                cards_list.append(update_card(card_info))
                del_card(card_info)
            elif select == '2':
                del_card(card_info)
            break
    else:
        print("未搜索到相关内容")
    print("搜索名片完成")
    print("=" * 50)


def update_card(card_info):
    """
    修改卡片信息
    :param card_info: 旧的card信息
    :return:
    """
    name = input("请输入修改后的姓名【回车不修改】：")
    age = input("请输入修改后的年龄【回车不修改】：")
    phone = input("请输入修改后的电话【回车不修改】：")

    if len(name) == 0:
        name = card_info['name']
    if len(age) == 0:
        age = card_info['age']
    if len(phone) == 0:
        phone = card_info['phone']

    card_new = {'name': name,
                'age': age,
                'phone': phone,
                }
    return card_new


def del_card(card_info):
    """
    删除选择的卡片信息
    :param card_info:
    :return:
    """
    cards_list.remove(card_info)


def more_func():
    # dev分支的修改
    pass
