# !/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
project:dj33
author:lanyu 2020/6/5
"""
import pytz
from django import template
from datetime import datetime
register = template.Library()
@register.filter()

def time_filters(time):
    """
    如果时间相差 60秒内 展示 刚刚
    如果时间差 3600 秒 展示多少分钟
    如果时间差 60*60 < current > 60*60*24 展示 XX 小时前
    :return:
    """
    if isinstance(time,datetime):
        now = datetime.now()  # 不含时区
        now = now.replace(tzinfo=pytz.timezone('UTC'))
        timestamp = (now-time).total_seconds()
        print('时间戳%s'%timestamp)
        if timestamp < 60:
            return '刚刚'

        elif timestamp>=60 and timestamp<60*60:
            minut = int(timestamp //60)  # 300 5 299 4
            return '{}分钟前'.format(minut)

        elif timestamp>=60*60 and timestamp<60*60*24:
            hours = int(timestamp //(60*60))  # 300 5 299 4
            return '{}小时前'.format(hours)

        elif timestamp>=60*60*24 and timestamp<60*60*24*30:
            days = int(timestamp //(60*60*24))  # 300 5 299 4
            return '{}天前'.format(days)

        elif timestamp>=60*60*24*30 and timestamp<60*60*24*7*52:
            month = int(timestamp //(60*60*24*30))  # 300 5 299 4
            return '{}月前'.format(month)

        elif timestamp>=60*60*24*7*52 and timestamp<60*60*24*7*52*3:
            years = int(timestamp //(60*60*24*7*52))  # 300 5 299 4
            return '{}年前'.format(years)

        elif timestamp> 60*60*24*7*52*3:
            return '漫漫长夜有你陪着'

        else:
            return time.strftime('%Y-%m-%d %H:%M')

    else:
        return time

