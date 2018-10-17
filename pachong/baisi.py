# -*-coding：utf-8-*-
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    target = 'http://www.xiaoshuotxt.org/mingzhu/18892/'
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('div', class_='neir')
    print(texts)