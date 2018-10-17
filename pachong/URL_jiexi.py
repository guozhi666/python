#-*- coding:utf-8 -*-
import requests

# response = requests.get('http://httpbin.org/get?name=germey&age=22')
# print (response.text)
#
# data = {
#     'name':'germey',
#     'age': 22
# }
# responses = requests.get('http://httpbin.org/get', params=data)
# print (responses.text)


# 爬取图片并保存到本地
# response = requests.get('https://github.com/favicon.ico')
# with open('favicon.ico', 'wb')as f:
#     f.write(response.content)
#     f.close()


# 添加headers
# headers = {
#     user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
# }
# response = requests.get('http://www.zhihu.com/explore', header = headers)
# print (response.text)



response = requests.get('https://www.12306.cn', varify = False)
print (response.status_code)