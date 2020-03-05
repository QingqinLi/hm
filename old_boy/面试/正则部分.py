"""
去除以下html文件中的标签，只显示文本信息。
<div>
<p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p> <br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p> <br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>
</div>
"""
# import re
#
# with open('正则.txt', 'r') as f:
#     ret = re.compile("<p>|<div>|</div>|</p>|<br>|\s")
#     content = re.sub(ret, '', f.read())
# print(content)


"""
将以下网址提取出域名：

"""

te = 'http://www.interoem.com/messageinfo.asp?id=35, http://3995503.com/class/class09/news_show.asp?id=14, ' \
     'http://lib.wzmc.edu.cn/news/onews.asp?id=769, http://www.zy-ls.com/alfx.asp?newsid=377&id=6,' \
     'http://www.fincm.com/newslist.asp?id=415'

# ret = re.compile("http://.*?/")
# res = re.finditer(ret, te)
# for i in res:
#     print(i.group())

"""
提取出如下字符串中的单词：
"""

# test_str = "hello world ha ha"
# print(re.split(' +', test_str))


"""
编写Python脚本，分析xx.log文件，按域名统计访问次数

xx.log文件内容如下：
https://www.sogo.com/ale.html
https://www.qq.com/3asd.html
https://www.sogo.com/teoans.html
https://www.bilibili.com/2
https://www.sogo.com/asd_sa.html
https://y.qq.com/
https://www.bilibili.com/1
https://dig.chouti.com/
https://www.bilibili.com/imd.html
https://www.bilibili.com/

脚本输出：
4 www.bilibili.com
3 www.sogo.com
1 www.qq.com
1 y.qq.com
1 dig.chouti.com
"""
import re
from collections import Counter

with open('ym.log') as f:
    data = f.read()

ret = re.findall('https://(.*)/.*', data)
ret1 = dict(Counter(ret))
# print(ret1)
ret_sort = sorted(ret1.items(), key=lambda x: x[1], reverse=True)
for i in ret_sort:
    print(i[1], i[0])















