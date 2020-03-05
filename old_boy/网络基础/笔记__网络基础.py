"""
架构 c/s b/s
    c/s: 重逢发挥pc机的性能
    b/s优点：统一了应用的接口
两台计算机之间通信：
    网线 交换机
同一台计算机两个py文件的通信：
    socket
    import
    文件
多个计算机之间通信：
    交换机 交换机通信方式：广播，单播 组播

更多个计算机之间通信：
    交换机 路由器
交换机
请求帧
mac地址(网卡） 物理地址，全球唯一 唯一标示一台电脑
ip地址 逻辑地址，四未点分十进制
端口：操作系统为本机的应用程序随机分配的i 个端口（1-65535 0-1023不能用）
网段： 一个局域网内ip地址的范围
子网掩码： 用来计算网段的，子网掩码&ip地址
如何判断两个电脑是否处在同一网段：子网掩码&ip地址

TCP: 面向连接的，可靠的 面向字节流形式的，TCP本质上就是只允许同一时间，一个服务器和一个客户端保持连接, type = SOCK_STREAM
UDP: 无连接的 不可靠的 面向数据报形式的 传输速度快 相对不可靠 允许一个服务器和多个客户端同时通信, type = SOCK_DGARM
tcp协议为什么比upd协议更可靠：  tcp是面向连接的，而udp是面向无连接的，tcp的通信过程中有一个ACK.确认收到消息的一个标示
路由器与交换机的区别
    交换机的主要功能是组织局域网，经过交换机内部处理解析信息之后，将信息以点对点，点对多的形式发送给固定端
    路由器的主要功能：进行跨网段的数据传输， 路由选择最佳路径
    eg. 需要将多台电脑连接到一根网线，用交换机即可， 如果只有一个外网ip，但是你有好多台电脑需要上网，用路由器即可
arp协议： 通过目标ip地址获取目标mac地址的一个协议
OSI模型
    物理层 光纤 集线器 网线 传输点信号
    数据链路层 交换机 网卡 网桥    arp
    网络层 路由器 三层交换机    ip
    传输层 四层交换机 四层路由器    tcp upd
    应用层    http https ftp

socket模块
    tcp 面向连接 可靠的 面向字节流的
    udp 无连接的 不可靠 面向数据报形式
    TCP协议编码流程
        服务端：
        实例化对象
        绑定ip地址和端口号
        监听
        接收客户端的连接
        收发
        关闭

        客户端：
        实例化对象
        连接服务器
        收发
        关闭

回环地址：127.0.0.1 每个计算机都有这么一个本机地址，只能被本机识别，不会被其他机器识别

tcp协议的三次握手：
    一定是client发起请求
    a 客户端发起请求连接服务器
    b 服务器返回 ：接收到请求 并要求连接客户端
    c 客户端回复 ：可以连接
四次挥手：
    谁先发起断开连接的请求都可以
    a eg 客户端发起断开连接的请求(没有数据要发送了，询问对方是否有数据要发送）
    b 服务端回复：我接收到你的请求了
    c 我已经准备好断开连接了
    d 客户端回复: 收到信息，断开连接
ACK: 确认收到
SYN: 请求连接的标志
FIN: 请求断开的标志


UDP协议及编码：
    type = SOCK_DGRAM
    通信优势： 可以同时和多个客户端通信

粘包：
    只有TCP可能会出现

TCP和UDP的区别

Pycharm 控制台带颜色输出\033[字体颜色；北京颜色m 数据 \033[0m
socket： 一个模块 一个套接字，是一个类，是传输层和应用层之间的一个抽象层

在py代码中调用操作系统的命令（新模块 subprocess)
    r = subprocess.Popen('ls',
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)
    # subprocess.Popen(cmd,shell=True,subprocess.stdout,subprocess.stderr)
    # cmd : 代表系统命令
    # shell = True   代表这条命令是 系统命令,告诉操作系统,将cmd当成系统命令去执行
    # stdout   是执行完系统命令之后,用于保存结果的一个管道
    # stderr   是执行完系统命令之后,用于保存错误结果的一个管道
    print(r.stdout.read().decode('gbk'))
    print(r.stderr.read().decode('gbk'))
    stdout和stderr结果只能取一次

粘包：
    发送端发送数据的时候，接收段不知道如何让去接收，造成的一种数据混乱的现象，（接收放不知道消息之间的界限，不知道一次性提取多少字节的数据造成的）
    在tcp协议中，有一个合包机制（nagle算法）将多次连续发送且间隔较小的数据，进行打包成一块数据传输，
    还有一个拆包机制，在发送端，因为受到网卡的MTU限制，会将大的超过MTU限制的数据 进行拆分，拆分成多个小的数据进行传输，当传输到目标主机的操作系统层时，会重新将多个小的数据合并成原本的数据

    udp不会发生粘包，udp协议本层一次收发数据大小的限制是：65535 - ip包头（20）- udp包头（8） = 65507，在数据链路层，MTU一般限制1500， 1500-20-8 = 1472
    sendto（num） num>65507会报错，在1472～65507中数据会在数据链路层拆包，而udp本身不是一个可靠的协议，
    所以在拆包之后，草成的多个小数据包在网络传输中，如果丢失任何一个，那么此次数据传输失败，所以num<1472是比较理想的状态

tcp粘包的拆包和合包机制发生在发送端

解决粘包：
    新模块struct
    strut.pack(type, num) type: num的类型。num 一个数字， 把一个数字打包成一个四字节的bytes
    struct.unpack(type, r)解成原数字，结果是一个数组，原数字在下表为0的位置

socketServer:
    内置模块，主要是为了解决TCP洗衣中，服务器不能同时连接多个客户端的问题，是处在socket抽象层和应用层中的一层，比socket更加贴近用户

进程是资源分配的基本单位，
正常情况下 多进程之间是无法进行通信的，因为每个进程都有自己独立的内存空间
"""
# subprocess模块执行命令
import os
import socket
import subprocess

r = subprocess.Popen('pwd', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout = r.stdout.read().decode('utf-8')
stderr = r.stderr.read().decode('utf-8')
print(stdout, stderr)
