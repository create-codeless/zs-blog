# -*- coding: utf-8 -*-
# @Time    : 2020/11/19 16:55
# @Author  : lanyu
from django.template.defaultfilters import stringfilter

from django import template
register = template.Library()

@register.filter
@stringfilter
def my_con(value):
    # out = "".join(str(value).split('\\xao\\n\\t'))
    # print(out)
    out = dict.fromkeys((ord(c) for c in u"\\xa0\\n\t"))
    output = value.translate(out)
    return output
    # return value.replace(value,"")


