"""
正则： 正则指引
re模块

正则表达式（一种匹配字符串的规则）：
    只能匹配字符串，从头到尾匹配
    字符组[]
        pass
        [^abc]:^表示非，不能以abc开头、
        【】，[^] 下面这一组无法描述的一般用上面字符组的形式／一个特殊元字符无法面数一个字符内出现的内容了
        在字符组中一些特殊的字符就会现出原形
    元字符
        \d 数字 \w 数字、字母、下划线 \s （空 、\n \t) \D \W \S -与小写字母相反 \n \t
        [\d\D][\w\W][\s\S] 匹配所有
        .:匹配除了换行符的任意字符 爬虫常用 表单提交不常用
        ^ $ :k
        \b 边界（字符串的前后-单词的边界）
        开始^: 一般只出现在正则表达式的开头
        结束$：一般只出现在正则表达式的结尾

        # [1bc] 是一个范围
        # [0-9][A-Z][a-z]    匹配三个字符
        # [abc0-9]           匹配一个字符
        # [0-9a-zA-Z]        匹配一个字符

        a|b 匹配a/b 只能匹配一个字符，找到一个就不找了，一次只有一个结果，两条规则有重叠时候，长的放在前面（会从头开始匹配，放在后面不会被匹配到）| 表示左边的所有，右边的所有

        从头开始匹配，
        .:匹配除了换行符的任意字符
        \.：转义 匹配.
    分组:() 整体约束
        \d+(\.\d*)? 匹配小数或者整数的正则表达式


    量词：
        什么都没有的字符串也会有一个开始符
        {n} 两次前面的正则匹配多少次，只对前面正则有效用
        {n,} 至少n次， 尽量多的匹配（贪婪匹配--回溯算法）
        {n, m} 至少n次，至多m次。尽量多的匹配
        ？重复0次或一次(可有可无的）--- 贪婪（能匹配就匹配）
        * 匹配0次或任意多次
        + 匹配一次或任意多次

    特殊的用法和现象：
        ？的使用：
            1、使用在元字符的后面
            2、量词后面的？eg.??,*?,... 取消贪婪匹配（匹配最少的）--- 在能匹配上的情况下匹配最少的

    总结：
        1、原字符 量词   默认贪婪匹配
        2、元字符 量词 ？  惰性匹配


元字符后面只能是量词

转义符：
    python中的转义符：\, r

正则表达式进阶：
    分组命名：
        （?P<name>) 表示给分组起名字
        （?P=name) 表示使用这个分组，这里匹配到的内容和分组中内容完全相同
        通过索引使用分组：\1 表示使用第一组，匹配到的内容必须和第一个组中的内容完全相同

re模块：
    匹配：
        findall 返回一个所有结果的列表
        search 结果是一个正则结果对象，没有找到None
        match 从头开始匹配
    切割：
        split

    替换：
        sub 相当于replace
        subn

    进阶：
        compile --- 预编译 节省时间（多次使用某一个相同的正则表达式的时候，会提高效率）时间效率
        finditer 节省内存 空间效率 大量数据的时候

    特殊：
        使用findall会优先显示搜索结果中分组中的内容 组内先写?:--取消分组优先
        split 保留切分的元素 正则表达式加（）--- 遇见分组 会保留分组内被切掉的内容 在列表中
        search 有分组的话 group(n)可以拿到gruop中的匹配内容
    分组命名：
        语法：1、？P<tag_name（组名)> 两部分的内容相同
            定义：
            使用：
                先定义再使用
            2、通过索引 推荐使用


转义符：
    # 所有的 \w \d \s(\n,\t, )  \W \D \S都表示它原本的意义
    # [-]只有写在字符组的首位的时候表示普通的减号
    #    写在其他位置的时候表示范围[1-9]
    #    如果就是想匹配减号 [1\-9]

"""
# 练习题

import re
# ret = re.findall('\d+', '19277vvgvuhuhu344h')
# print(ret)

