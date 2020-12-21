# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 21:34
# @Author  : lanyu

import requests
from lxml import etree
from pyquery import PyQuery as pq

res =requests.get('https://www.lujianxin.com/')
s = etree.HTML(res.text)
items = s.xpath('//div[@class="zhuanti whitebg"]/ul/li')

linkurl = list()
num = 1
for i in items:
    print(num)
    link = 'https://www.lujianxin.com/' + '' .join(i.xpath('./i/a/@href')[0])
    title = i.xpath('./b/text()')[0]
    image = 'https://www.lujianxin.com/' + i.xpath('.//img/@src')[0]
    zy = i.xpath('./span/text()')[0]
    res = requests.get(link)
    res1 = pq(res.text)
    tag = res1('.con_text')
    content = tag.children('p')
    # f = open('data.sql', 'a+', encoding='utf-8')
    # f.write(str(res2)+ '\n')
    text = ''.join(str(content).split())
    # res2 = (num, title, 1, 2, image, 1, text, 'www.ccmsy.com', 0, 0, 99, 99, "2020-11-20 19:43:47","2020-11-20 19:43:47.320327", 1, zy)
    res2 = (num, title,image, text, 'www.ccmsy.com', 0, 0, 99, 99, "2020-11-20 19:43:47","2020-11-20 19:43:47.320327", 1, 1,1,1,zy)
    f = open('../dj_site/wx.sql', 'a+', encoding='utf-8')
    f.write(
        'INSERT INTO `blog` VALUES ' + str(
            res2) + ';' + '\n')
    print(num)
    num += 1
