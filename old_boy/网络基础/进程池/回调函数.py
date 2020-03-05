from multiprocessing import Pool
import requests
import time
import os


def func(url):
    res = requests.get(url)
    print("子进程的pid：%s, 父进程的pid：%s" % (os.getpid(), os.getppid()))
    if res.status_code == 200:
        return url


def cal_back(sta):
    url = sta
    print("回调函数的pid:%s" % os.getpid())
    with open('content.txt', 'a+') as f:
        f.write(url + "\n")


if __name__ == '__main__':
    p = Pool(5)
    l = ['https://www.baidu.com',
         'http://www.jd.com',
         'http://www.taobao.com',
         'http://www.mi.com',
         'http://www.cnblogs.com',
         'https://www.bilibili.com',
         ]
    print("主进程pid:%s" % os.getpid())
    for i in l:
        p.apply_async(func, args=(i,), callback=cal_back)
    p.close()
    p.join()