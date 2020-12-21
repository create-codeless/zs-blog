# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 14:10
# @Author  : lanyu

import os
import datetime

from kombu import Exchange, Queue
import django
from celery.schedules import crontab
from celery import platforms

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj_site.settings")
django.setup()
platforms.C_FORCE_ROOT = True   # 允许root用户启动worker

# 记录日志
CELERYD_HIJACK_ROOT_LOGGER = True
CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_TASK_SERIALIZER = "pickle"
# 指定任务接受的序列化类型.
CELERY_ACCEPT_CONTENT = ["msgpack", "pickle", "json", "yaml", ]
# 结果序列化方法
CELERY_RESULT_SERIALIZER = "pickle"

# 结果保存
CELERY_RESULT_BACKEND = 'redis://:{}:{}/14'.format("127.0.0.1", "6379")
# Broker使用redis
BROKER_URL = 'redis://:{}:{}/15'.format("127.0.0.1", "6379")

default_exchange = Exchange('default', type='direct')
topic_exchange = Exchange('topic', type='topic')
fanout_exchange = Exchange('fanout', type='fanout')

CELERY_QUEUES = (
    Queue('default', default_exchange, routing_key='default'),
    Queue('topic', topic_exchange, routing_key='topic'),
    Queue('fanout', fanout_exchange, routing_key='fanout'),
)

CELERY_DEFAULT_QUEUE = 'default'
CELERY_DEFAULT_EXCHANGE = 'default'
CELERY_DEFAULT_ROUTING_KEY = 'default'


