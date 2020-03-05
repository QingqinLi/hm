# 冒泡排序
list_maopao = [1, 5, 8, 22, 66, 11, 77, 124, 45, 112, 5555]


def maopao(list_maopao):
    for j in range(len(list_maopao)):
        for i in range(len(list_maopao) - 1 - j):
            if list_maopao[i] > list_maopao[i + 1]:
                list_maopao[i], list_maopao[i + 1] = list_maopao[i + 1], list_maopao[i]
    return list_maopao


print(maopao(list_maopao))

def buddle(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l
print(buddle(list_maopao))

