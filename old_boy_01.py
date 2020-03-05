"""
1、判断质数
2、位数
3、回文
4、大写字母，小写字母，数字出现的次数
5、姓氏在不在百家姓， 复姓的问题
6、数字的读法
7、冒泡排序
8、36选7个不重复的数字

"""


def prime():
    """
    判断数字是不是质数
    :return:
    """
    try:
        num = int(input("input a number"))

    except TypeError:
        print("error")


def maopao():
    paixu_list = [55, 66, 77, 11, 44, 22, 33, 1000]
    for j in range(len(paixu_list)):
        for i in range(len(paixu_list) - 1 - j):
            if paixu_list[i] > paixu_list[i + 1]:
                paixu_list[i], paixu_list[i + 1] = paixu_list[i + 1], paixu_list[i]

    print(paixu_list)


def sum(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


def min_max(*args):
    # 1、排序的方法
    # list_num = list(args)
    # for num in range(len(list_num)):
    #     for i in range(len(list_num) - 1 - num):
    #         if list_num[i] > list_num[i + 1]:
    #             list_num[i], list_num[i + 1] = list_num[i + 1], list_num[i]
    # print(list_num)
    # return {"max": list_num[-1], "min": list_num[0]}
    # 2、比较的方法
    # max = args[0]
    # min = args[0]
    #
    # for num in args:
    #     if num > max:
    #         max = num
    #     if num < min:
    #         min = num
    # return {"max": max, "min": min}
    # 3、max(), min()函数的方式
    return {"max": max(args), "min": min(args)}


# maopao()
# print(sum(1,2,3,3,4))
print(min_max(2, 4, 5, 1, 77, 23, 100, 33, 11))