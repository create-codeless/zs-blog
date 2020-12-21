# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 14:12
# @Author  : lanyu

from django.conf import settings
from django.views.generic import View
from django.shortcuts import render, redirect, resolve_url
from django.contrib.syndication.views import Feed
from django.contrib.sitemaps import Sitemap
from blog import models
# from blog.utils import get_value_from_db
from blog.utils import get_value_from_db
from dj_site import settings


class OpenView(View):
    """
    任何方法都允许的视图：
        写这个类是为了类里面可以写多个方法来完成任务， 如果使用基于函数的视图也能实现对任意请求方式响应，但是缺点在于不能在内部定义多个方法
    """

    def get(self, request, *args, **kwargs):
        # 集成了这个类的子类必须实现自己的get方法
        raise NotImplementedError(
            "You must override the function 'get' as you extend {0}".format(self.__class__.__name__)
        )

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class Index(OpenView):
    """
    首页视图
    """
    def get(self, request, *args, **kwargs):
        # 获取首页动态内容
        data = {
            'banners': self.get_banners(),  # 轮播图
            'headlines': self.get_headlines(),  # 热点小窗
            'table': self.get_table(),  # 文艺
            # 'ad': self.get_ad(),
            # 'blog_list': self.get_blog_list(request),
            'page': {
                'title': '首页 | 张志刚的博客',
                'keywords': '文艺青年、技术干货、个人博客、原创文章、内容创作、程序员、文学创作',
                'description': '张志刚的博客，一个助力实现文学梦想，技术干货创作和分享的开放平台。',
            }
        }
        return render(request, 'site/index.html', data)

    def get_banners(self):
        queryset = models.Banner.objects.filter(
            is_active=True,
        ).order_by('-add','priority')[0:4]
        return queryset

    def get_headlines(self):
        # 边上 2个图
        num = int(get_value_from_db('BAN_SHOW_NUM', 4))
        queryset = models.Blog.objects.filter(
            is_active=True,
            is_top=False,
            cat__is_active=False
        ).order_by('-mod')[num:(num + 2)]
        return queryset

    def get_table(self):
        # 鸡汤数据响应
        d = {'cat': 1, 'arts': None}
        num = int(get_value_from_db('TABLE_SHOW_NUM', 6))
        d['arts'] = models.Blog.objects.filter(
            is_active=True,
            cat__is_active=False,
            cat__pre_cat='A'
        ).order_by('-add')[:num]
        return d

    # def get_blog_list(self, request):
    #     """
    #     按照分页参数获取对应信息
    #     """
    #     num = int(get_value_from_db('BLOG_LIST_SHOW_NUM', 10))
    #     query = models.Blog.objects.order_by('-add').filter(
    #         is_active=True,
    #         cat__is_active=True,
    #         cat__pre_cat='B'
    #     )[:num]
    #     return query




