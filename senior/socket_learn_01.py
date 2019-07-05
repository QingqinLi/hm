# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import socket


def learn_socket():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 可以使用套接字首发数据,sendto(content, (ip_addr(str):host(int)))
    udp_socket.sendto("hello", ("192.168.38.162", ))
    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    learn_socket()