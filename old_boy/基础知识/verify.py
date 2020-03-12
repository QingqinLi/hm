import copy
lst1 = ["何炅", "杜涛", "周渝 ", ["麻花藤", "芸", "周笔畅"]]
lst2 = lst1.copy()
list3 = copy.deepcopy(lst1)
lst1[3].append(" 敌是多磨寂寞")

print(lst1)
print(lst2)
print(list3)
print(id(lst1[3]))
print(id(lst2[3]))
print(id(list3[3]))