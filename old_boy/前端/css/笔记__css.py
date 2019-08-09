"""
博客：https://www.cnblogs.com/liwenzhou/p/7999532.html

css语法：
    选择器{属性1：值1；属性2：值2}
css导入方式：
    1、直接将样式写在标签内部的style属性中 不推荐大规模使用
    2、在head标签中写style标签
    3、将样式单独写在css文件中，通过link标签的href属性导入（在项目中一般使用这种方式）
css选择器（importent jQuery中的选择器类似）：
    1、基本选择器
        ID选择器
        类选择器   类名不要以数字开头（有的浏览器不认）class属性有多个，要用空格隔开
        标签选择器   大规模使用
        通用选择器   *
    2、组合选择器
        div p 后代选择器
        div>p 儿子选择器
        div+p 毗邻选择器（紧挨着后边的）
        div~p 弟弟选择器 （所有的后边的）
    3、属性选择器
        div[s14]    找到有s14这个属性的div标签
        input[type='email'] 找到type是email的input标签（带有属性和值）
    4、分组和嵌套
        div, p {} 多个元素的样式相同的时候，可以通过在多个选择器之间使用都好分割的分组选择器来统一设置元素样式
        div.c1 {}
    5、伪类和伪元素
        伪类：
            :hover  鼠标移动到标签上应用的样式
            :focus  input标签获取焦点时应用的样式
            link--未访问的连接
            visited--已访问的连接
            active--选定的链接
        伪元素：
            p:before {   在p标签内部的最前面追加一个内容
                content: "*"
                color: red
                }
            p:after {   在p标签内部的最后面追加一个内容
                content: "";
                clear:both;
                display:block;
                }
            first-letter 首字母设置特殊样式
            before和after多用于清除浮动
css选择器的优先级：
    1、选择器相同的情况下：
        下面的优先级高，会覆盖
    2、选择器不同的情况下 根据权重计算
        内联(1000) > ID选择器（100）> 类选择器（10）> 元素选择器（1）>继承的（0）
    3、不讲道理的
        ！important(一般不使用）
css的属性：
    1、高和宽
        只有块儿级标签才能设置宽，内联标签的宽度又内容决定
    字体属性
        字体类别 font-family 又多个值（不支持第一个，尝试下一个... 回退）
        字体大小 font-size inherit 表示继承父元素的字体大小值
        字体粗细 font-weight normal bold bolder lighter 100-900 inherit(继承父类）
        字体颜色 color
            英文的颜色 red
            16进制的颜色代码 #FF0000
            RGB rgb(255, 0,0)
            rgba(255, 0, 0, 0.4)
        文字装饰效果
            水平居中：
                text-align:center
            单行文本的垂直居中：
                line-height=父标签的高度
            文本装饰器：
                text-decoration: none/under-line/over-line（上边）/line-through/inherit
        文字对齐 text-align: left right center justify(两端对齐）
        文字缩进 text-indent: px
    背景
        background
        background_color
        background_img: url()
        repeat. repeat-x, repeat-y, no-repeat

    不能被继承的属性：border, margin, padding, background
盒子模型：
    内容-padding-border-margin（上右下左 顺时针）
浮动：
    float：left/right
    浮动的副作用：浮动框不在文档的普通流中 clear
    clear:只会对自身起作用，而不会影响其他元素
    浮动元素会生成一个块级框 而不论它本省是什么元素
    清除浮动的方式:
        固定高度
        伪元素清除法
        overflow：hidden

定位：
    相对定位：相对于自己原来在的位置做定位 relative 元素还占有原来的位置 主要用法：方便绝对定位元素找到参照物
    绝对定位：相对自己已经定位过的祖先标签 absolute 不会占据原来的位置
    固定定位：相对于屏幕做定位 fixed 出现滑动条位置不会变

溢出：
    overflow：hidden/scroll/auto／visible(默认值 内容不会被修建会呈现在元素框之外）
边框：
    border:1px solid red;
    border-radius: 50% 实现圆角边框的效果
    dotted：点状虚线边框
    dashed：矩形虚线边框
    solid：实线边框
display:
    block 默认占满页面宽度，如果指定了宽度，用margin填充剩下的部分
    inline 按行内元素显示，
    inline-block： 同时具有行内元素和块级元素的特点
    none：元素存在，不会占用空间（占用的空间也会从页面布局中消失）但是在浏览器中不现实，一般与JS同时使用
        visibility:hidden 可以隐藏某个元素，但是隐藏的元素和未隐藏之前一样需要占用空间，会影响布局

z-index: 层叠顺序，数值大的压住数值小的，只有定位了的元素，才有z-index,浮动元素不能使用z-index,值没有单位， 从父
opacity: 定义透明效果。0-1 0是完全透明 1是完全不透明；


： 冒号表示状态
一行展示又有固定宽度
隐藏属性之后 不占页面的位置
没有设置高度 会使用文本的高度
内填充：内容和边框（padding）的距离
margin：外边距 标签和标签之间的距离
两个边距（上变距／下变距 --- 取最大的）
顺时针：上右下左
浮动：
    浮动的副作用：相当于这个元素从文档中拿出来了
    解决浮动的副作用：
        设置父容器的高度
        一个空的div clear属性
        清除浮动的样式类：

溢出：框太小，内容太多

定位：大的布局不变
    相对定位：

    绝对定位：

    固定定位：

    绝对定位和固定定位在文档中已经没有它的位置了（可以被其他元素占用位置）， 相对定位的位置还在





"""
