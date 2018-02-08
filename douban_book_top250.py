#时间：2017_12_5
#作者：Jason
#功能：爬取豆瓣评分TOP250的书籍
import requests
from bs4 import BeautifulSoup
import random
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}
for i in range(10):
    pro = ['http://103.71.178.242:80', 'http://118.193.107.169:80', 'http://120.198.224.7:80']
    url = ('https://book.douban.com/top250?start=' + str(i * 25))
    res = requests.get(url, proxies={'http': random.choice(pro)}, headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    name = soup.find_all('div', class_="pl2")
    for each in name:
        title = each.a['title']
        urls = each.a['href']
        print(urls)

