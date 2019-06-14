
name = 'hm'
# 文本对齐操作
poem = ["xxxx",
        "xxx",
        "xxxxx",
        "xxxxx",
        "xxxxx",
        "xxxxx",
        ]
for item in poem:
    print(item.center(10, "*"))

poem_str = "xxxx\t xxx\t xxxxx1\t \n xxxxx2\t\t xxxxx3\t\t"
poem_list = poem_str.split()
poem_new = " ".join(poem_list)
print(poem_new)

test_list = [1,2,4,5,6,7,8,5,4]
for i in test_list:
    print(i)
    if i == 4:
        continue
else:
    print("here")


# test checkout
# test 119
def test():
    print("test merge git")