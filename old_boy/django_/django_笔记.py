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
https://www.cnblogs.com/maple-shaw/articles/9323320.html
https://www.cnblogs.com/maple-shaw/articles/9403501.html
https://www.cnblogs.com/maple-shaw/articles/9502602.html
https://www.cnblogs.com/maple-shaw/articles/9414626.html
https://www.cnblogs.com/maple-shaw/articles/9333824.html#4289892
9414626
https://www.cnblogs.com/maple-shaw/articles/9524153.html
https://www.cnblogs.com/maple-shaw/articles/9537320.html

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
            
    拆表：一对一（foreign_key unique)
        不是经常查询的字段，分表
        
        
            
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
        
    simple_tag 
        和自定义filter类似，只不过接收更加灵活的参数
        注册simple tag 
            @register.simle_tag(name="plus")
            def plus(a, b, c)
                return "{}+{}+{}".format(a, b, c)
                
        使用自定义simple tag
            {% load app01_demo %}
            simple_tag
            {% plus "1", "2", "abc" %}
    
    inclusion_tag
        多用于返回html代码片段
        templatetags/my_inclusion.py
        from django import template

        register = template.Library()
        
        @register.inclusion_tag('result.html')
        def show_results(n):
            n = 1 if n < 1 else int(n)
            data = ["第{}项".format(i) for i in range(1, n+1)]
            return {"data": data}
            
        templates/snippets/result.html

        <ul>
          {% for choice in data %}
            <li>{{ choice }}</li>
          {% endfor %}
        </ul>  
        
        templates/index.html
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta http-equiv="x-ua-compatible" content="IE=edge">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>inclusion_tag test</title>
        </head>
        <body>
        
        {% load inclusion_tag_test %}
        
        {% show_results 10 %}
        </body>
        </html>
        
        流程：页面中使用inclusion_tag 传参数给函数，函数返回一个数据，给inclusion_tag的页面调用
        
    视图：
        1、CBV和FBV
            FBV function based view
            CBV class based view
        
        2、CBV的流程
            定义：
                from django.views import View
                class AddPress(View):  # 类一定要继承View
                    def dispatch(self, request, *args, **kwargs):
                        ret = super().dispatch(request, *args, **kwargs)
                        return ret
                        
                    def get(self, request):
                        print("get")
                        print(self.request)
                        print render(self.request, 'add_press2.html')
                        
                    def post(self, request):
                        print("post")
                        press_name = request.POST.get("name")
                        press.objects.create(name = press_name)
                        return redirect('/press_list/')
            使用： 
                url(r'^add_press/$', views.AddPress.as_view())  # 固定写法， 添加出版社
            流程：
                1、AddPress.as_view()  view函数
                2、当请求到来的时候执行view函数
                    1、实例化自己的类 self
                        self = cls(**initkwargs)
                    2、self.request = request
                    3、执行self.dispatch(request, *args, **kwargs)
                        1、执行父类的dispatch方法
                            判断请求方式是否被允许 http_method_names = []
                                允许的情况
                                 handler = 通过反射获取 get  post 方法
                                不允许的情况
                                 handler = 不允许的方法
                                handler（request，*args, **kwargs)
                        2、返回httpResponse对象
                    4、返回httpResponse对象给django
                1、加在方法上：
                    @method_decorator(timer)
                    def get(self, request):
                        pass
                2、加在dispatch上
                    @method_decorator(timer):
                    def dispatch(self, request, *args, **kwargs)
                        pass
                3、加在类上
                    @method_decorator(timer, name='post')
                    @method_decorator(timer, name='get')
                    class AddPress(View):
                        pass
                    
        3、request
            print(request.method) GET PIST PUT DELETE OPTION
            request.GET request.POST request.FILES(获取文件参数） request.path_info url, 不包括域名端口和参数
            request.body request.scheme request.path 
            request.encoding
            request.META request.get_host() request.get_full_path() request.is_secure() request.is_ajax()
        4、response
            from django.shortcuts import render, HttpResponse, redirect
            1、HttpResponse, HttpResponse('str')
            2、render(request, 'html文件名'， {})  html代码
            3、redirect(跳转的地址）Location: /press_list/
            4、HttpResponse(json.dumps(ret)) Content-Type:text/html;
               charset = utf-8
               JsonResponse(ret) Content-Type: application/json
    3、路由
        pass
    
    url命名和反向解析
        1、命名：
            url(r'^press_list/$', views.press_list, name = 'press_list),
            url(r'^home/$', views.press_list, name = 'press_list'),
            分组
            url(r'^home/([0-9]{4}/([0-9]{2})/$', views.home, name='home'),
            命名分组
            url(r'^home/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.home, name='home')
            分组和命名分组区别： views中接收参数一个是位置参数，一个是关键字参数
        2、反向解析：
            1、在视图中的应用
                from django.urls import reverse
                reverse('press_list') '/press_list/'
                分组：
                    reverse('home', args=('2008', '09')) 'app01/home/2008/09'
                命名分组：
                    reverse（'home', args=('2008', '09')) 'app01/home/2009/01'
                    reverse('home', kwargs = {'year': '2019', 'month': '10'})
            2、在模板中的应用：
                {% url 'press_list' %}  '/press_list/'
                分组
                {% url 'home' '2019' '10' %} '/app01/home/2008/09/'
                命名分组：
                {% url 'home' '2009', '10' %} 'app01/home/2009/10'
                {% url 'home' month='10' year='2018' %} '/app01/home/2019/10/'
                
    namespace 
        url(r'app02/', include('app02.urls', namespace='app02')),
        
        reverse('app02:home', kwargs={'year': '2019', 'month': '1'})
        
        {% url 'app02:home' '2018' '10' %}
                
ORM:（对象和关系型数据库的映射，将程序中的对象自动持久的持久化到关系型数据库中， 在业务逻辑层和数据库层之间充当了桥梁的作用）--操作对象来操作数据库数据
    优点：
        开发效率高，
    缺点：
        有一定的局限性，效率低
    常用字段(记住常用的自定义类型）
        autoField 一个model不能有两个autoField
        DateTimeFiled9(auto_now_add--添加的时候把当前时间数据填进去，auto_now, 修改的时候也会更新时间数据) auto_now/auto_now_add/default是互斥的，不能同时设置
        charField
        IntegerField
        BooleanField
        choice 
        ...
        自定义字段
        
        null=True 可以为空 （数据库层面）
        blank=True 可以为空（django层面，）一般这两个都写
        db_column 数据列的名字， 自定义名字，一般用本身的名字
        db_index 字段是否可以建立索引
        choices admin中显示选择框的内容
        error_messages 自定义错误类型， {'null': '不能为空'}
        在数据类的下边在定一个类Meta
        class Meta:
            db_table = 'new_name'  # 数据库生成的表名称，默认是app名称，下划线，类名
            # 联合索引
            index_together = [
            ]两个存在的字段
            # 联合唯一索引
            unique_together =((),)两个存在的字段
            #排序
            ordering = （"id")
     
    必知必会13条       
        get 查询不到或者查询到多个就报错
        filter 查询所有满足条件的对象 -- 对象列表
        exclude 排除 查询出所有不满足条件的对象 -- 对象列表
        values 取具体的数据，对象列表，里面的元素是字段，字段：值 没有指定参数，获取全部字段，指定字段，则获取指定的字段数据  ，返回字典序列     
        values_list 获取具体的数据，对象列表 元素 值， 返回元组序列
        order_by('id/-id') -为降序， 多个字段（一个字段重复，按照第二个字段排序）
        reverse 对查询结果反序，前面需要先进行排序，才有效
        distinct() 去重复
        count() 计数， 返回总数
        first（） 获取当前结果的第一条，是一个对象，类似之前取出来是一个queryset之后用索引[0]取第一个的方法
        exists() 数据是否存在
        返回的是对象列表的方法：
            all. filter exclude order_by reverse distinct values values_list
        返回对象的方法：
            get first last create
        返回布尔值：
            exist
        返回数字的：
            count
    单表查询之双下划线：
        __gt greater than 大于
        __lt less than 小于
        __gte greater than equal 大于等于
        __lte less than equal 小于等于
        __in=[] list in
        __range = [1, 3] 范围， 大于等于小于等于,等价与between and
        __contains 包含 模糊查询
        __icontains 包含 忽略大小写
        __startswith 以什么开头
        __istartswith 以什么开头 忽略大小写
        __endswith 以什么结尾
        __isnull 是否为空
        [limit: offset] 
        __regex正则匹配，__iregex 不区分大小写
    
    外键的查询：
        book_obj.publisher 查询外键的出版社对象
        obj = models.Book.objects.filter(publisher__name = 'xxx') 内联查询方式, 两张表的时候__表示跨表查询
        obj = models.Book.objects.all().vaues("title', 'publisher__name') 查询字段。
        从book 到 publisher为正向查询
        
        从publisher 到 book是反向查询
        obj = models.publisher.objects.get(id=1)
        print(obj.book_set.all()) book_set 固定写法，管理对象（表名小写_set)
        obj.books.all
        obj.books.set(set_list对象列表)
        obj.books.add(set对象)  books--related_name
        在models中：
            publisher = models.ForeignKey(to ='publisher;, related_name = 'books') 此上边的book_set要改成这里的relate_name
            查出版社 
                models.publisher.objects.filter(id=models.Book.objects.get(title='xxx').publisher_id) 比较麻烦
                models.publisher.objects.filter(books__title = 'xxx')
        related_query_name 设置了之后查询只能用这个名字查询，不影响create等
        Publisher.objects.filter(xxxx__title='跟太白学理发') 书名
        字段查找（跨表）：
            关联字段__字段
        对象查找：
            obj.表名_set 
        字段查找:
            表名__字段
    多对多的查询
        正向：
            obj = Author.objects.filter(id=1)
            
            obk.books.set(list)
            obj.books.add(*list)
            obj.books.remove(*list)
            obj.books.clear()
            obj.books.create(title = 'xxx', price=12, pulisher_id=1) 创建author关联的书籍的对象
        反向：
            obj = Book.objects.get(id=1)
            obj.author_set.all()
            在author中book设置related_name. 替代author_set
    在关联的任何一段，不需要调用save方法
    
            
聚合和分组：
    聚合：aggregate(Max('price'))
        是一个终止子句， 可以查询多个，但是不能在有其他的操作，
        aggregate(max = Max('price')) 新命名，位置传参要放在关键字传参前面
        from django.db.models import Avg, Sum, Max, Min, Count
        models.Book.objects.all().aggregate(Avg("price"))
    分组：annotate() 返回的是对原来的查询结果增加一列聚合结果的querySet， 键的名称是按照字段和聚合函数的名称自动生成的
    
F和Q：
    F:
        from django.db.models import F
        models.Book.objects.filter(sale__gt=F("kucun").values()
        把字段的值拿出来
            应用：翻倍， 
    Q:
        from django.db.models import Q
        使用：
            Q(id__lte=3)|Q(id__gte=6)
            & | ~ 与或非
            
事务：
    同数据库中的事务概念（原子性）
    from django.db import transaction
    with transaction.atomic():
        new_publisher = '''
        
    
cookie:
    是一个保存在浏览器本地的一组组键值对，特征：是服务器让浏览器去保存的，浏览器有权利是否进行保存
    为什么要有cookie：
        http协议是无状态的，每次请求都是无关联的，都没有办法保存状态，使用cookie保存状态
    一般用在登录
        在登录成功之后
            ret = redirect('home')
            ret.set_cookie('is_login', '1'， max_age=xx) 设置键值对
            ret.set_signed_cookie(key, value, max_age, salt='xx') 加盐加密cookie
            return ret
        获取cookies：
            request.COOKIES
            request.get_sgined_cookie(key, salt='xxx', default=''--取不到时候的默认值)
        在需要使用cookie的时候去判断cookie的值是否为为期望值
        request.get_full_path 提交数据的时候，提交给当前的路径
        
        设置cookie：
        删除cookie：
            登录注销的时候
            ret.delete_cookie(key)
            
        参数：
            max_age: 最大存活时间
            path: 一级域名，二级域名
            
    不允许使用cookie之后，网站登录会出现问题
    数据不能太长
    不安全(明文）
    
    
session：
    与cookie配合使用
    存在服务器上的键值对
    为什么要用session：
        cookie保存在浏览器上，不安全
        cookie的长度收到限制
    使用：
        设置 request.session['is_login'] = 1
            request.session.setdefault(key, value)
        获取：
            request.session[key]
            request.session.get(key)
        删除：
            del request.session[key] 删除某一个键值对
            request.session.delete() 删除该用户的所有session数据，不删除cookie （拿着钥匙却找不到箱子了）
            request.session.flush() 删除该用户的所欲session数据， 删除cookie （钥匙也删除了）
        
        配置：
            默认存放在django_session
            setting中有两个相关设置
            默认到期时间是两周之后
            
            # Cookie name. This can be whatever you want.
			SESSION_COOKIE_NAME = 'sessionid'
			# Age of cookie, in seconds (default: 2 weeks).
			SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2
			
			# Whether to save the session data on every request.
			SESSION_SAVE_EVERY_REQUEST = False
			# Whether a user's session cookie expires when the Web browser is closed.
			SESSION_EXPIRE_AT_BROWSER_CLOSE = False
			
			SESSION_ENGINE = 'django.contrib.sessions.backends.db'
            
        浏览器中存session_key 叫做session_id
        常用：
            删除数据库中的内容，但是不删除浏览器中的
        设置超时时间：
            request.session/set_exipry()
        清除所有过期的session
            request.session.clear_exipred()
            
            
        
中间件：
    可以实现给多有请求加上相同的操作
    是一个中间类，用来在全局范围内处理和响应的一个钩子，使用不当，会影响性能
    五个方法：
        process_request(self, request)
        process_view(self, request, view_func, view_args, view_kwargs)
        process_template_response(self, request, response)
        process_exception(self, request, exception)
        process_response(self, request, response)
        
        process_request:
            执行时间：
                在视图函数执行之前
            参数 
                request  视图函数中用到的request
            执行顺序
                按照注册顺序 顺序执行
            返回值：
                None: 正常流程走
                HttpResponse对象
                    当前中间减后面的中间件的process_request和process_response方法，视图函数都不执行，执行当前中间的process_response方法及之前的中间的process_response方法
                    执行当前中间件的process_response方法以及之前的中间的process_response方法
        
        process_response
            执行时间：
                在视图函数执行之后
            参数
                request  视图函数中用到的request
                response 视图函数中返回的response
            返回值：
                必须是response对象
            执行顺序；
                按照注册顺序倒序执行
        
        process_view
            执行时间
                process_request之后，以及路由匹配之后，在视图函数执行之前
            参数：
                view_func   要执行的视图函数
                view_args 视图函数的位置参数
                view_kwargs 视图函数的关键字参数
            返回值：
                None 正常走
                response: 不会调用其他中间件的process_view，视图函数，执行全部的response函数
            
            执行顺序
                按照注册顺序 顺序执行
            
        process_exception(self, request, exception)
            执行时间（触发条件：视图函数有异常才执行）
                在视图函数之后，在process_response之前
            参数
                excepion  错误信息对象
            返回值
                None 正常走，给下一个中间件的process_exception来处理异常
                HttpResponse对象
                    注册顺序之前的中间件的process_exception方法不走了
                    执行所有中间件的process_response方法， 返回给浏览器
            执行顺序
                按照注册顺序倒序执行
        
        process_template_response
            执行时间（触发条件：response对象要求有一个render方法） 视图函数执行完成后立即执行
                在视图函数之后，在process_response之前
            参数
            返回值
                返回response
                不返回视图函数的return的结果了，而是返回视图函数的return的值（对象）中render方法的结果）
            执行顺序 
                按照注册顺序倒序执行
            
    
    
CSRF中间件
    CSRF跨站请求伪造
    补充：
        两个装饰器
        from django.views.decorators.csrf import csrf_exempt, csrf_protect
        csrf_exempt  给单个视图排除校验
        csrf_protect  给单个视图必须校验
        
    
Ajx:
    提交数据，但是不刷新页面            
        
        
        
        
json：
    一种数据结构，跨平台跨语言
    python中json数据的转换
    1、数据类型
        字符串 数字 布尔值 列表 字典 None
    2、序列化 python的数据类型 -》json字符串
        json.dumps(python的数据结构）
        json.dump(python的数据类型,f-文件句柄）
    3、反序列化 json字符串 -》python放入数据类型
        json.loads(json字符串）
        json.load(json字符串，f--文件句柄）
    js中json数据的转换
    1、数据类型 
        字符串 数字 布尔值 数组 对象 null
    2、序列化 js的数据类型 0》 json字符串
        JSON.stringify(js的数据类型）
    3、反序列化 json字符串 -》js数据类型
        JSON.parse(json字符串）
    JsonResponse({})
    JsonResponse([], safe=False)
    
Ajax:
    1、浏览器向服务器发请求的方式
        在浏览器的地址栏中输入url 回车 GET
        form表单发请求
            action 提交的地址
            method 请求方式 GET/POST
            input标签必须要有name属性
            一个类型是submit的input标签 或者button按钮
        a标签 GET
        Ajax：
            AJax是一个与服务器交互的技术， JS技术
            特点：异步 不刷新页面 数据量小
    使用jq发送ajax请求：
        导入jq
        $.ajax({
            url: 发送的地址,
            type: 'post',
            data:{
                k1:v1,
                k2:v2,
            },
            success:function(res){
                res 返回的响应的响应体
            }
            error:function(res){
                res 返回的响应的响应体
            }
        })
    ajax如何通过django的CSRF验证：
        1、在data中添加csrfmiddlewaretoken 的值
            {% csrf_token %}
            data: {
                csrfmiddlewaretoken: $('[name="cerfmiddlewaretoken"]').val(),
                k1:v1,
                k2:v2,
            }
        2、设置请求头
            headers:{"X-CSRFToken": $('[name="csrfmiddlewaretoken"]').val()
        3、导入文件
    上传文件
    

form：
    form
        完成的事情
            有input标签，让用户可以填数据
            校验form表单提交的数据
            提示错误信息
    django中的form
        定义
            from djsngo import forms
            
            class RegForm(forms.Form):
                user = forms.CharFiled(label="用户名"）
                pwd = forms.CharFiled(label="密码"）
        使用
            视图中
                form_obj = RegForm()
                return render(request, 'register2.html', {"form_obj": form_obj})
                form_obj.is_valid() 布尔值
                form_obj.cleaned_data 所有通过校验的字段的名字和值
                
                模板中：
                    {{ form_obj.as_p }}  自动生成多个p标签 包含label input框
                    {{ form_obj.user }} 生成某个字符安的input框
                    {{ form_obj.user.errors }} 某个字段的所有错误信息
                    {{ from_obj.user.errors.0 }} 某个字段错误信息的第一个
                    
                    {{ form_obj.errors }} 所有字段的错误信息
        字段和参数
            参数
            label = '用户名', 标签的展示
            min_length 校验的规则 最小长度
            initial = 'alex',  初始值
            error_messages = { 自定义错误提示
                'min_length' : ''
                'required': ''
            }
            disabled 是否是不可修改的
            
            widget = widgets.PasswordInput()  插件 执行数据的类型
        
        校验
            1、每个字段有默认的校验方法
                min_length = 6,
                max_length = 6
                required = False
            2、自定义校验规则
                validators = [校验器1， 校验器2--可以是函数，也可以是自定义]
                1、
                    from django.core.validators import RegexValidator
                    RegexValidator(r'^1[3-9]\d{9}$', '错误提示信息')
                2、自定义函数
                    from django.core.exceptions import ValidationError
                    
                    def check_name(value):
                        if 'alex' in value:
                            raise ValidationError('xxxx')
            3、钩子函数
                局部钩子
                    def clean_phone(self):
                        value = self.cleaned_data.get("phone")
                        if re.match(r'^[3-9]\d{9]$', value):
                            return value
                        raise ValidationError("xxx")
                    通过校验： 返回当前字段的值
                    不通过 raise ValidationError()
                全局钩子
                    def clean(self):
                        pwd = self.cleaned_data.get("pwd")
                        re_pwd = self.cleaned_data.get("re_pwd")
                        
                        if pwf == re_pwd:
                            return self.cleaned_data
                        self.add_error("re_pwd", '')
                        raise ValidationError("两次密码不一致")
                    通过校验：
                        返回self.cleaned_data
                    不通过：
                        self.add_error('字段名'， '错误提示'）
                        raise validationError()

django自带的用户认证
    auth:默认使用auth_user表来存储用户数据 from django.contrib import auth
        创建超级用户
            python manage.py createsuperuser 
            密码是加密的
        认证 校验用户名和密码
            obj = auth.authenticate(request, username, password)
            会在user对象上设置一个属性来标示后段已经认证了该用户，且该信息在后续的登录过程中是需要的
            认证成功返回对象 失败None
            is_authenticated() 判断当前请求是否通过了认证
        保存登录状态 记录到session login(request, user-经过认证的user对象)
            实现用户登录的功能，本质上会在后段为该用户生成相关的session数据
            auth.login(request, obj)
            from django.contrib,auth.decorators import login_required
            装饰器 login_required() 给某个视图添加登录校验，没有登录会跳转到django默认的URL；／accounts/login'/
                可以在setting文件中lOGIN_URL进行修改
        注销 删除session logout(request) 无返回值， session信息会全部清除
            from django.contrib.auth import logout
        对象和匿名对象（不需要session的情况）
        判读登录状态
        创建用户 create_user() 密码是加密的
            from django.contrib
            create_superuser() 创建超级用户
        is_active 是否可以登录  
        检查密码：
            check_password(password)
            set_password(password) 
            设置完之后一定要调用用户对象的save方法
            
        user对象的属性 
            username 
            password
            is_staff 用户是否拥有网站的管理权限
            is_active 是否允许用户登录
        拓展默认的auth_user
            继承AbstractUser类，定义一个自己的Model类
            在setting中说明：
                AUTH_USER_MODEL = 'app名.UserInfo;
            一旦执行类新的认证系统所用的表，就要在数据库中创建该表，不能继续使用原来默认的auth_user表了
         
                        
        
    
"""
