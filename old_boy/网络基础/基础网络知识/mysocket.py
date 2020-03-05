import socket


# 不需要编码解码，自定义socket udp类
class Mysocket(socket.socket):
    def __init__(self, encoding='utf-8'):  # 执行父类中的__init__方法
        super().__init__(type=socket.SOCK_DGARM)
        self.encoding = encoding

    def my_sento(self, msg, addr):
        return self.sendto(msg.encode(self.encoding), addr)  # 调用父类中的sendto

    def my_recvfrom(self, num):
        msg_r, addr = self.recvfrom(num)  # 调用父类的revcfrom方法
        return msg_r.decode(self.encoding), addr