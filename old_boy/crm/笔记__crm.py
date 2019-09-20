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

"""