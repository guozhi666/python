from bs4 import BeautifulSoup
import requests, json

if __name__ == '__main__':
    target = 'https://unsplash.com'
    headers = {'authorization':'your Client-ID'}
    req = requests.get(url = target, headers = headers, verify = False)
    htmls = json.loads(req.text)
    next_page = htmls['next_page']
    print('下一页地址：', next_page)
    for each in htmls['photos']:
        print ('图片ID:', each['id'])