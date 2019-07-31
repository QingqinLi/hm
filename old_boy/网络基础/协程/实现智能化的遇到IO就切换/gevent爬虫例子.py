from gevent import monkey
monkey.patch_all()
import gevent
import time
import requests


def get_result(url):
    res = requests.get(url)
    print(url, res.status_code, len(res.content))


url_l = ['http://www.baidu.com',
         'https://www.jd.com',
         'http://www.taobao.com',
         'http://www.qq.com',
         'http://www.mi.com',
         'http://www.cnblogs.com']


def sync_func(url_l):
    for url in url_l:
        get_result(url)


def async_func(url_l):
    l = []
    for url in url_l:
        g = gevent.spawn(get_result, url)
        l.append(g)
    gevent.joinall(l)


start = time.time()
sync_func(url_l)
print('sync:',time.time() - start)

start = time.time()
async_func(url_l)
print('async:',time.time() - start)