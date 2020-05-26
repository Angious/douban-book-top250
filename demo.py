# -*- coding: utf-8 -*-
# @Author : Angious
# @Github : https://github.com/Angious
# @FileName: demo.py
# @Software: PyCharm
# @Time : 2020/5/25 17:45

import requests
from lxml import etree
import re
import random
import json


def GetHtmlData(rdm):
    # rdm = random.randint(0, 225)  # 随机一个开始页面，取25个数据
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }
    url = 'https://book.douban.com/top250?start={}'.format(rdm)
    resp = requests.get(url=url, headers=headers, timeout=10)
    # print("响应状态码:", resp.status_code)
    if 200 != resp.status_code:
        return 404
    html = etree.HTML(resp.text)
    return html


def GetInfo(rdm):
    html = GetHtmlData(rdm)
    if html == 404:
        return 404
    bookname = html.xpath('//div[@class="pl2"]/a/@title')               #书名
    rating_nums = html.xpath('//span[@class="rating_nums"]/text()')     #评分
    rating_people_ = html.xpath('//span[@class="pl"]/text()')           #评价人数(未格式化)
    rating_people = []                                                  #评价人数(格式化)
    for i in rating_people_:
        e = re.findall('\d+',i)
        rating_people.append(e)
    imgurl = html.xpath('//a[@class="nbg"]/img/@src')                   #封面链接
    info = html.xpath('//p[@class="pl"]/text()')                        #出版信息集
    author = []                                                         #作者
    translater = []                                                     #翻译（外文作品有此属性）
    publisher = []                                                      #出版社
    date = []                                                           #发行日期
    price = []                                                          #价格
    for i in info:
        data = i.split('/')
        author.append(data[0])
        translater.append(data[1] if len(data) == 5 else 'none')
        publisher.append(data[-3])
        date.append(data[-2])
        price.append(data[-1])

    '''
    ---参数列表---
    bookname                                                #书名
    rating_nums                                             #评分
    rating_people                                           #评价人数(格式化)
    imgurl                                                  #封面链接
    author                                                  #作者
    translater                                              #翻译（外文作品有此属性）
    publisher                                               #出版社
    date                                                    #发行日期
    price                                                   #价格
    '''

    dic = {'bookname':0,'imgurl':0,'author':0,'translater':0,'publisher':0,'rating_nums':0,'date':0,'price':0,'rating_people':0}
    dict_json = {i: 0 for i in range(0, 24)}
    for i in range(0,24):
        dic['bookname'] = bookname[i]
        dic['imgurl'] = imgurl[i]
        dic['author'] = author[i]
        dic['translater'] = translater[i]
        dic['publisher'] = publisher[i]
        dic['rating_nums'] = rating_nums[i]
        dic['date'] = date[i]
        dic['price'] = price[i]
        dic['rating_people'] = rating_people[i]
       # print(dic)
        dict_json[i] = str(dic)

    # print(dict_json)
    jsn = json.dumps(dict_json, ensure_ascii=False)
    # print(jsn)
    return jsn


if __name__ == '__main__':
    json_data = GetInfo()
    print(json_data)




