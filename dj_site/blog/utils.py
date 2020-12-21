# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 16:48
# @Author  : lanyu

import os
import json
import datetime
import base64
from blog import models as _m
from dj_site import settings as _st

from django.core.cache import caches

def get_value_from_db(key, default):
    # 从extend数据库读取值, 不存在则返回默认值
    obj = _m.Expand.objects.filter(key=key).first()
    return obj.value if obj else default


def today_key():
    # 获取redis中存储的今日日期
    return datetime.datetime.now().strftime('%y%m%d')


class ContextUtil(object):
    """
    关于全局模板上下文的工具
    """

    @classmethod
    def origin_art_cnt(cls) -> int:
        # 获取原创文章数量
        return _m.Blog.objects.filter(source__isnull=True, is_active=True).count()

    @classmethod
    def run_days(cls) -> int:
        # 网站运行天数
        start = datetime.datetime.strptime(get_value_from_db("SITE_START", "2020-11-11"), '%Y-%m-%d')
        now = datetime.datetime.now()
        times = now - start
        return times.days

    @classmethod
    def copy_art_cnt(cls) -> int:
        # 获取原创文章数量
        return _m.Blog.objects.filter(source__isnull=False, is_active=True).count()

    @classmethod
    def visit_cnt(cls) -> int:
        # 总访问次数统计
        visit_cnt = int(get_value_from_db('VISIT_CNT', 753))
        return visit_cnt

    # @classmethod
    # def today_visit_cnt(cls) -> int:
    #     # 今日访问次数
    #     cache = caches['four']
    #     today = cache.get(today_key(), 0)
    #     return today


    @staticmethod
    def cats(pre='A'):
        # 站点除了散文之外的技术博客
        return _m.Category.objects.order_by('-add').filter(is_active=False, pre_cat=pre)

    @classmethod
    def person_links(cls):
        # 个人主页连接
        return _m.Link.objects.order_by('-add').filter(is_active=True, cat=1)

    @classmethod
    def most_read(cls):
        # 阅读次数最多的几条
        num = int(get_value_from_db('MOST_READ_NUM', 10))
        query = _m.Blog.objects.order_by('-read').filter(is_active=True)[:num]
        return query

    @classmethod
    def recommend(cls):
        # 推荐阅读
        num = int(get_value_from_db('RECOMMEND_NUM', 10))
        query = _m.Blog.objects.order_by('-add').filter(is_active=True, is_fine=True)[:num]
        return query















