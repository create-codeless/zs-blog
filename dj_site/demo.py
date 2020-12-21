# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 19:33
# @Author  : lanyu


from aip import AipOcr,AipBodyAnalysis
from pprint import pprint

class Person(object):

    def __init__(self):
        """
         API_KEY  SECRET_KEY ---》 https://console.bce.baidu.com/iam/#/iam/accesslist
        APP_ID ====>
        """
        self.APP_ID = '20186647'
        self.API_KEY = '412a628a1025456d83fdae14a459f076'
        self.SECRET_KEY = "d263dad9a5d740f097a6e20c456111ed"

    def detection(self):
        clients = AipBodyAnalysis(self.APP_ID, self.API_KEY, self.SECRET_KEY)

        image = self.get_file_content('test.jpg')
        options = {}
        # """ 带参数调用人体检测与属性识别 """
        res = clients.bodyAttr(image, options)
        data = res['person_info'][0]['attributes']
        news = {}
        for k, v in data.items():
            news[k] = v['name']
        pprint(news)

    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

if __name__ == '__main__':
    p = Person()
    p.detection()








