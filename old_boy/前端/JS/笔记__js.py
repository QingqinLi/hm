"""

https://www.cnblogs.com/liwenzhou/p/8004649.html
https://www.cnblogs.com/liwenzhou/p/8011504.html
https://www.cnblogs.com/liwenzhou/p/8178806.html
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
    轻量级的js框架，一个js插件，相比较原生的DOM操作更简单，开发效率更高
    在页面的标签加载完之后执行 window.onload = function(){...}
    通常会把给标签绑定事件的JS代码都放在body标签的最后面

    计时器的练习

    使用：
        1、下载jQuery
            1.x 兼容ie678
            2.x
            3.x
            jquery.js jquery.min.js(压缩过的，为了加载速度更快）
        2、导入 一个页面导入一次就可以（一个页面导入一次就可以了）
        3、使用（不能在导入的script中使用）
            基本语法：
                1、jQuery
                2、$ 一般用这个
                $("").xxx()
                支持链式操作
                不能对jquery对象调用原生的属性或方法， jquery对象才能调用jquery方法，DOM对象只能调用DOM方法
                jquery对象和dom对象的相互转化：
                    jQuery --- > DOM        $("div") --- > $("div")[0]
                    DOM ---> jQuery         this --- > $(this)
                jquery对象取原生对象，索引0的 $("")[0] 可以用原生的属性方法

    查找标签：
        选择器
            基本选择器：
                1. $("#id值")
                2. $("标签名")
                3. $(".class名")
                4. $("*")

                5. $("div.c1")
                6. $("div,.c1")
            层级选择器：
                $("dic .c1")  div下面子孙中有c1样式类的标签
                $("div>.c1") div下面儿子中有c1样式类的标签
                $("label+input") 找到紧挨着label的input标签
                $("div~p") 找到div同级下面的所有的p标签
            属性选择器
                $("[s1]") 有属性
                $("[type='submit']") 属性等于
                $("[type!='submit']")  属性不等于

            基本筛选器：
                $("div:first")/$("div:last")
                $("div:eq(index)")/$("div:gt(3)")/$("div:lt(3)")
                eq是找索引等于index的那个元素 gt找大于给定索引值的元素，lt找小于给定索引值的元素
                $(div:even")/$("div:odd")
                $("div:not(.c1)")  找到没有c1样式累的div标签
                $("div:has(.c1)")  找到内部有c1样式类的div标签（是在后代标签中查找）
            表单筛选器：
                $(":text")/$(":password")
                $("input:checked")
                $(":seleced")
                $(":disabled")   表单对象属性
        筛选器：
            上一个.prev() prevALl() prevUntil()
            下一个.next() nextAll() nextUntil()
            祖先标签.parent() parents() 查找当前元素的所有父辈元素 parentsUntil() 查找当前元素的所有父类元素，直到匹配到那个元素为止
            儿子和兄弟 .children()/.siblings()
            查找.find('选择器条件）在后代中查找符合要求的
            筛选.filter('选择器条件'） 根据条件对已经找到的结果进行二次过滤
            .first()
            .last()
            .not()/.has()
            .eq()
        操作class
            addClass()
            removeClass()
            hasClass()
            toggleClass() 相反没有就添加 有就删除

        操作样式
            操作样式只直接操作css
                .css("color") 获取样式的值
                .css("color", "red") 设置样式的值
            位置
                position（）相对父元素的偏移位置
                offset（） 相对当前窗口的偏移位置
                scrollTop() 相对顶部的偏移
                scrollLeft()  相对左侧的偏移
            尺寸
                height（） 元素的高度 设置的height
                width（） 元素的宽度 设置的width
                innerHeight()  height+padding
                innerWidth()
                outerHeight()  height+padding+border
                outerWidth()
            求值
                text()
                html()
                val() 取第一个匹配元素的内容
                val(新值）
                val(["1", "2"]) 设置多选的checkbox， select的值
            属性
                attr（） 可以看到的属性等的值，设置（两个参数，{}对象可以用来设置多个属性）  --- 显示的，用于获取可以看到的属性和自定义属性
                removeAttr() 从第一个匹配的元素中删除一个属性
                prop（） checked radio...有true和false的属性用这个取值   ---隐式的， 不支持获取标签的自定义属性，可以获取返回布尔值，checkbox， radio， option
                removeProp（） 移除属性
            绑定时间的方式
                .click(function(){...})

        has--早子孙后代中找，与not不是相反的关系
        jquery变量约定-变量前加$前缀
        select和checked的选择

    属性选择器
    操作样式：
        操作class
        操作css
            $("").css("color") 获取选中标签的某个属性
            $("").css("color", red) 设置选中标签的属性值

    文档操作：
        创建标签：document.createElement("div")
        内部添加：
            前面加：
                $(A).prepend(B)  b追加到a
                $(A).prependTo(B) a追加到b
            后面加：
                $(A).append(B)
                $(A).appendTo(B)
        外部添加
            前面加
                $(A).before(B)
                $(B).insertBefore(A)
            后面加
                $(A).after(B)
                $(B).insertBefore(A)
        移除和清空
            remove（） 把选中过得标签从文档树中移除
            empty（） 把选中的标签内部的元素都移除
        替换
            $(A).replaceWith(B)
            $(B).replaceAll(A)
        clone
            注意参数true，加上true会吧标签绑定的事件也复制
    事件
        常用事件：
            click，hover, blur, focus, change, keyup
        1、jquery绑定事件的方式
            1、给标签绑定事件的方式
                onclick=函数（）
                js中，标签对象.onclick=function(){}
            2、jquery绑定事件
                $("选择器").click(function(){...})
                .on(events, [, selector--选择器（可选）], function(){}) 绑定事件
                .off(events, [, selector, ], [funcition(){}]) 移除用on绑定的事件
            3、事件委托
                原理：事件冒泡，利用副标签去捕获自标签的事件
                    1、如何阻止事件冒泡（向上传递）
                        e.stopPropagation()
                    2、阻止默认事件的执行（通常是用于阻止form表单的提交）
                        e.preventDefault()
                    3、阻止后续事件的执行
                        return false
                目的：解决未来的标签如何绑定事件
                语法：
                    $("祖先标签").on("click", "选择器", function(){...})
            dom中定义的事件，可以用on的方式来绑定， 但是hover这种的jquery中定义的事件是不能用on的方式来绑定的

    动画效果：
        // 基本
        show([s,[e],[fn]])
        hide([s,[e],[fn]])
        toggle([s],[e],[fn])
        // 滑动
        slideDown([s],[e],[fn])
        slideUp([s,[e],[fn]])
        slideToggle([s],[e],[fn])
        // 淡入淡出
        fadeIn([s],[e],[fn])
        fadeOut([s],[e],[fn])
        fadeTo([[s],o,[e],[fn]])
        fadeToggle([s,[e],[fn]])
        // 自定义（了解即可）
        animate(p,[s],[e],[fn])
    each
        1、$.each(要遍历的对象，fnnction(){})
        2、$("").each(function(){
        //this 是进入循环体的标签
        console.log(this)
        })
        3、退出本次循环
        4、退出each循环 return false
        注意: jQuery的方法返回一个jQuery对象，遍历jQuery集合中的元素 - 被称为隐式迭代的过程。当这种情况发生时，它通常不需要显式地循环的 .each()方法：
    data
        任意的jquery标签都有一个，类似全局变量，页面刷新之后就没有了，两个函数之间传递消息的时候
        .data(key, value) 存值
        .data(key) 根据key取值
        .data() 取所有的键值对
        .removeData(key) 根据key删除值
        .removeData() 删除所有的键值对
    页面载入：
        1、$(documents).ready(function(){
        js代码
        }
        2、$（funcition)(){}
        与window.onload的区别： window.onload()函数有覆盖的现象，文档加载完整之后才能调用
        jquery的这个入口函数没有覆盖现象，文档加载完整之后可以调用
    拓展
        $.extend() 对jquery拓展一个自定义方法{"函数名"：function(){}}
        $.fn.extend() 给jquery对象拓展自定义方法，固定写法

    页面的开发：
        DOM里只需要记忆document.createElement()
        主要使jquery操作



Bootstrap ：https://v3.bootcss.com/
计算机中的浮点数为什么都是不精确的
"""
