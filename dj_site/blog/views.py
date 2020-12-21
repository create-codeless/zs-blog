from django.core.paginator import Paginator
from django.db.models import F
from django.shortcuts import render,reverse,redirect
from django.views import View
# Create your views here.
from blog import models as m
from django import http
import logging
logger = logging.getLogger('log')
from django.conf import settings
from django.contrib.auth import get_user_model


class Login(View):
    def get(self,request):
        return render(request,'site/login.html')


class NewsList(View):
    """
    技术类
    _m.Category.objects.order_by('-add').filter(is_active=False, pre_cat='B')

    cat__pre_cat='B'
    """

    def get(self,request,*args,**kwargs):
        try:
            tag_id = int(request.GET.get('tag_id', 0))

        except Exception as e:
            logger.error('标签错误\n{}'.format(e))
            tag_id = 1

        try:
            page = int(request.GET.get('page', 1))
        except Exception as e:
            logger.error('页面错误\n{}'.format(e))
            page = 1

        # news_list = m.Blog.objects.values('id','title','cover','digest','mod').annotate(author=F('author__username'))

        news_list = m.Blog.objects.select_related('author').only('cover', 'title', 'digest','author__username','mod')
        news = news_list.filter(is_active=True,cat_id=tag_id, cat__is_active=False) or news_list.filter(is_active=True,cat__is_active=False,cat__pre_cat='B')

        paginator = Paginator(news, 5)
        try:
            news_info = paginator.page(page)
        except Exception as e:
            logger.info('给定的页码错误{}'.format(e))
            news_info = paginator.page(paginator.num_pages)

        news_info_list = []
        for n in news_info:
            news_info_list.append(
                n.to_put()
            )

        data = {
            'news': news_info_list,
            'total_pages': paginator.num_pages
        }
        return http.JsonResponse({"data":data,"status":0})


class Link(View):
    """
    友链相关
    """
    def get(self, request, *args, **kwargs):
        ctx = {
            'public_links': self.get_public_links(), # 公益
            'public_cnt': self.public_cnt,   # 数量
            'person_cnt': self.person_cnt,  # 个人数量
            'biz_cnt': self.biz_cnt,     # 商业链接数量
            'person_links': self.get_person_links(),  # 个人
            'biz_links': self.get_biz_links(),  # 商业
            'page': {
                'title': '友情链接 | 张志刚的博客',
                'keywords': '友情链接、公益链接、个人主页、商业广告',
                'description': '张志刚的博客，一个助力实现文学梦想，技术干货创作和分享的开放平台。',
            },
        }
        return render(request, 'site/link.html', ctx)

    def get_person_links(self):
        # 获取链接 个人主页
        return m.Link.objects.filter(is_active=True, cat=1)

    @property
    def person_cnt(self):
        return self.get_person_links().count()

    def get_public_links(self):
        # 公益链接
        return m.Link.objects.filter(is_active=True, cat=0)

    @property
    def public_cnt(self):
        # 公益数量
        return self.get_public_links().count()

    def get_biz_links(self):
        # 商业广告
        return m.Link.objects.filter(is_active=True, cat=2)

    @property
    def biz_cnt(self):
        # 商业链接数量
        return self.get_biz_links().count()

class GoTo(View):
    """
    友链或广告点击
    """

    def get(self, request, *args, **kwargs):
        return http.JsonResponse({'msg': 'OK'})


from tasks.ops import update_art_like


class Detail(View):
    """
    详情页
    """
    model = m.Blog
    def get(self,request,*args,**kwargs):
        obj = self.get_obj(kwargs.get('pk'))
        if not obj:
            raise http.Http404()
        print(type(obj.content))
        # out = "".join(obj.content.split())

        ctx = {
            'art': obj,
        }
        # 更新阅读次数
        obj.read += 1
        obj.save(update_fields=('read',))

        return render(request,'site/detail.html',ctx)

    def get_obj(self, pk):
        return self.model.objects.filter(pk=pk, is_active=True).first()

    def get_next(self, obj):
        # 获取下一篇： 按发表时间
        return self.model.objects.filter(is_active=True, add__gt=obj.add).order_by('add').first()

    def get_prev(self, obj):
        # 获取上一篇： 按发表时间
        return self.model.objects.filter(is_active=True, add__lt=obj.add).order_by('-add').first()



    def post(self, request, pk):
        """
        点赞, 异步任务来做
        """
        obj = m.Blog.objects.filter(pk=pk).first()
        response = http.JsonResponse({'code': 0, 'msg': obj.like + 1})
        # 7天内不允许重复点赞
        response.set_cookie(pk, 'true', expires=60 * 60 * 24 * 7)
        # 异步更新数据库
        # update_art_like.delay(pk)
        # update_art_like.delay(pk)
        obj.like +=1
        # obj.update(like=F("like") + 1)
        return response


    def get_art_like_status(self, pk):
        # 检验当前文章是否已经点赞过
        liked = self.request.COOKIES.get(pk, 'false')
        return liked


User = get_user_model()


class DsImg(View):
    # 获取文章打赏码

    def get(self, request, *args, **kwargs):
        art_id = self.request.GET.get('art_id', 'xxx')
        art = m.Blog.objects.filter(pk=art_id).first()
        alipay_src = ''
        wechat_src = ''
        siter = User.objects.filter(username='admin').first()

        # if not art:
            # 放上站长的二维码
        alipay_src = '{}{}'.format(settings.MEDIA_URL, siter.alipay)
        wechat_src = '{}{}'.format(settings.MEDIA_URL, siter.wechat)
        # else:
        #     # 放上作者的二维码
        #     alipay_src = '{}{}'.format(settings.MEDIA_URL, art.author.alipay or siter.alipay)
        #     wechat_src = '{}{}'.format(settings.MEDIA_URL, art.author.wechat or siter.wechat)

        response = http.JsonResponse({
            "title": "作者打赏码",
            "id": 'dsm',
            "start": 0,
            "data": [
                {
                    "alt": "支付宝打赏码",
                    "pid": 'alipay',
                    "src": alipay_src,
                    "thumb": alipay_src
                },
                {
                    "alt": "微信打赏码",
                    "pid": 'wehcat',
                    "src": wechat_src,
                    "thumb": wechat_src
                },
            ]
        })
        return response

from haystack.views import SearchView as _SearchView

# 搜索
def search(request):
    template = 'site/search.html'

    # def create_response(self):
    #     # 接受前台用户输入的查询的值
    #     kw = self.request.GET.get('q','')
    #     # 如果没有值，显示热门新闻数据
    #     if  not kw:
    #         show = True
    #         host_news = models.HotNews.objects.select_related('news').only('news__title','news__image_url','news__id').filter(is_delete=False).order_by('priority','-news__clicks')
    #         # 参数  分页
    #         paginator = Paginator(host_news,5)
    #         try:
    #             page = paginator.page(int(self.request.GET.get('page',1)))
    #         # 假如传的不是整数
    #         except PageNotAnInteger:
    #             #  默认返回第一页
    #             page = paginator.page(1)
    #         except EmptyPage:
    #             page = paginator.page(paginator.num_pages)
    #         return render(self.request, self.template, locals())
    #     else:
    #         show = False
    #         return super().create_response()

    query = request.GET.get('q')  # 获取关搜索键词
    if query:
        search_list =m.Blog.objects.filter(title__icontains=query)  # 根据标题所含关键词
    # 搜索
    # print(search_list)
        error_msg = 'No result'
        return render(request, template, {'page': search_list,'query':query})

    else:
        return redirect('/')



























