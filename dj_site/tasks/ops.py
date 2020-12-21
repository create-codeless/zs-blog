# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 14:03
# @Author  : lanyu
import logging
from django.db.models.query import F
from blog.models import Blog
from tasks import app

logger = logging.getLogger(__name__)


@app.task(name="ops.update_art_like")
def update_art_like(pk):
    """
    更新文章点赞量
    """
    Blog.objects.filter(pk=pk).update(like=F("like") + 1)
    logger.info("更新文章点赞量成功: {}".format(pk))


