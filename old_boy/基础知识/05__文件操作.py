"""
1. 初识 件操作
2. 只读(r, rb)
3. 只写(w, wb) 如果没有文件则会创建文件，如果文件存在。则会将原来文件中的内容删除，再写入新的内容
4. 追加(a, ab) 追加模式下，写入的内容是会追加在文件的结尾
5. r+读写 r+b 对于读写模式. 必须是先读. 因为默认光标是在开头的. 准备读取的. 当读完之后再进行写入. 我们以后使用频率最高的是r+
6. w+写读 w+b 先将所有的内容清空. 然后写入. 最后读取. 但是读取的内容是空的, 不常用， w+模式下,开始读取不到数据. 然后写的时候再将原来的内容清空，所以很少用
7. a+写读(追加写读) 不论先读还是后读. 都是读取不到数据的.
8. 其他操作 法
9.  件的修改以及另 种打开 件 柄的 式

读取文件的方法
read（）将文件中内容全部读取出来，弊端：占内存，如果文件过大，可能会导致内存崩溃
read() 读取n个字符，需要注意得失，如果再次读取的时候，会在当前位置继续读下去而不是从头开始读，如果使用rb，则读取出来的是n个字节
readline（）一次读取一行数据，每次读取出来的数据都会有一个\n,可以使用strip（）去掉\n或者空格
readlines() 将每一行形成一个元素，放到一个list中，将所有的内容都读出来，所以也是，容易出现内存崩溃的情况，不推荐使用
循环读取 每次读取一行的内容 不会产生内存溢出的问题

在r+模式下. 如果读取了内容. 不论读取内容多少. 光标显示的是多少. 再写入
或者操作文件的时候都是在结尾进行的操作.

open（）方法读取完的文件一定要记得关闭f.close()
f.seek(n) 光标移动到n位置，移动的单位是byte，中文（utf-8）模式下要移动3倍
移动到开头seek（0）
移动到结尾seek(0, 2)
f.tell() 可以告诉我们光标的位置

os.remove() 删除源文件
os.rename() 重命名文件
"""
# f = open('userinfo', mode='r', encoding="utf-8")
# content = f.read()
# print(content)
# f.close()
#
# # 不需要自己写close
# with open('userinfo', encoding="utf-8") as file:
#     for line in file:
#         print(line)

# rb. 读取出来的数据是bytes类型, 在rb模式下. 不能选择encoding字符集.
# 在读取非文本的时候，比如读取mp3文件 图像，视屏的时候就需要用到rb，因为这种数据是没有办法直接读取的 文件的上传下载的地方还会用到，还有看的
# 直播，实际上也是这种数据
# f = open('userinfo', mode='rb')
# content = f.read()
# print(content)
# f.close()

# f = open("test.txt", "w", encoding="utf-8")
# f.write("ceshi")
# f.flush()
# f.close()

# wb模式下. 可以不指定打开 件的编码. 但是在写 件的时候必须将字符 转化成utf-8的 bytes数据
# f = open("test.txt", "wb")
# f.write("中文显示".encode("utf-8"))
# f.flush()
# f.close()

f = open("text.txt", mode='a', encoding='utf-8')
f.write("追加内容")
f.flush()
f.close()