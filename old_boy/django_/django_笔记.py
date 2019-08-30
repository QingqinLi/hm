# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
"""
https://www.cnblogs.com/liwenzhou/p/8296964.html
http://www.cnblogs.com/liwenzhou/p/7931828.html

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
        2、render： 返回一个HTML文件，打开文件，读取内容，按照响应格式返回， {'key': 'value'} 替换特殊符号，按照响应格式返回
        3、redirect 跳转 绝对地址（不同网站之间的跳转），相对地址（同一个网站之间的跳转），锚点（同一个网站页面位置的跳转）
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
        2、告诉djamgo连接哪个数据库
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
            press = models.ForrignKey(to=''---表， on_delete-models.CASCADE--django1.x模式是联级的删除，不写也可以，2.x中需要写明)
            press在数据库中自动变成press_id
            查询的时候press_id是press的id，press是press的对象
    给数据库中已经存在的表中添加另外一个字段的时候，这个字段即没有默认值也不能为空，ORM就不知搭配数据库中已经存在的字段该怎么处理这个字段，所以一般在新增字段de
    时候。会指定一个默认值或者允许为空
    
    多对多的关系创建表：
        1、自己创建第三张表
        2、让ORM创建第三张表
        3、
        搜索数据的时候，s
    
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

        
    
"""
