# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 14:03
# @Author  : lanyu

import celery

app = celery.Celery()

app.config_from_object("tasks.settings")

app.autodiscover_tasks([
    "tasks.ops",
])

