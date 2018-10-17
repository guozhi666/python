#-*- coding:utf-8 -*-
import requests
import re

content = requests.get('http://book.douban.com/').text
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)"more-meta.*?author>(.*?)</span>.*?year>(.*?)</span>.*?</li>', re.S)
result = re.findall(pattern, content)
for results in result:
    url, name, author, date = results
    author = re.sub('\s', '', author)
    date = re.sub('\s', '', date)
    print (url, name, author, date)