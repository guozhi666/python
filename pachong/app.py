# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    server = 'http://www.xiaoshuotxt.org/mingzhu/18892/'
    target = 'http://www.xiaoshuotxt.org/mingzhu/18892/1034829.html'
    req = requests.get(url = target)
    html = req.text
    bf = BeautifulSoup(html)
    div = bf.find_all('div', class_ = 'zlb')
    a_bf = BeautifulSoup(str(div[0]))
    a = a_bf.find_all('a')
    for each in a:
        print(each.string, server + each.get('href'))
    # print (div[0])
    # print (html)