ret2 = re.search('\d+', '*7@hbnnjj2233kkk333')
print(ret2)  # 匹配到会输出一个对象，否则输出None
if ret2:
    print(ret2.group())  # 返回的对象通过group来获取匹配的第一个结果

# match 从头开始匹配
# ret4 = re.match('\d+', '123hhh345')
# print(ret4)
# ret5 = re.match('\d+', 'ff55666')
# print(ret5)


# 替换
# sub(要替换的目标字符，要替换成的字符串，字符串, [n--替换几个]）
# ret = re.sub('\d+', "H", 'replace789bbbbb')
# print(ret)
ret2 = re.sub('\d', "H", "replae789jjjj", 1)
print(ret2)
#
# # subn 返回的是一个元祖，一个替换之后的字符串，一个替换了几次的整数
# ret3 = re.subn('\d', "H", "replace334ddd44ddd")
# print(ret3)

# # 切割 split 用特定re表达式分割字符串
# print("alex|1234".split("|"))
# ret = re.split('\d+', '123ddd444ffff43ff3ff')
# print(ret)

# 爬虫／自动化开发
# compile 时间效率 只有在多次使用某一个相同的正则表达式的时候，这个compile才会提高我们程序的效率
# print(re.findall('-0\.\d+|-[1-9]\d+(?:\.\d+)?', 'alex-87dhhe89nbbubs80'))
# ret = re.compile('-0\.\d+|-[1-9]\d+(\.\d+)?')
# res = ret.findall("alex-87dhhe89nbbubs80")
# res2 = ret.search("alex83egon-20taibai-40")
# print(res2.group())

# ret = re.compile('-0\.\d+|-[1-9]\d+(\.\d+)?')
# res = ret.search('alex83egon-20taibai-40')
# print(res.group())

# finditer 节省空间效率 同生成器原理
# ret = re.finditer("\d+", "sjkhkdy982ufejwsh02yu93jfpwcmc")
# for i in ret:
#     print(i.group())

# ret = re.compile('-0\.\d+|-[1-9]\d*(?:\.\d+)?')
# c = ret.search('-1asdada-200')
# print(c.group())
# c1 = ret.findall('-1asdada-200')
# print(c1)

# ret = re.split("\d+", 'alex83egon20taibai40')
# # print(ret)
# ret1 = re.split("(\d+)", 'alex83egon20taibai40')
# print(ret1)

ret = re.search('\d+(.\d+)(.\d+)(.\d+)?', '1.2.3.4-2*(60+(-40.35/5)-(-4*3))')
print(ret.group(), ret.group(1), ret.group(2), ret.group(3))

# 分组练习
# ret = re.findall(r"\d+(?:\.\d+)|(\d+)", "1-2*(60+(-40.35/5)-(-4*3))")
# print(ret)

# ret = re.findall('>(\w)<', r'<a>wahaha<\a>')
# print(ret)

# ret = re.search(r'<(\w+)>(\w+)</(\w+)>', r'<a>wahaha</b>')
# # print(ret.group(), ret.group(1), ret.group(2), ret.group(3))

# 分组命名
# ret = re.search('<(?P<name>\w+)>\w+<(?P=name)>', r'<a>hello<a>')
# print(ret.group('name'))
# ret = re.search("<(?P<name>\w+)>\w+</(?P=name)>","<h1>hello</h1>")
# print(ret.group('name'))  #结果 ：h1
# # print(ret.group())

# ret = re.search(r"<(\w+)>\w+</\1>", "<h1>hello</h1>")
# print(ret.group(1))
# print(ret.group())  #结果 ：<h1>hello</h1>

# 分组命名 根据名字取值
# ret = re.search(r'<(?P<tag>\w+)>(?P<c>\w+)</(\w+)>', r'<a>wahaha</b>')
# print(ret.group())
# print(ret.group('tag'))
# print(ret.group('c'))