from bs4 import BeautifulSoup
from multiprocessing import Process
import requests
import time
import json
import re

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko)\
     Chrome/75.0.3770.142 Safari/537.36'
}


def get_page():
    # url = 'http://yuanxiao.mpacc.cc/index.php?m=content&c=request&a=public_ajax_lists&area=2&mpaccxmtype=&schoolcharacter=1&page=1'
    url = 'http://www.kuakao.com/lk/fxzd/'
    page = requests.get(url, headers=headers)

    school_list = []
    if page.status_code == 200:
        school = page.content.decode('utf-8')
        # print(school)
        soup = BeautifulSoup(school, 'html.parser')
        # res = soup.find_all('h4', class_='listModeTit')
        # for i in res:
        #     ret = re.compile('<h4 class="listModeTit">(?P<content>.*)</h4>')
        #     s = ret.search(str(i))
        #     school_list.append(s.group('content'))
        # # for i in school:
        # #     if not i == 'pages':
        # #         school_list.append(school[i]['title'])
        res = soup.find_all('div', class_='listRight')

        # print(type(res), res[0])
        for result in res:
            title = str(result.find('h4', class_='listModeTit'))
            title = re.search('<h4 class="listModeTit">(?P<title>.*)</h4>', title).group("title")
            link = result.find('a', class_='clearfix').get('href')
            school_list.append([title, link])

    with open('kaoyan.txt', 'a+') as f:
        for school in school_list:
            f.write(str(school)+'\n')


if __name__ == '__main__':
    get_page()