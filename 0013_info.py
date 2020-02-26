# 第 0013 题： 用 Python 写一个爬图片的程序
# 直接参考：https://github.com/jm199504/BeautifulSoup-MaoYan

import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pages = range(0,100,10)
titles,actors,mtimes,imgs,areas = list(),list(),list(),list(),list()

def crawl(page):
    url = 'http://maoyan.com/board/4?offset={}'.format(page)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0'}
    data = requests.get(url,headers=headers)
    soup = BeautifulSoup(data.text, 'lxml')
    for i in range(1,11):
        titles.append(soup.select('.board-wrapper > dd:nth-of-type({}) > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > p:nth-of-type(1)'.format(i))[0].get_text())
        # print(titles)
        actors.append(soup.select('.board-wrapper > dd:nth-of-type({}) > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > p:nth-of-type(2)'.format(i))[0].get_text().strip()[3:])
        mta = soup.select('.board-wrapper > dd:nth-of-type({}) > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > p:nth-of-type(3)'.format(i))[0].get_text()[5:]
        mtimes.append(mta.split('(')[0])
        areas.append(mta.split('(')[1][:-1] if '(' in mta else '中国大陆')
        imgs.append(re.findall('data-src="(.*?)"',str(soup.select('.board-wrapper > dd:nth-of-type({}) > a:nth-of-type(1)'.format(i))[0]))[0])
    movies = pd.DataFrame()
    movies['电影名'] = titles
    movies['主演'] = actors
    movies['上映时间'] = mtimes
    movies['地区'] = areas
    movies['海报'] = imgs
    movies.to_csv('mt.csv',index=None,encoding='utf_8_sig')


if __name__=="__main__":
    for page in pages:
        crawl(page)
    mt = pd.read_csv('mt.csv')
    mtdict = dict()
    for area in list(mt['地区']):
        mtdict[area] = 1 if area not in mtdict else mtdict[area]+1

    mtdict = dict(sorted(mtdict.items(), key = lambda kv:(kv[1], kv[0]),reverse=True))

    print(mtdict)
    plt.figure(figsize=(10, 7))

    plt.rcParams['font.sans-serif'] = ['SimHei']
    for x, y in zip(np.arange(len(list(mtdict))), mtdict.values()):
        plt.text(x, y+0.5, '%s' % y, ha='center')

    plt.bar(np.arange(len(list(mtdict))),mtdict.values())
    plt.title('TOP100-猫眼电影')
    plt.xticks(np.arange(len(list(mtdict))),list(mtdict.keys()))
    plt.show()