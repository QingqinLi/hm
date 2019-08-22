# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
"""
博客：https://www.cnblogs.com/majj/p/?page=2
https://www.cnblogs.com/majj/p/9169416.html
mysql是基于c/s的服务器端的软件
    mysql服务端
        -server端开启
        -解析指令
        -对文件夹，文件，数据的增删改查
    mysql客户端
        -连接server端
        -发送指令（sql语句）
        
    安装mysql
        数据库服务器
        数据库管理系统（mysql软件）
        数据库（data／db 一个文件夹）
        表：一个文件
        记录：多个字段的信息组成一条记录，即文件中的一行内容
        
        下载：
            mysql.msi
            解压包到指定的路径
            添加bin到系统的环境变量
            初始化软件data目录
                生成data目录 存放数据库-文件-记录
                初始化的时候一定要等着程序自己退出
                mysqld --initialize-insecure
        
        开启mysql服务端
            mysqld（必须授权）
        
        开启客户端 连接服务端
            mysql -uroot -p
        
        安装windows服务
            mysqld --install 安装windows服务
            mysqld --remove 移除window服务
            
            net start mysql 开启服务端
            net stop mysql 关闭服务端
            
        忘记密码：
            1、先关掉之前的mysql服务器的进程
            2、跳过授权表开启mysql的服务端 mysqld --skip-grant-tables(开启服务端的约束条件跳过授权）
            3、客户端连接 mysql -uroot -p
            4、更改密码 update mysql.user set authentication_string=password('pwd') where User='root';
            查看进程号
                tasklist | findstr mysql
            杀死进程
                taskkill /F /PID 进程号
    
    统一字符编码
        在Mysql软件的目录下新创建一个my.ini
        [mysqld]
			# 设置mysql的安装目录 **后面的路径一定是安装sql的目录（自己电脑的）**
			basedir=C:\mysql-5.7.22-winx64\mysql-5.7.22-winx64
			# 设置mysql数据库的数据的存放目录，必须是data
			datadir=C:\mysql-5.7.22-winx64\mysql-5.7.22-winx64\data
			sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES
			# mysql端口
			port=3306
			# 字符集
			[mysqld]
			character-set-server=utf8
			collation-server=utf8_general_ci
			[client]
			default-character-set=utf8
			[mysql]
			default-character-set=utf8
			
			再次重启mysql 服务端
			
			
			mysql -uroot -p
			\s;查看mysql软件配置
			
        创建mysql用户
            创建用户指定密码
                create user 'mjj'@'192.168.1.1' identified by '123';
                create user 'mjj'@'192.168.1.%' identified by '123':
                create user 'yinying--用户名'@'%--指定的登录ip' identified by '91'---密码;
            使用账号密码登录
                mysql -uyining -h 192.168.13.29 -P 3306 -p91
            
        show databases: 查看所有的数据库
        use db1;使用数据库
        desc s1; 查看表设计
        
        创建表
            create table t1(id int, name char(10)) defult charset='utf8';
            insert into t1(id, name) values(1, "alex"),(2,"eu");
            
        查询所有的数据：
            select * from t1;
        查询个别字段的数据
            select id from t1;
            
    数据类型：
        数值类型：
            默认类型
                默认是有符号（-128，127）
                无符号（0， 255）
                unsigned：给当前的字段设置约束
                create table t2(x tinyint unsigned);
            浮点型：
                float
                double
                decimal
            datatime ***'
                YYYY-MM-DD HH:MM:SS
                date 日期
                time 时间 now() 函数获取现在的datatime
            字符
                char(n) 定长 存储速度快 但是浪费空间
                varchar 变长 查询速度相对较慢 但是节省空间
            enum 多选一
                create table consumer(
                    id int unsigned,
                    name char(20),
                    sex enum('male', 'female') not null default 'male',
                    fav set("1","2","3"),
                    
                    );
                insert into consumer(id, name, sex, fav) values(1, 'a','male', '1,2')
                
            set 多选多
                
            表的约束
                作用： 保证数据的完整性和一致性
                not null default
                unique: 不同的唯一的
                    单列唯一：
                        只有一列是唯一的
                    多列唯一：
                        多个字段都设置unique
                        unique(x1),
                        unique(x2),
                        
                    组合唯一：
                        unique(x1, x2)
                primary key 现在的sql版本中 只允许表中又一个主键 通常是id
                
                not null ~~unique
                
                auto_increment 自增长
                
                foreign key 外键
                    on delete cascade  一起删除
                    on update cascade,  一起更新
                    首先创建被关联表（主表）
                    constraint fk_dep foreign key(dep_id) references dep(id)
                    on delete cascade 
                    on update cascade,
                    外键的变种：
                        一对多或者多对一
                        多对多'
                            需要定义一个这两张表的关系表来专门存放二者之间的关系
                            创建数据
                                create table book(
                                    id int primary key auto_increment,
                                    name varchar(20)		
                                );
                                
                                create table author(
                                    id int primary key auto_increment,
                                    name varchar(20) not null
                                
                                );
                                
                                create table author2book(
                                    id int primary key auto_increment,
                                    book_id int not null,
                                    author_id int not null,
                                    constraint fk_book foreign key(book_id) references book(id)
                                    on delete cascade
                                    on update cascade,
                                    constraint fk_author foreign key(author_id) references author(id)
                                    on delete cascade
                                    on update cascade						
                                );
                                  
                        一对一
                            在左表foreign key右表的基础上，将左边的外键字段设置成unique即可
                
    表单查询
        单表查询  
            关键字：
                from
                where
                group by
                having（必须用在group by之后）字段必须是group的字段或者是聚合函数的内容
                select
                distinct
                order by(asc desc)
                limit
                1、找到表from
                2、拿着where指定的约束条件，去表／文件中取出一条条的记录
                3、将取出的结果进行分组group by 如果没有group by则整体为一组
                4、将分组的结果进行having过滤
                5、执行select
                6、去重
                7、将结果按照条件排序 order by
                8、限制结果的显示条数
            group by
                select A.c from (select post,max(salary)as c from employee group by post) as A;
                使用分组：
                    sql_mode = 'ONLY_FULL_GROUP_BY'
                    分组之后只能查询分组的字段，如果想要查询组内的其他字段的信息，必须要借助聚合函数
                    max()
                    min()
                    avg()
                    sum()
                    count()
                    group_concat()
                    查询岗位名以及岗位包含的所有员工名字
                        select post,group_concat(name) from employee group by post;
                
                    
                        select post,avg(salary) from employee group by post having avg(salary) > 10000;
                         
                        select post,group_concat(name),count(1) 
                            from employee
                        group by post having count(1)< 2;
                        
                        
                        select post,avg(salary) as A from employee group by post having A > 10000 order by A desc;
                        
                        select * from employee order by age asc,id desc;
                    
                          
        多表查询：
            内连接：只连接匹配的行
                select * from employee inner join department on employee.dep_id = department.id;
                
                等效：
                        select * from employee,department where department.id = employee.dep_id;
                        select * from employee inner join department on department.id=employee.dep_id;
            左连接：显示左表的全部记录(左边的数据没有匹配到内容也会显示）
                select * from employee left join department on employee.dep_id=department.id;
            右连接：显示右表的全部记录
                select * from employee right join department on employee.dep_id=department.id;
				select * from employee full join department on employee.dep_id=department.id;（没有全连接）
			没有匹配条件的交叉连接，生成笛卡尔积
			全外连接：显示左右两个表的全部记录
			    mysql不支持全外连接full join 但是可以通过union all／union 两个表的左右连接来实现全外连接
			    union all和union的区别： union会去掉相同的记录
		子查询：
            子查询是将一个查询语句嵌套在另一个查询语句中， 内层查询语句的查询结果，可以为外层查询语句提供查询条件，
            关键字： in/not in/any/all/exists/not exists
            还可以包含比较运算符：=、！=、>、<
            exists 关键字表示存在，在使用exists关键字的时候，内层查询语句不返回查询的记录，而是返回一个真假值，当返回True的时候，外层查询语句会继续查询，否则外层查询语句不进行查询
            
		
		索引：
		    
    sql简单总结：
        建表：
            我们要保证数据的一致性和完整性
            表是如何设计的
            数据类型
            约束：
                not null default
                unique
                primary key
                auto_increment
                foreign key
            外键的变种：
                多对一
                多对多
                一对一
            单表查询：
                关键字的优先级
                from
                where
                group by
                having
                select
                order by
                limit
            多表查询
                内连接 inner join
                左连接 left join
            子查询
            多张表连接起来，最终还是但表查询
            多表查询
        
        
        
可拓展性
jquery库
                         
            
        
        
"""
