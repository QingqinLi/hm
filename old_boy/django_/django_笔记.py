# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
"""
https://www.cnblogs.com/liwenzhou/p/8296964.html
http://www.cnblogs.com/liwenzhou/p/7931828.html
看图：https://www.cnblogs.com/liwenzhou/p/8296964.html
https://www.cnblogs.com/liwenzhou/p/7931828.html

内容回顾：
    1. MySQL  ****
        1. SQL语句
        2. 设计表的能力
        3. 原理
    2. 前端  ***
        1. HTML/CSS/JS
        2. jQuery  *****
        3. Bootstrap  *****
    3. 并发编程  **
        1. 进程
        2. 线程
        3. 协程
        4. IO多路复用
    4. 网络编程  ***
        1. socket/socketserver
        2. 粘包
    5. 面向对象  *****
        1. 封装、继承、多态
    6. 常用模块  *****
        1. os/sys/time/random/re/json/pickle/hashlib
        2. collections/functools(题：1 2 3 4能组成多少个不重复的三位数)
    7. 函数  *****
        1. 函数（函数定义/函数的参数/返回值/作用域/lambda）
        2. 迭代器/生成器
        3. 列表推导式/列表生成式
        4. 内置函数
            1. filter/map
            2. zip
            3. sorted
            4. ...等68个
        5. 递归
    8. 数据类型和内置方法  *****
    9. 文件操作  *****
    10. Python语法基础  *****
博客： www.cnblogs.com/liwenzhou/articles/
web框架的原理：
    1、C/S B/S
        cs客户端模式
        bs浏览器模式 ->web开发
    2、web开发的本质
        1、互联网上两台机器之间的通信：
            1、ip
            2、端口
            3、协议
        2、协议：
            1、HTTP 默认端口是80
            2、HTTPS 默认端口是443
        3、浏览器输入URL一回车到发挥页面，这中间的过程：
            1、域名 -》DNS解析 -》IP地址 -》服务端 -》返回消息 -》浏览器
            2、浏览器《--》服务端
            3、服务器把写好的HTML页面，返回给浏览器，浏览器按照HTML格式渲染（显示）
        4、请求和响应
            1、HTTP协议中：
                浏览器给服务端发消息的过程叫请求（request）
                服务端给浏览器回复消息的过程叫响应（response）
            2、请求和响应的消息都必须遵循一个固定的格式
python中框架的分类：
    a、收发socket消息，按照http协议解析消息 web服务程序 wsgiref gunicorn uWSGI
    b、字符串替换
    c、业务逻辑处理
    自己实现abc的：tornado
    自己实现bc，使用别人的a Django
    自己实现c，使用别人的ab Flask
    
    web服务程序 <-- WSGI协议 --> web应用程序
    
Django安装：
    Django版本介绍：
        注意LTS版本
    == 安装指定版本
    pip install Django==1.11.11
    pip install django==1.11.11 -i https://pypi.tuna.tsinghua.edu.cn/simple   指定数据源的地址
    pip uninstall Django
    pip -V:
        查看pip版本，路径
    创建项目
        命令行：django-admin startproject 项目名
        用pycharm创建
    启动项目：
        命令行启动：
            Django项目的根目录下，执行命令：
                python manage.py runserver
                python manage.py runserver 8080
            停止：ctrl + C
        pycharm启动
            点绿色三角
            注意左侧框中的名字一定要是项目名称
            
            
from表单提交数据：
    form表单必须要有action和method属性， 上传文件需要额外指定enctype属性 enctype="multipart/form-data"
    所有获取用户输入的标签必须放在form表单中，必须要有name属性(input, select, textarea)
    必须要有submit按钮

Django基础必会三件套
    from django.shortcuts import HttpResponse, render, redirect
        1、HttpResponse 返回一个指定的字符串时, 把一个字符串成二进制，按照HT，TP响应的格式要求返回
        2、render： 返回一个HTML文件，打开文件，读取内容，按照响应格式返回， {'key': 'value'} 替换特殊符号，按照响应格式返回.特殊符号的替换发生在Django服务端
        3、redirect 跳转 绝对地址（不同网站之间的跳转），相对地址（同一个网站之间的跳转），锚点（同一个网站页面位置的跳转），给浏览器返回的是一个特殊的响应，这个响应类似于一个命令，让浏览器去访问我指定的URL
    request相关的属性
        request.method  返回的是请求的方法（全大写）：GET/POST
        request.GET 获取URL里面的参数。类似与字典的数据结构
        request.POST post提交的数据，类似与字典的数据结构
    Django的模版语言
        1、{{变量名}} {'key': value}
        2、for循环
            {% for i in ret%}   
                {{i}
                {{forloop.connter }} 计数 counter0是从0开始计数
            {% endfor %}
            {% if %}
            {% else %}
            {% endif %}
        {% %} 逻辑相关
        {{ }} 变量相关
        (.)在模版语言中有特殊的含义，当模版语言遇到.的时候，会按照这样的顺序查询：
            字典查询
            属性或者方法查询
            数字索引查询
        如果使用的变量不存在，模版系统将插入string_if_invalid 选项的值，它将默认设置为''（空字符串）
        
        过滤器（filter）https://www.cnblogs.com/maple-shaw/articles/9333821.html
            {{value| filter_name:参数}} 参数最多只有一个
            | 过滤器
            过滤器支持链式操作： 即一个过滤器的输出作为另一个过滤器的输入
            过滤器参数包含空格的话必须用引号包裹起来。|的左右都没有空格
            常用的过滤器：
                default：如果一个变量是false或者是空的时候，使用给定的默认值，否则使用变量的值 {{value|default:"nothing"}}， 在settings中设置
                        TEMPLATES的options中增加一个选项string_if_invalid:'string' 可以替代default的作用
                filesizeformat: 将值格式化为"人类可读"的文件尺寸
                add: 给变量加参数 {{ value|add:"2" }} {{ first|add:second }}---如果first是[1,2,3]，second是 [4,5,6]，那输出结果是 [1,2,3,4,5,6] 。
                length: 返回值的长度，作用域字符串和列表
                lower: 把字母都转换为小写
                upper: 把字母都转换为大写
                title：首字母大写
                ljust：左对齐 "{{ value|ljust:"10" }}" 参数表示一共占几个字符
                rjust：右对齐 "{{ value|rjust:"10" }}"
                center：居中
                slice：切片，参数是切的范围
                first：取第一个元素
                last：取最后一个元素
                join：使用字符串凭借列表， 参数是拼接用的字符串
                truncatechars:如果字符串字符多于指定的字符数量，那么会被截断， 截断的字符串将会以可翻译的省略号序列（...)结尾， 参数：保留的字符数（包括...){{ value|truncatechars:9}}
                date:time格式化,{{ value|date:"Y-m-d H:i:s"}}
                     在setting中配置：DATETIME_FORMAT = 'Y-m-d H:i:s'
                                          USE_P20N = False
                safe: django的模版中会对html标签和js等语法标签进行自动转义，为了安全，但是有时不希望这些html元素被转义，可以使用safe
            自定义filter：
                自定义过滤器只是带有一个或者两个参数的python函数
                位置：
                    app01/
                    __init__.py
                    models.py
                    templatetags/  # 在app01下面新建一个package package
                        __init__.py
                        app01_filters.py  # 建一个存放自定义filter的py文件
                    views.py
                编写filter：
                    from django import template
                    register = template.Library()
                    
                    
                    @register.filter
                    def fill(value, arg):  value是过滤器前的内容
                        return value.replace(" ", arg)
                    
                    
                    @register.filter(name="addSB") --name是别名， 可以用这个名字来调用filter
                    def add_sb(value):
                        return "{} SB".format(value)
                使用：
                    {# 先导入我们自定义filter那个文件 #}
                    {% load app01_filters %}
                    
                    {# 使用我们自定义的filter #}
                    {{ somevariable|fill:"__" }}
                    {{ d.name|addSB }}
                    
        tags：{% %}
            for 可用的一些参数:
                forloop.counter: 当前循环的索引值（从1开始）
                forloop.counter0 当前循环的索引值（从0开始）
                forloop.revcounter 当前循环的倒序索引值（到1结束）
                forloop.revcounter0 当前循环的倒序索引值（到0结束）
                forloop.first 当前循环是不是第一次循环（布尔值）
                forloop.last 当前循环是不是最后一次循环（布尔值）
                forloop.parentloop 本层循环的外层循环
            for empty: 如果循环为空时候的操作
            if..elif..else 不支持连续判断 a>b>c 应该使用 a>b and b>c,不支持算数运算 + - * ／ add
            if语句支持 and or == > < != <= >= in not in is not 判断
            with: 定义一个中间变量 ？？？
                {% with 变量 as 别名%}
                {{别名}}
                {% endwith %} 一般用在变量名比较长的情况下
    django模版语言不支持连续判断，a>b>c
    属性的优先级大于方法
    
            
            
            
    程序连接mysql
        使用pymysql模块
        1、导入pymsql模块
        2、创建连接
        3、获取执行命令的游标
        4、用游标区执行sql语句
        5、获取sql的执行结果
        6、关闭游标
        7、关闭连接
        
        创建一种工具 来翻译SQL语句   ORM（object Relationship Model）
        
        优点：
            1、开发效率高
            2、开发不需要直接写sql语句
        缺点：
            1、执行效率低
        
        ORM   DB
        类    数据表
        属性  字段
        对象  数据行
Django创建app项目 项目中又分了一级python包，不同的功能放到不同的包中
    1、创建app python manage.py startapp app_name
    2、告诉django创建了一个app 在settings.py中找到那个INSTALLED_APPS中添加新创建的app
DJango中ORM的使用
    1、用处
        操作数据表和数据行
    2、使用
        1、创建一个数据库（手动，orm不支持操作数据库）
            create database mysite;
        2、告诉django连接哪个数据库
            databases = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql', 连接数据库的类型
                    'NAME': 'mysite'; 连接数据库的名字
                    'HOST': '127.0.0.1';  数据库主机地址
                    'PORT': 3306 数据库的端口
                    'USER': 'root';
                    'PASSWORD': '',
                }
            }
        3、用什么连接数据库
            利用第三方的包，比如pymysql和MySQLdb
            告诉Django受用pymysql模块代替默认的MySQLdb去连接mysql数据库
            在setting.py同级的init文件中：
                import pymysql
                pymysql.install_as_MySQLdb()
        4、在app/models.py中创建类，类必须继承models.Model
        5、 创建数据表
            python manage.py makemigrations 把models.py记录下来
            python manage.py migrate 把变更预计翻译称sql语句，去数据库中去执行
ORM查询
    uer.objects.filter(email='', pwd='')
ORM增删改查：
    class_name.objects.all() 返回一个列表，查询全部内容
    class_name.objects.filter() 查询条件，返回一个列表
    class_name.objects.get() 返回一个对象 有且只有一个结果的时候正常，否则会报错
    
    
    class_name.objects.create(name='') 创建一个对象，返回的就是刚创建的对象
    class_name.objects.filter(condition).delete() 删除
    
    obj = class_name.objects.get(id='')
    obj.name = new_name 修改对象的属性（修改数据行某个字段的值）
    obj.save() 把修改同步到数据库
    
    多对多的操作：
        1、不能直接操作第三张关系表
        2、借助orm提供的方法,使用查询到的对象操作（一定是一条数据，不然会报错）【0】
            1、all（）
            2、add(id1, id2)
            3、set([id1, id2])
            4、clear()
    创建model：
        AutoField 必须指定primary_key=True
        外键：
            sql语句：
                create table book (
                    id int primary key auto_increment,
                    title varchar(30) not null,
                    press_id int not null,
                    constraint fk_press foreign key(press_id) references press(id) 
                    on delete cascade
                    on update cascade
                )
            press = models.ForeignKey(to=''---表， on_delete-models.CASCADE--django1.x模式是联级的删除，不写也可以，2.x中需要写明)
            press在数据库中自动变成press_id
            查询的时候press_id是press的id，press是press的对象
            外键修改：
                book_obj = Book.objects.create(title='', press=出版社对象）
                book_obj = Book.objects.create(title='',press_id=出版社的id）
    给数据库中已经存在的表中添加另外一个字段的时候，这个字段即没有默认值也不能为空，ORM就不知搭配数据库中已经存在的字段该怎么处理这个字段，所以一般在新增字段de
    时候。会指定一个默认值或者允许为空
    
    多对多的关系创建表：
        1、自己创建第三张表
        2、让ORM创建第三张表
        books = models.ManyToManyField(to='Book')
        3、
        搜索数据:
            author_obj.books.all()
        修改：
            author_obj.set([id1, id2, id3])
            author_obj.add(id1, id2, id3)
        清空：
            author_obj.clear() 清除对应关系
            
Django框架：
    MVC：Model View Controller 模型（Model） 视图（View）控制器（Controller) 具有耦合低，重用性高，生命周期成本低等的特点
    django框架把它拆分成三个部分，MTV（Model---负责业务对象和数据库的对象（ORM），Template---负责如何把页面展示给用户， View---负责业务逻辑，并且在适当的时候调用Model和Template）
csrf_token： 这个标签用来跨站请求伪造保护在页面的表单上写{% csrf_token %}

图书管理系统：
    编辑或者删除的时候隐式的提交id， path/?id={{}} url传递参数， ？后的参数不会影响路由判断路径
        id 和name都使用post提交，设置id的框为隐藏不展示
    select标签把已经存在的出版社在页面上展示出来，使用模版语言的for循环
    删除增加一个几秒后跳转到指定页面的操作：
        location.href
        setTimeout()
        setinterval()
request.GET 是取url里面的参数，和什么请求是没有关系的
request.POST.getlist() 用来获取list数据
取一条数据的时候如果用的是filter，一定要取第一条数据[0]!!!
注释csrf， form表单可以提交请求
    相当于在form表单中添加了一个隐藏的input标签。name csrfmiddlewaretoken value asss... 64


装饰器：
    def wrapper(fn):
        def inner(*args, **kwargs):
            执行被装饰函数之前的操作
            ret = fn(*args, **kwargs)
            执行被装饰函数之后的操作
            return ret
        return inner
        
    def func(tools):
        pass
        
    func = wrapper(func)
    print(func(tools))
    
母版继承：（避免写重复的代码）
    1、定义一个母版， 普通的html代码。base.html
    2、在母版中定义block块
    3、子页面中继承的母版 {% extends 'base.html' %}
    4、重写block块
    
    注意事项：
        1、{% extends 'base.html' %}写在第一行
        2、{% extends name %} name写继承的母版的名字的字符串
        3、自定义的内容写在block中
        4、定义几个blcok块，一般要有js css
    通常会在模板中定义页面专用的css和js块。方便子页面替换

模板：
    组件：
        可以将页面常用的页面内容， 如导航条，页尾信息等组件保存在单独的文件中，然后在需要使用的地方按照如下语法导入即可
        1、写一段代码 nav.html
        2、{% include 'nav.html' %}
        
    静态文件相关：
        1、{% load static %}
        2、{% static '相对路径' [as 别名] --- 保存为一个变量%}  去settigs中获取STATIC_URL '／static／'和相对路径进行拼接
        3、{% get_static_prefic %}去settings中获取static_url, '/static/'
            {% get_static_prefic %}相对路径
    
    自定义inclusion_tag
        1、在app下创建一个templatetags的python包（名字不能错）
        2、在包下写py文件 eg.mytags
        3、编辑文件 from django import template
                   register  = template.Library()
        4、定义函数 可以接收参数， 返回一个字典
        5、函数加上装饰器 @register.inclusion_tag('pagination.html'_
        6、函数返回的字典，交给pagination.html渲染
        
    
"""
