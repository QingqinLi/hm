"""
博客 https://www.cnblogs.com/liwenzhou/p/7988087.html

浏览器发请求 --> HTTP协议 --> 服务端接收请求 --> 服务端返回响应 --> 服务端把HTML文件内容发给浏览器 --> 浏览器渲染页面

HTML:超文本标记语言，不是一种编程语言，使用标签来描述网页，本质是可识别的规则，网页文件的拓展名.html .htm

标签中重要的属性：
    id：定义标签的唯一id，html文档树中唯一
    class: 为html定义一个或多个类型（classname）（css样式类名）
    style：规定元素的行内样式（css样式）

<!-- 注释的内容 -->
<!DOCTYPE> 不是html标签，要卸载html文档的第一行，指示web浏览器关于页面使用哪个html版本进行编写的指令
html标签的结构：
    head：给浏览器看的内容
        title：标题
        style：css样式
        link：css文件
        script：JS
        meta：提供有关页面的元信息，针对搜索引擎和更新频度的面熟和关键词，提供的信息用户不可见
            <meta charset="UTF-8">
            <meta http-equiv="refresh" content="2;URL=https://www.oldboyedu.com">
                http-equi： 相当于http的文件头作用，可以向浏览器传回一些有用的信息，以帮助正确的显示网页内容， content其实就是各个参数的变量值
            <meta name="keywords", content = "balabala">
                name 主要用于描述网页，content的内容便于搜索引擎查找和分类信息
        link: 引入外部样式表文件
    body:给用户看的内容

html标签的用法：
    <head 属性=值1 属性2=值2></head>
    <body></body>
    <meta>

<img alt:图片未家在出来的时候提示 title:鼠标滑上去的时候展示的 > </img>
<a target:> </a>
多个空格，浏览器回解析成一个空格展示
div 没有样式
span 没有样式
<ul type:类型> <li></ul>   无序
<ol></ol>  有序
href属性指定目标网页地址。该地址可以有几种类型：
    绝对URL - 指向另一个站点（比如 href="http://www.jd.com）
    相对URL - 指当前站点中确切的路径（href="index.htm"）
    锚URL - 指向页面中的锚（href="#top"）

<img src="图片的路径" alt="图片未加载成功时的提示" title="鼠标悬浮时提示信息" width="宽" height="高(宽高两个属性只用一个会自动等比缩放)">
<table border:边框> </table>:<thead></thead><tbody><tr><th></th></tr></tbody>
属性：
    id: 唯一标志
    # id: 跳转到页面内的位置

body中的常用标签：
    常用标签：
        独占一行的标签：块级标签
            h1-h6
            p
            div
            hr 水平线
            li
            tr
        连在一起的标签：行内标签（内联标签）:
            a
            span
            img
            b 加粗/i斜体/u下划线/s删除
    嵌套标签：
        标签可以嵌套标签
        规则：
            尽量不要用内联标签嵌套块级标签
            p标签不能嵌套p标签
            p标签不能嵌套div标签

    获取用户输入的标签：
        form--容器
            属性：
                action
                method
                enctype
            提交数据注意事项：
                form标签必须把获取用户输入的标签包起来
                form标签必须有action属性，method属性（默认是get）
                form标签必须有一个submit提交数据
                form标签中的获取用户输入的标签必须有name属性（否则后台接收不到数据）

        input标签
            text, password, email, date, checkbox, radio
            button --普通按钮，通常用js给他绑定事件
            submit 提交按钮，默认将form中的数据提交
            reset 重置按钮,将当前form的输入框都清空
            enctype --> 当form表单中有文件类型的数据需要上传时multipart/form-data
            placeholder: 设置提示语
            value属性用来设置输入框的默认值
            name属性 指定form表单提交数据时的key，用户填写的是value



        select：
            multiple=multiple 简写为multiple
            内部包含option 设置value属性
            通过selected属性设置默认选中
        textarea：
            cols 列数
            rows 行数
            name 属性

        label
            多用于和输入框搭配使用
            绑定方式
                label包输入标签
                for=id来绑定



特殊符号：
    小于号：&lt;
    大于号：&gt;
    空格：&nbsp;
    版权：&copy;
    注册商标：&reg;
    &：&amp;
    ¥：&yen;

特殊符号都是&开头';'结束


"""