from html.parser import HTMLParser

import requests,random
from lxml import etree
import threading
import requests
# from requests.adapters import HTTPAdapter
from pyquery import PyQuery as pq
import pymysql
conn = pymysql.connect(host='101.200.62.28',user='lanyu',password='xiaozahng',database='db_news',port=3306)
cursor = conn.cursor()

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    'Cookie': 'Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f=1606132806,1606197288,1606468864; Hm_lpvt_0362c7a08a9a04ccf3a8463c590e1e2f=1606469028',
    'Referer': 'https://www.yuanrenxue.com/crawler',
    'Host': 'www.yuanrenxue.com',
}

def news(num):
    ses = requests.session()
    handleNone = lambda x: x if x else ' '
    # ses.mount('https://', DESAdapter())
    import time
    time.sleep(2)
    res =ses.get('https://www.yuanrenxue.com/crawler/page/{}'.format(num),headers=headers,verify=False)
    s = etree.HTML(res.text)
    items = s.xpath('//ul[@id="postlist"]/li')
    image = 'https://www.lujianxin.com//media/blog/cover/UTF-8.png', 'https://www.lujianxin.com//media/blog/cover/prometheus.png', 'https://www.lujianxin.com//media/blog/cover/prometheus.png', 'https://www.lujianxin.com//media/blog/cover/harbor.jpeg', 'https://www.lujianxin.com//media/blog/cover/CPU-cover.png', 'https://www.lujianxin.com//media/blog/cover/python-schema.png', 'https://www.lujianxin.com//media/blog/cover/cloud-cover.jpg', 'https://www.lujianxin.com//media/blog/cover/internet-cover.jpg', 'https://www.lujianxin.com//media/lujianxin.com.png', 'https://www.lujianxin.com//media/blog/cover/linux-cover.jpg'
    num = 50
    for i in items:
        title = handleNone(''.join(i.xpath('.//h2[@class="info-tit"]//text()'))).strip()
        zy = handleNone(''.join(i.xpath('.//div[@class="info-desc"]/text()'))).strip()
        # image = i.xpath('./span[1]/a/img/@src')[0]
        link = i.xpath('.//a[@class="link"]/@href')[0]
        time.sleep(1)
        res = ses.get(link,headers=headers,verify=False)
        res1 = pq(res.text)
        tag = res1('.single-content')
        content = tag.children('p')
        text = ''.join(str(content).split())

        # 此处位打包sql文件 导入
        """
         res2 = (num, title,random.choices(image)[0], text, 'www.ccmsy.com', 1, 0, 99, 99, "2020-11-20 19:43:47.320327","2020-11-20 19:43:47.320327", 1, 1,2,1,zy)
         f = open('../dj_site/wx2.sql', 'a+', encoding='utf-8')
         f.write('INSERT INTO `blog` VALUES ' + str(res2) + ';' + '\n')
        """
        sql = """ INSERT INTO `blog` VALUE (%s,%s,%s,%s,'www.ccmsy.com',1,0,99,99,'2020-11-20 19:43:47.320327','2020-11-20 19:43:47.320327',1,1,2,1,%s) """
        cursor.execute(sql, (num, title,random.choices(image)[0],text,zy))
        conn.commit()
        print(num)
        num += 1

if __name__ == '__main__':
    # h = []
    for i in range(4,6):
        news(i)
    #     t = threading.Thread(target=news,args=(i,))
    #     t.start()
    #     h.append(t)
    # for k in h:
    #     k.join()
