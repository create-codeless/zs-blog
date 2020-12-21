# -*- coding: utf-8 -*-
# @Time    : 2020/11/19 20:27
# @Author  : lanyu

from django.urls import path
from . import views
app_name = 'me'

urlpatterns = [

 path('',views.My_info.as_view())

]
