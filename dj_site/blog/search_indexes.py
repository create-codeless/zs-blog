# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 17:06
# @Author  : lanyu
from haystack import indexes  # 导入索引
from . import models   # 导入模型表

class BlogIndex(indexes.SearchIndex,indexes.Indexable):

    text = indexes.CharField(document=True,use_template=True)
    """
    　　document:使用文档建立索引字段
　　　　use_template:使用模板语法
    """

    def get_model(self):
        # 返回你的模型类
        return models.Blog

    def index_queryset(self, using=None):
        return self.get_model().objects.all()



