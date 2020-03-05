# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
"""
https://v3.bootcss.com/css/
Bootstrap 是twitter开源的一个前端开发框架（HTML+CSS+JS）
目前到3.3.x
使用：
    下载：https://v3.bootcss.com/
    导入：link标签导入 bootstrap.css/bootstrap.min.css

常用样式类：
    1、容器
        container 类似于固定宽度并且支持响应式布局的容器
        container-fluid 类似于占用100%宽度，占据全部视口（viewport）的容器
        
    2、栅格系统 响应式 移动设备优先的流式栅格系统
        把一行平均分成最多12列
        大于12分会重新起一行排列
        可以设置标签占多少列
        1、row表示行
        2、col-xx-** 表示一列
            xx: 表示样式使用的屏幕尺寸
                --xs 手机
                --sm 平板
                --md 桌面显示器
                --lg 超大屏幕
            ** 表示占用12份中的几份 取值范围：1～12
        3、col-xx-offset-**:
            表示左侧有几份
        4、列支持再嵌套（再写一行，分成12份）
        5、列排序
            1、col-xx-push-* 往右推
            2、col-xx-push-* 往左拉
    3、布局样式
    4、表格
    5、表单
    6、按钮
    7、图片
    8、辅助类
        1、文本颜色
        2、背景颜色
        3、快速浮动
        4、清除浮动
        
    1. Bootstrap
		1. 图标
			1. Bootstrap内置的： https://v3.bootcss.com/components/
			    图标类只能应用在不包含任何文本内容或子元素的元素上
			2. font-awesome图标：http://www.fontawesome.com.cn/
			    设置css前缀fa和图标的具体名称。把图标放在任意的位置，被设计为行内元素，一般使用<i>标签，使语义更加精确
			    为了增加图标大小相对于它们的容器, 使用 fa-lg (33% 递增), fa-2x, fa-3x, fa-4x, 或 fa-5x classes.
                    <i class="fa fa-camera-retro fa-lg"></i> fa-lg
                    <i class="fa fa-camera-retro fa-2x"></i> fa-2x
                    <i class="fa fa-camera-retro fa-3x"></i> fa-3x
                    <i class="fa fa-camera-retro fa-4x"></i> fa-4x
                    <i class="fa fa-camera-retro fa-5x"></i> fa-5x
			3. 阿里图标：        http://iconfont.cn/
		2. 面板
		3. ...
		4. jS插件
			1. 模态框
			2. 轮播图

	2. 插件
		弹出插件SweetAlert：http://mishengqiang.com/sweetalert/
    	
	<mark></mark> 高亮显示文本
	<del></del> 展示为被删除的文本
	<s></s> 没用的文本---机器识别
	<ins></ins> 额外插入的文本使用
	<u></u> 带下划线的标签
	<small></small> 其中的文本被设置为父容器字体大小的85%；
	<strong></strong> 强调一段文本
	<em></em> 用斜体强调一段文本
	
	不能将表单组和输入框组混合使用
	不要将表单直接和输入框组混合使用，建议将输入框组嵌套到表单组中使用
	表单框组中一定要设置label标签，
	
	2、Bootstrap的使用
		
		1.编译化
		为什么前端静态文件需要编译？
		
			html/css/js/图片/mp3/mp4/ett/woff/word/zip/....
			服务器承载的压力大（访问量，请求多==》公司的服务器施加压力）
			负载均衡
		2.打包
		
		了解到：
			grant| gulp| ****webpack****
			
		
		
		模块化开发
		
			前端中后端语言 nodejs|koa “当红炸子鸡” 火  express  
			后端中         python    flask|django|Tornado
			
			一个半月以后
				npm init --yes
				npm install jquery
				
				
				
				script	同步
				commonjs  node  var $ = require('jquery');
				python  from xxx import ooo
				es6Module   import $ from 'jquery'
				
				
				$.ajax({})
				
			less sass	==>css的升级版
				less编译器网站 http://tool.oschina.net/less
				
			animate.css : https://www.awesomes.cn/repo/daneden/animate-css
				awesome:社区
				
			font-awesome:http://www.fontawesome.com.cn/examples/
			
			
			
			******博客、crm、路飞项目  一定要跟上*******
	

"""
