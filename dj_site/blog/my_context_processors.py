# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 16:45
# @Author  : lanyu
"""
    0. 自定义全局上下文
"""

from dj_site import settings
from blog.utils import ContextUtil as ctx


def site(request):
    # 关于站点的静态信息
    return {'SITE': settings.SITE}

def cats(request):
    # 头部数据分类
    return {
        'A_CATS': ctx.cats('A'),
        'a_cat': '文学创作',
        'B_CATS': ctx.cats('B'),
        'b_cat': '技术干货',
    }


def links(request):
    # 个人网站友链信息
    return {"PERSON_LINKS": ctx.person_links()}

def recommend(request):
    # 推荐阅读
    return {'RECOMMEND': ctx.recommend()}


def site_count(request):
    # 关于站点的统计信息
    return {'SITE_CNT': {
        'run': ctx.run_days(),  # 运行天数
        'origin': ctx.origin_art_cnt(),  # 原创文章数
        'copy': ctx.copy_art_cnt(),  # 转载文章,
        'visit': ctx.visit_cnt(),  # 总访问数
        'today_visit': 1024,  # 今日访问
    }}

def live_re(request):
    # 来必力评论插件
    return {"LIVE_RE": settings.LIVE_RE}


