import os
from functools import reduce
# 递归 主要用来遍历树形结构

filePath = "D:\\moji\\index_v2"


# 递归文件树
def read(filePath, n):
    files = os.listdir(filePath)
    print("files", files)
    for l_file in files:
        # print(os.path.join(filePath + l_file))
        file_name = os.path.join(filePath, l_file)
        if os.path.isdir(file_name):
            print("\t" * n, l_file, "test")
            read(file_name, n+1)  # 递归
        else:
            print("\t" * n, l_file)

# n用来控制缩进， 代表层级关系
# read(filePath, 0)


# 汉诺塔 https://blog.csdn.net/qq_37873310/article/details/80461767
def hanoi(n, a, b, c):
    if n == 1:
        print(a, "--->", c)
    else:
        hanoi(n-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n-1, b, a, c)


# hanoi(4, "A", "B", "C")


# n的阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def factorial2(n):
    sum = 1
    for i in range(1, n+1):
        sum *= i
    return sum


def factorial3(n):
    b = reduce(lambda x, y:x*y, range(1, n+1))
    return b


# print(factorial3(3))


# 斐波那契数列
def fibonacci(n):
    if n < 1:
        return -1
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# print(fibonacci(9))


# 幂的递归 pow()函数 ** 递归
def power(n, m):
    if m == 1:
        return n
    else:
        return n * power(n, m-1)


# print(pow(3, 4), 3 ** 4)


# 二分查找
# 算法方式
def find_mid(list_sorted, num):
    left = 0
    right = len(list_sorted) - 1

    while left <= right:
        middle = (left + right) // 2
        num_mid = list_sorted[middle]
        if num == num_mid:
            return middle
        elif num > num_mid:
            left = middle + 1
        elif num < num_mid:
            right = middle - 1
    else:
        return "not found"


# 递归方式
def search_binary(lst, left, right, num):
    # left = 0
    # right = len(list_sorted) - 1
    middle = (left + right) // 2

    if left > right:
        return -1
    elif list_sorted[middle] == num:
        return middle
    elif num > list_sorted[middle]:
        left = middle + 1
    else:
        right = middle - 1

    return search_binary(lst, left, right, num)


list_sorted = [11, 22, 33, 44, 55, 66, 77, 88, 89, 200]
print(search_binary(list_sorted, 0, len(list_sorted)-1, 660))


