from django.shortcuts import render

# Create your views here.


from io import StringIO, BytesIO
from PIL import Image
from django.conf import settings
from django import http
from blog import models as m
import os
#固定大小读取图片 TODO 测试yield方式显示图片与一次性显示图片的性能测试  作业 改变chunk_size的大小， 查看性能变化  (内存、cpu、耗时)
from django.views import View


def img_fixed(request, filename=None, width=None, height=None):
    # ext = os.path.splitext(filename)[-1][1:]
    img = Image.open(settings.BASE_DIR + "/media/%s" % (filename))
    # img = Image.open(settings.BASE_DIR + "/media/header-bg1.jpg")
    #缩放图片
    img.thumbnail((1920, 1080))
    # 保存到缓冲区并返回
    buffer = BytesIO()
    img.save(buffer, format='png')
    return http.HttpResponse(buffer.getbuffer(), content_type="image/png")

import base64
class My_info(View):

    def get(self,request):

        data = {
            'banners': self.get_banner(),  # 轮播图
            'info': self.get_my(),  # 文艺
            # 'ad': self.get_ad(),
            # 'blog_list': self.get_blog_list(request),
            'page': {
                'title': 'lanyu-张志刚-个人简历',
                'keywords': '个人简历、张志刚、web简历、Python开发、爬虫工程师、数据分析工程师',
                'description': '一个爱吃鸡的Python后端程序员',
            }
        }

        return render(request, 'me.html',data)

    def res_banner(self):
        """
        压缩图片得函数
        """
        image = ['b-1.jpg', 'b-2.jpg', 'b-3.jpg', 'b-4.jpg']
        for i in image:
            img = Image.open(settings.BASE_DIR + "/media/%s" % (i))
            width = img.width
            height = img.height
            rate = 1.0
            if width >= 2000 or height >= 2000:
                rate = 0.3
            elif width >= 1000 or height >= 1000:
                rate = 0.5
            elif width >= 500 or height >= 500:
                rate = 0.9
            width = int(width * rate)
            height = int(height * rate)
            img.thumbnail((width, height), Image.ANTIALIAS)
            # 保存到缓冲区并返回
            buffer = BytesIO()

            img.save(buffer, format='png')
            # 从内存中取出bytes类型的图片
            data = buffer.getvalue()
            # 将bytes转成base64
            data = base64.b64encode(data).decode()
            return data

    def get_banner(self):
        b = m.Banner.objects.only('image_url').filter(is_active=True,id__in=[5,6,7,8])
        return b

    def get_my(self):
        info = '   <p>我是来自湖南的Python开发工程师;人生苦短,忠于Python,始于Python</p><p>有着坚实的后端开发基础，并且一直保持对新技术的学习热情。主要开发语言为Python，熟悉django、flask、scrapy 等主流框架，熟悉mysql、nosql使用，熟悉Vue、jQuery、Bootstrap等前端常用框架；目前正在更加深入的研究编程底层原理、数据采集、数据分析和可视化技术。</p><p>爱骑车、网游、读写博客、听音乐、公益，代码不是生活的全部。</p>'

        return info

    def get_jn(self):
        pass

