from multiprocessing import Pool
import requests
import time


def func(url):
    res = requests.get(url)
    if res.status_code == 200:
        return 'ok'


if __name__ == '__main__':
    p = Pool(5)
    l = ['https://www.baidu.com',
         'http://www.jd.com',
         'http://www.taobao.com',
         'http://www.mi.com',
         'http://www.cnblogs.com',
         'https://www.bilibili.com',
         ]
    start = time.time()
    for i in l:
        p.apply(func, args=(i,))
    print(time.time() - start)

    start = time.time()
    for i in l:
        p.apply_async(func, args=(i, ))
    p.close()
    p.join()
    print(time.time() - start)