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
            5、flush privileges; 刷新权限
            
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
            create table t1(id int, name char(10)) defult charset='utf8';（指定字符集）
            insert into t1(id, name) values(1, "alex"),(2,"eu");
            
        查询所有的数据：
            select * from t1;
        查询个别字段的数据
            select id from t1;
        数据操作：
            一、
            在MySQL管理软件中，可以通过SQL语句中的DML语言来实现数据的操作，包括
            
            1.使用INSERT实现数据的插入
            2.UPDATE实现数据的更新
            3.使用DELETE实现数据的删除
            4.使用SELECT查询数据以及。
            
            
            二、插入数据 INSERT
            1. 插入完整数据（顺序插入）
                语法一：
                INSERT INTO 表名(字段1,字段2,字段3…字段n) VALUES(值1,值2,值3…值n);
            
                语法二：
                INSERT INTO 表名 VALUES (值1,值2,值3…值n);
            
            2. 指定字段插入数据
                语法：
                INSERT INTO 表名(字段1,字段2,字段3…) VALUES (值1,值2,值3…);
            
            3. 插入多条记录
                语法：
                INSERT INTO 表名 VALUES
                    (值1,值2,值3…值n),
                    (值1,值2,值3…值n),
                    (值1,值2,值3…值n);
            
             4. 插入查询结果
                语法：
                INSERT INTO 表名(字段1,字段2,字段3…字段n) 
                                SELECT (字段1,字段2,字段3…字段n) FROM 表2
                                WHERE …;
            
            三、更新数据UPDATE
            语法：
                UPDATE 表名 SET
                    字段1=值1,
                    字段2=值2,
                    WHERE CONDITION;
            
            示例：
                UPDATE mysql.user SET password=password(‘123’) 
                    where user=’root’ and host=’localhost’;
            四、删除数据DELETE
            语法：
                DELETE FROM 表名 
                    WHERE CONITION;
            
            示例：
                DELETE FROM mysql.user 
                    WHERE password=’’;
            
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
                char(n) 定长 存储速度快 但是浪费空间 0-255 一个中文是一个字符，是utf8的三个字节 会使用空格填充
                varchar 变长 查询速度相对较慢 但是节省空间 0-65535 存储数据的真实内容 不会使用空格填充
                    length()：查看字节数
                    char_length():查看字符数
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
                where  (Where发生在分组group by之前，因而Where中可以有任意字段，但是绝对不能使用聚合函数。)
                group by (‘每’这个字后面的字段，就是我们分组的依据)
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
            查询数据范围：between and 
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
            
        
        索引：约束和加快查找
            索引的作用：
                没有索引的时候是从前往后一条一条的查询
                创建索引的本质，就是创建额外的文件（某种格式存储，查询的时候，先去格外的文件中查找，定好位置之后，再去原始的表中直接查询，斗牛士创建索引越多，所以也会对硬盘有损耗
                目的：
                    额外的文件保存特殊的数据结构
                    查询快，但是插入更新删除依然很慢
                    创建索引之后，必须命中索引才能有效
            hash索引和BTree索引：
                hash索引的类型：查询单条快，但是查询范围很慢
                btree索引：层数越多，数据量指数级增长（innodb默认支持这个）    
            普通索引：加速查找
                创建表的时候指定：index index_name(col);
                之后指定:create index index_name on table_name(col)
                删除索引: drop index index_name on table_name
                查看索引：show index from table_name
      
            唯一索引：加速查找和唯一约束
                创建表的时候指定：unique index index_name(col);
                创建索引：create unique index index_name on table_name(col)
                删除唯一索引：alert table table_name drop primary key;
                            alert table table_name modify col int, drop primary key
            主键索引：
            联合索引（多列）:将n个列组合称一个索引 （频繁使用n列来共同查询的时候）
                创建索引：create index index_name on table(col1,col2)
            联合主键索引：
            联合唯一索引：
            联合普通索引：
            
            覆盖索引：
                selct name from userinfo where name = 'xxx';
            索引合并：把多个单列索引合并使用
                select * from userinfo where name = 'xx' and id = 111;
                
            使用索引的方式：
                创建索引（大数量级的情况下使用）
                命中索引
                正确使用索引
            
            - 组合索引最左前缀
                如果组合索引为：(name,email)
                name and email       -- 使用索引
                name                 -- 使用索引
                email                -- 不使用索引
           (1)避免使用select *
           (2)count(1)或count(列) 代替count(*)
           (3)创建表时尽量使用char代替varchar
           (4)表的字段顺序固定长度的字段优先
           (5)组合索引代替多个单列索引（经常使用多个条件查询时）
           (6)尽量使用短索引 （create index ix_title on tb(title(16));特殊的数据类型 text类型）
           (7)使用连接（join）来代替子查询
           (8)连表时注意条件类型需一致
           (9)索引散列（重复少）不适用于建索引，例如：性别不合适
        
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
        
        
存储引擎：
    表类型又被称为存储引擎， mysql数据库提供来多种存储引擎
    show engines 查看所有支持的引擎
    show variales like 'storage_engine%'; 查看正在使用的存储引擎
    InnoDB存储引擎 支持事务，设计目标主要面向联机处理的应用，行锁设计，支持外键，是mysql的默认存储引擎，具备高可用，高性能高扩展
    MyISAM 存储引擎
        不支持事务，表锁设计，支持全文索引，主要面向一些OLAP数据库应用，他的缓冲池只缓存索引文件而不缓存数据文件
    ndb存储索引： 集群存储引擎，数据全部放在内存中，主键查找速度级快，是高可用，高性能，高可拓展性的数据库集群系统
    Memory存储引擎：数据都放在内存中，数据库重启活着放生崩溃，表中的数据都将小时，适合作为临时表，默认使用hash索引
    BLACKHOLE: 黑洞存储引擎，可以应用于主备复制中的分发系统
    执行引擎：create table t1(id int) engine=innodb
        
        
