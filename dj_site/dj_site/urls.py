"""dj_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from . import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from me.views import img_fixed
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='index'),  # 首页
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


# ==============文件处理路由==============
urlpatterns.extend({
    # re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # path('ueditor/', include('DjangoUeditor.urls')),
path(r'media/<str:filename>/', img_fixed),
re_path(r'^search/', include('haystack.urls')),

})


# =============博客业务路由=============
urlpatterns.extend([
    path('api/', include('blog.urls', namespace='api')),
    path('me/', include('me.urls', namespace='me')),
])



















