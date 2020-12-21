# # -*- coding: utf-8 -*-
# # @Time    : 2020/11/17 21:34
# # @Author  : lanyu
import requests
# from lxml import etree
# from pyquery import PyQuery as pq
#
# res =requests.get('https://www.lujianxin.com/')
# s = etree.HTML(res.text)
# items = s.xpath('//div[@class="whitebg bloglist"]/ul/li')
# # s1=  []
# # for i in items:
# #     s = 'https://www.lujianxin.com/'+ i
# #     s1.append(s)
# # print(s1)
#
# linkurl = list()
# num = 18
# for i in items:
#     title = i.xpath('./h3[@class="blogtitle"]//text()')[0]
#     zy = i.xpath('./p[@class="blogtext"]/text()')[0]
#     time = i.xpath('./p[@class="bloginfo"]/span[2]/text()')[0]
#     image = i.xpath('./span[1]/a/img/@src')[0]
#     link = 'https://www.lujianxin.com/' + i.xpath('./span[1]/a/@href')[0]
#     res = requests.get(link)
#     res1 = pq(res.text)
#     tag = res1('.con_text')
#     content = tag.children('p')
#     print((title,zy,time,image,content))
#     text = ''.join(str(content).split())
#     res2 = (num, title, 1, 2, image, 1, text, 'www.ccmsy.com', 0, 0, 99, 99, "2020-11-20 19:43:47",
#             "2020-11-20 19:43:47.320327", 1, zy)
#     f = open('../dj_site/js_data.sql', 'a+', encoding='utf-8')
#     f.write(
#         'INSERT INTO blog (id,title,author_id,cat_id,cover,music_id,content,source,is_fine,is_top,"read","like","add","mod",is_active,digest) VALUES ' + str(
#             res2) + ';' + '\n')
#     num+=1

import ssl
context = ssl._create_unverified_context()

print(requests.get('https://www.baidu.com',verify='/path/to/certfile'))

