# -*- coding: utf-8 -*-
# @Time    : 2020/11/14 23:10
# @Author  : lanyu
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
   path('link.html', views.Link.as_view()),  # 友链页

   path('goto/', views.GoTo.as_view()),  # 友链点击记录

   path('login/',views.Login.as_view()),

   path('',views.NewsList.as_view()),

   path('zf/', views.DsImg.as_view()),  # 获取打赏码地址

   # path('search/', views.search, name='search'),

   path('<pk>/',views.Detail.as_view(),name='detail'),


]