执行计划：
    explain 查询sql 用来显示sql执行信息参数 用于sql优化
    性能：all < index < range < index_merge < ref_or_null < ref（根据索引找一个或者多个值）< eq_ref（连接时候使用primary_key /unique) < system(系统）/const（常量）


慢日志记录： 开启慢日志查询日志，可以让MySQL记录下查询超过指定时间的语句，通过定位分析性能的平静，优化数据库系统的性能
可拓展性
进入MySql 查询是否开了慢查询 show variables like 'slow_query%'

分页性能相关方案：
limit 开始index，数量  越往后越需要的时间长，引文越往后查，全文扫描查询，回去数据表中扫描查询
    解决方案：
        1、只有上一页和下一页：记录当前页面的最大id和最小id
            下一页：
            select * from userinfo where id>max_id limit 10;
    
            上一页：
            select * from userinfo where id<min_id order by id desc limit 10;
        2、中间有页码的情况：
            select * from userinfo where id in(
               select id from (select * from userinfo where id > pre_max_id limit (cur_max_id-pre_max_id)*10) as A order by A.id desc limit 10
           );  
    
jquery库

创建用户和授权
    创建用户：
        create user 'alse'@'192.168.x.x' identified by '123';
        create user 'alex'@'192.168.x.%' identified by '123';
        create user 'alex'@'%' identified by '124';
    删除用户：
        drop user 'user_name'@'ip address';
    修改用户：
        rename user 'user_name'@'ip_address' to 'new_name'@'ip address';
    修改密码：
        set password for 'user_name'@'ip_address'=Password('new_pws')
    对当前用户的授权管理：
        show grants for 'user_name'@'ip_address'
        grant select, insert, update on db1.table1 to 'alex'@'%';
        grant all privileges on db1.* to 'alex'@'%';
        取消权限；
            revoke all on db1,table1 from 'alex'@'%';
            revoke all privileges on *.* from 'alex'@'%';
mysql备份命令行：
    备份表结构+数据
        mysqdump -u root db1 > db1.sql -p
    备份数据表结构：
        mysqdump -u root -d db1 > db1.sql -p
    #导入现有的数据到某个数据库
        #1.先创建一个新的数据库
        create database db10;
        # 2.将已有的数据库文件导入到db10数据库中
        mysqdump -u root -d db10 < db1.sql -p

pymysql:
    # 创建连接
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        database='db7',
        port=3306,
        charset='utf8'
    ) 
    # 创建游标
    cur = conn.cursor()
    执行sql：
    cursor.execute(sql)
    防止sql注入：  
        sql = "select * from userinfo where name = %(name1)s and pwd =%(pwd1)s "
        
        resCount = cur.execute(sql,{"name1":username,"pwd1":pwd}) 
        常见的sql注入：
            select * from userinfo where name = 'xxx'' or 1=1 -- and pwd = 'xxx' 绕过用户名和密码
            select * from userinfo where name ='xxx' -- 1=1 and pwd = 'xxx'(注释） 绕过密码
    增删改：执行sql之后要及时的commit，否则操作不生效
        conn.commit()
    关闭
        cur.close()
        conn.close()
    # 创建游标 指定返回值的类型,默认返回的是元组，不方便查看
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    取值：
        cur.fetchone() 取出一条记录
        cur.scroll(-1,mode='relative') 游标移动（releative:相对于自己，absolute：相对于起始位置
        cur.fetchall() 获取所有
        fetchmany(n) 获取n条数据
        

存储过程：
    #1. 准备表
    create table userinfo(
    id int,
    name varchar(20),
    gender char(6),
    email varchar(50)
    );
    
    #2. 创建存储过程，实现批量插入记录
    delimiter $$ #声明存储过程的结束符号为$$
    create procedure auto_insert1()
    BEGIN
        declare i int default 1;
        while(i<3000000)do
            insert into userinfo values(i,concat('alex',i),'male',concat('egon',i,'@oldboy'));
            set i=i+1;
        end while;
    END$$ #$$结束
    delimiter ; #重新声明分号为结束符号
    
    #3. 查看存储过程
    show create procedure auto_insert1\G 
    
    #4. 调用存储过程
    call auto_insert1();
    
    准备300w条数据
            
修改字符集：
    alter database db1 charset gbk;
        
localstorage
sessionstorage
"""
