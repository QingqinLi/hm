"""

https://www.cnblogs.com/liwenzhou/p/8004649.html
https://www.cnblogs.com/liwenzhou/p/8011504.html
html: 文档的结构
css: 修改文档的外观样式
js： 实现页面的动态效果
历史：
    ECMAScript 一个标准 ES5/ES6
    node.js 跑在服务端的js
    脚本语言
三大部分：
    1、基础语法
    2、操作浏览器对象 BOM
    3、操作文档的标签 DOM
js导入方式：
    直接写在页面的Script标签内部
    将JS代码写在一个js文件然后通过页面上的script的src属性导入
基础语法：javascript的语句要以分号（；）为结束符
    变量名可以使用数字、字母，下划线_, $  但是不能以数字开头
    使用 变量名 声明变量,变量名区分大小写，推荐使用驼峰式命名规则， 保留字不能作为变量名
        在ES6中新增了let命令，用来声明变量 用法类似var， 但是声明的let命令只在let所在的代码块内有效。eg.for循环
        新增const来声明常量 一旦声明 值就不更更改
    1、数据类型 js拥有动态类型：
        数字（number） 不区分整形和浮点型，只有一种数字类型
            parseInt()
            parseFloat()
            NaN --not a number
        字符串 使用+来拼接字符串
            常用方法：
                .length 返回长度
                .trim() 移除空白--两边 trimleft() trimright() charAt(n) 返回第n个字符 concat 拼接 indexOf(substring, start) 子序列的位置
                    .slice(start, end)切片 toLowerCase() 小写 toUpperCAse()大写 split(delimiter, limit) 分割
                .substring(start,end) 若start>end:它们将会对换，负数或者不是数字会被0替换
                。slice(start, end)  start>stop 不会交换两者 小于0从末尾开始（同python）
            ${变量名} 在字符串中嵌入变量 用反引号扩起来

        布尔值:
            true和false都是小写
            空字符串 0 null undefined NaN 都是false

        null 一般在需要指定或清空一个变量时才回使用， name = null

        undefined 声明但未初始化时， 默认值是undefined, 函数无明确的返回值的时候返回的事undefined
        对象 js中所有的事物都是对象 字符串 数值 数组 函数 此外 就是允许自定义函数
            对象只是带有属性和方法的特殊数据类型
            获取对象的值：
            obj.xxx
            obj['xxx']
            数组（列表）
                .length
                .push(e) 尾部追加元素
                .pop() 获取尾部的元素
                .unshift(e) 头部插入元素
                .shift() 头部移除元素
                .slice(start, end) 切片
                .reverse() 反转
                .join(seq) 将数组元素拼接成字符串
                .sort() 排序 按字母顺序对元素进行排序，要使用其他标准进行排序，需要提供比较函数，返回一个值说明这两个值的相对顺序的数字
                .foreach() 将数组的每个元素传递给回调函数
                .splice() 删除元素，并向数组中添加新元素
                .map() 返回一个数组元素调用函数处理后的值的新数组
                .forEach(function(num))
                .splice()
                遍历：使用for循环根据索引迭代
            自定义对象（字典）
        typeof 变量 类型查询 是一个一元运算符
            undefined - 如果变量是 Undefined 类型的
            boolean - 如果变量是 Boolean 类型的
            number - 如果变量是 Number 类型的
            string - 如果变量是 String 类型的
object - 如果变量是一种引用类型或 Null 类型的

    2、运算符：
        强等于和弱等于的区别
            算术运算符
            赋值运算符
                && || ！
            比较运算符
                === 强等于
                ==弱等于
                ！==
                ！=
            逻辑运算符
    3、流程控制
        if else
        for
        switch case语句通常会加上break语句，否则程序会继续执行后续case中的语句
        while
    三元运算符：var c = a > b ? a : b


函数：
   关键字：function
   arguments 获取函数的全部参数
   匿名函数(嵌入别的方法中使用)：
        var sum = function(a, b){
             return a + b;
        }
    自执行函数(变量的私有化，不会污染全局）：
        (function(a, b){
            return a + b;
        })(1, 2);
    ES6中允许使用“箭头”（=>）定义函数。没有参数的话就用（）代表参数
        var f = v => v;
        // 等同于
        var f = function(v){
          return v;
        }
    函数的参数（不传， 多传，少传都不会报错）
    函数只能返回一个值（最后一个） 如果要返回多个值 只能将其放在数组或者对象中返回）
    局部变量：
        在函数内部声明的变量是局部变量，只能在函数内部访问，函数执行完毕，本地变量就会被删除
    全局变量：
        在函数外部声明的变量是全局变量，网页的所有脚本和函数都能使用它
    变量的生存周期：
        JavaScript变量的生命期从它们被声明的时间开始。
        局部变量会在函数运行以后被删除。
        全局变量会在页面关闭后被删除。
    首先在函数内部寻找变量， 找不到到外层去寻找
    词法分析的过程：
        当函数调用的前一瞬间，会先形成一个激活对象：Avtive Object（AO），并会分析以下3个方面：

        1:函数参数，如果有，则将此参数赋值给AO，且值为undefined。如果没有，则不做任何操作。
        2:函数局部变量，如果AO上有同名的值，则不做任何操作。如果没有，则将此变量赋值给AO，并且值为undefined。
        3:函数声明，如果AO上有，则会将AO上的对象覆盖。如果没有，则不做任何操作。
        函数内部无论是使用参数还是使用局部变量都到AO上找。

内置对象和方法：
    自定义对象：
        本质是键值对的集合（Hash结构） 但是只能以字符串作为键
        取值方式:.属性 [属性]
        var person=new Object();  // 创建一个person对象
        person.name="Alex";  // person对象的name属性
        person.age=18;  // person对象的age属性
        ES6的Map结构，类似与对象，也是键值对的集合，但是键的范围不限于字符串，各种类型的值都可以当键
    类：首字母大写
    var Person = function(dream){
    this.dream = dream;
    继承：
        // 父类构造函数
        var Car = function (loc) {
          this.loc = loc;
        };

        // 父类方法
        Car.prototype.move = function () {
          this.loc ++;
        };

        // 子类构造函数
        var Van = function (loc) {
          Car.call(this, loc);
        };

        // 继承父类的方法
        Van.prototype = Object.create(Car.prototype);
        // 修复 constructor
        Van.prototype.constructor = Van;
        // 扩展方法
        Van.prototype.grab = function () {
          /* ... */
        };
    Date对象：
        var d = new Date().format()
        d.toLocaleString() 转换成当地的时间
        getDate()/getDay() 获取星期/getFullYear() 获取完整年分／getMonth()0-11/getYear()/getHours()/getMinutes()
        /getSeconds()/getTime()时间戳
    JSON对象：
        和语言没有关系的数据格式
        字符串转换成对象 var obj = JSON.parse(str1) 反序列化
        对象转换成JSON var str = JSON.stringify(obj1) 序列化

    正则（RegExp)对象
        var r1 = new regExp('^1[2-9][0-9]{9}$')
        /^1[2-9][0-9]{9}$/ 简写
        坑：
            r1.test() true--相当于传了undefined
            r1.test(undefined) true 当成了字符串的undefined
            不要加空格（尤其是正则）
            全局匹配g（lastindex--记录上次查找之后的位置 test函数会从这个位置开始查找）
            i--忽略大小写
    Math对象：
        math.abs() 绝对值／floor(向下舍入）／log（x) 数的自然对数 max／min／pow／random（） 0-1之间的随机数
        round（四舍五入）／sin（）正弦／sqrt平方根
        补充：
            python 中的round ，一般使用：对浮点数进行近似取值，保留几位小数（不写默认保留到整数）
            2.7版本中 四舍六入 两边一样远的时候，会保留离0远的一遍
            3.5中 如果两边一样远，会保留到偶数的一遍
            round(2.675, 2) 两个版本的结果都应该是2.68 结果却是2.67---浮点数的精度----round（） 函数精确度不高
                math.celling()天花板除法
                正处 2.7/ 3.5// div除法
                %.2f 保留两位消暑
                对浮点数要求高用 decimal模块


前端的js没有模块化的概念：一个文档中不同的js文件，从上到下可以查找到，可以用自执行函数防止变量污染


JavaScript面向对象之继承

BOM(Browser Object Model):
    window （全局的对象--一般省略）代表浏览器窗口
        常用方法：
            window.innerHeight-浏览器窗口的内部高度
            window.innerWidth 浏览器窗口的内部宽度
            window.open() 打开新窗口
            window.close() 关闭当前窗口
        子对象：
            navigator 判定用户所使用的浏览器，包含了浏览器相关信息
            screen对象 不常用
            history 包含浏览器的对象
            location 获得当前页面的地址，并把浏览器重定向到新的页面
                location.href 获取当前访问的URL
                location.href='url' js控制页面跳转到指定url
                location.reload() 重新加载当前页面
            弹出框
                警告框alert（）
                确认框 confirm（）
                提示框 prompt（）
            计时相关 可以在一定时间间隔后指定代码，而不是在函数被调用后立即执行--计时事件
                var t = setTimeout("JS", 毫秒）
                clearTimeout(变量)
                setInterval(function, time) 隔多长时间执行一次，会不停的调用函数，知道clearInterval()被调用或者窗口被关闭，
                    setInterval（）返回的id可以用作clearInterval()方法的参数
                clearInterval（） 取消定时任务，参数必须是setinterval返回的值

DOM Document Object Model 对文档的内容进行抽象和概念化的方法
    网页被加载时候，会创建页面的文档对象模型（被构造为对象的树）
    javascript可以通过DOM创建动态的hrml，可以改变html元素,html属性,css样式,对页面中所有时间作出反应
    直接找元素：
        document.getElementById()
        document.getElementsByCLassName()
        document.getElementsByTagName()根据标签找元素

    间接找元素：
        parentElement            父节点标签元素
        children                 所有子标签
        firstElementChild        第一个子标签元素
        lastElementChild         最后一个子标签元素
        nextElementSibling       下一个兄弟标签元素
        previousElementSibling   上一个兄弟标签元素
    createElement(标签名)
    追加一个子节点（作为最后的子节点）
    somenode.appendChild(newnode)；
    把增加的节点放到某个节点的前边。
    somenode.insertBefore(newnode,某个节点);
    somenode.removeChild(要删除的节点)
    somenode.replaceChild(newnode, 某个节点);

    属性：
        divEle.setAttribute("age","18")
        divEle.getAttribute("age")
        divEle.removeAttribute("age")
        懒加载

    获取值的操作：
        语法：
        elementNode.value
        适用于以下标签：
            .input
            .select
            .textarea

    css：
        class的直接操作：
            className  获取所有样式类名(字符串)

            classList.remove(cls)  删除指定类
            classList.add(cls)  添加类
            classList.contains(cls)  存在返回true，否则返回false
            classList.toggle(cls)  存在就删除，否则添加

            obj.style.backgroundColor="red"

        JS操作CSS属性的规律：

            1.对于没有中横线的CSS属性一般直接使用style.属性名即可。如：

            obj.style.margin
            obj.style.width
            obj.style.left
            obj.style.position
            2.对含有中横线的CSS属性，将中横线后面的第一个字母换成大写即可。如：

            obj.style.marginTop
            obj.style.borderLeftWidth
            obj.style.zIndex
            obj.style.fontFamily
    事件：
        常用：
            onclick        当用户点击某个对象时调用的事件句柄。
            ondblclick     当用户双击某个对象时调用的事件句柄。

            onfocus        元素获得焦点。               // 练习：输入框
            onblur         元素失去焦点。               应用场景：用于表单验证,用户离开某个输入框时,代表已经输入完了,我们可以对它进行验证.
            onchange       域的内容被改变。             应用场景：通常用于表单元素,当元素内容被改变时触发.（select联动）

            onkeydown      某个键盘按键被按下。          应用场景: 当用户在最后一个输入框按下回车按键时,表单提交.
            onkeypress     某个键盘按键被按下并松开。
            onkeyup        某个键盘按键被松开。
            onload         一张页面或一幅图像完成加载。
            onmousedown    鼠标按钮被按下。
            onmousemove    鼠标被移动。
            onmouseout     鼠标从某元素移开。
            onmouseover    鼠标移到某元素之上。

            onselect      在文本框中的文本被选中时发生。
            onsubmit      确认按钮被点击，使用的对象是form。

        绑定事件的方式：
            this指的是调用函数的标签本身
            方式一：
                <div id="d1" onclick="changeColor(this);">点我</div>
                <script>
                  function changeColor(ths) {
                    ths.style.backgroundColor="green";
                  }
                </script>
                注意：

                this是实参，表示触发事件的当前元素。

                函数定义过程中的ths为形参。

                方式二：

                <div id="d2">点我</div>
                <script>
                  var divEle2 = document.getElementById("d2");
                  divEle2.onclick=function () {
                    this.innerText="呵呵";
                  }
                </script>


    innerText 不能识别标签，按照文本来显示
    innerHTML 能正常识别标签

计时器的练习

jquery
    库
    轻量级的js框架
    使用：
        1、下载jQuery
        2、导入 一个页面导入一次就可以
        3、使用（不能在导入的script中使用）
            基本语法：
                jQuery
                $ 一般用这个
                $("").xxx()
                不能对jquery对象调用原生的属性或方法
                jquery对象取原生对象，索引0的 $("")[0] 可以用原生的属性方法

    查找标签：
        选择器
            id选择器 #id
            标签选择器 直接使用

        筛选器
        has--早子孙后代中找
        jquery变量约定-变量前加$前缀
        select和checked的选择


计算机中的浮点数为什么都是不精确的
"""





















