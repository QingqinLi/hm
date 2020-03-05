"""
数据表：
    自关联 self
    choices

modelform
    该标签
        vbosename
        labels
    Meta 只对默认生成的字段有作用
    model.save() 密码是明文的

day74
数据库部分设计
    1. 销售
        1. 销售注册，登录系统
            - 用户表
        2.销售添加客户信息，成为销售的私户
            - 客户表

        3. 销售固定时间跟进客户
            - 跟进记录表
        4. 客户报名
            - 报名记录表
            - 班级表（必须有）
            - 校区表
            - 合同表
        5. 销售审核报名，学生进行缴费。
            - 报名记录表 更改审核状态
            - 缴费记录表 销售收到钱
        6. 销售将钱交给财务，财务对缴费记录进行审核
            - 缴费记录 更改审核状态
        7. 自动修改学生状态
            - 客户表  状态改成缴费成功

    2. 班主任
        1. 每天创建课程记录，记录每天上课的情况。
            - 用户表
            - 班级表
            - 课程记录表
        2. 再根据课程记录，生成学生的学习记录，修改考勤情况。
            - 学习记录表

modelForm (比form使用方便）
    3. modelform
        1. 定义
            class RegForm(forms.ModelForm):

                re_password = forms.CharField(
                        label='确认密码',
                        widget=forms.widgets.PasswordInput()
                    )

                class Meta:
                    model = models.UserProfile
                    # fields = '__all__'   # 所有字段
                    # exclude = ['']     # 排除的字典
                    fields = ['username', 'password', 're_password', 'name', 'department']  # 指定需要的字段

                    widgets = {}   # 插件
                    labels = {}    # 显示中文名  等同models给字段加verbose_name
                    error_messages = {}   # 字段的错误信息



            form_obj.is_valid()  # 校验数据
            obj = form_obj.save()   # 创建新的数据  create方法

客户信息展示：
    母版和继承：
        {% extends 'layout'%}
        {% load static %}
        {% static '文件路径' %}

        block js css content

    内容展示
        普通字段 {{ customer.qq }}
        choices {{ customer.get_(class_type--字段)_display }}
        多对多 定义方法 返回字符串
        显示状态 定位方法 返回HTML代码段 mark_safe

    分页：
        from django.utils.safestring import mark_safe  字符串不转义
        from django.utils.html import format_html


编辑：
    form_obj = CustomerForm(instance=obj)
	form_obj带着原有的数据，根据数据生成input的值
    form_obj = CustomerForm(request.POST,instance=obj)
    将提交的数据和要修改的实例交给form对象
    form_obj.save()  对要修改的实例进行修改

公户变私户：
    CBV
        self.request
        self.user属性 已经当前用户 获取到的是AnonymousUser对象 如果用户未登录，该属性的值是一个AnonymousUser实例（匿名用户）
    反射：
        orm操作：
            1、models.Customer.objects.filter(id__in=ids).update(consultant=self.request.user) 用多的一方修改
			2、self.request.user.customers.add(*models.Customer.objects.filter(id__in=ids)) 用少的一方修改

私户变公户：
    orm操作：
        models.Customer.objects.filter(id__in=ids).update(consultant=None)
        只有在models中设置null=True的外键才有remove 和clear方法
		self.request.user.customers.remove(*models.Customer.objects.filter(id__in=ids))
	模糊查询：

		all_customer = models.Customer.objects.filter(Q(qq__contains=query) | Q(name__contains=query),
                                                          consultant__isnull=True)
		all_customer = models.Customer.objects.filter(Q(('qq__contains',query) --- 一个元组) | Q(('name__contains',query)),
                                                          consultant__isnull=True)

		def get_search_contion(self,query_list):

			query = self.request.GET.get('query', '')

			q = Q()
			q.connector = 'OR'
			for i in query_list:
				q.children.append(Q(('{}__contains'.format(i), query)))

        return q
保留搜索条件：
    from django.http import QueryDict
    print('query',request.GET)  #  <QueryDict: {'query': ['alex']}>
    print(request.GET.urlencode()) query=alex
    request.GET.copy()  深拷贝

    QueryDict对象
    QueryDict对象._mutable = True   # 对字典进行修改

    QueryDict对象['page'] = 页码数  # 多个值
    QueryDict对象.urlencode()       # query=alex&page=1     ?query=alex&page=1

添加和编辑后跳转回原页面
    qd = QueryDict()
    qd._mutable = True

    qd['next'] = request.get_full_path()
    qd.urlencode()
    传递qd到要跳转的链接

展示客户的跟进记录 增加 和编辑


缴费记录

公户变私户的问题解决：
    多个销售同时申请一个客户
        先到先得
    mysql中添加行级锁
        begin
        for update 加锁 select * from student where id=1 for update
        commit

班主任的功能：
    班级的管理
        班级的展示
        添加班级
        编辑班级
    课程的管理：
        关联班级

    学习记录的管理
        批量添加
            student_list = []
            for student in all_students:
                student_list.append(modes.StudentRecord(course_record=course_obj. student=student))
            models.StudyRecord.objects.bulk_create(student_list)

        展示编辑学习记录
            FormSet = modelformset_factory(models.StudyRecord
"""
