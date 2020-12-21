"""
Django settings for dj_site project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(pa8)u27_iyqxa9=e2pvcp=l#dvnj3bdaags75^p)ilwc68eqx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = [
    'www.ccmsy.com',
    '127.0.0.1',
]

SERVER = 'http://{}'.format(ALLOWED_HOSTS[0])
# Application definition


INSTALLED_APPS = [
    'simpleui',  # 后台管理
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


INSTALLED_APPS.extend([
    # 主要业务模块
    'blog',
    'me',
    'haystack',
])


HAYSTACK_CONNECTIONS = {
    'default': {
        # 'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine', # jieba搜索
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),  # whoosh_index 文件夹不需要自己手动创建 会自动创建
    }
}

HAYSTACK_SEARCH_RESULTS_PER_PAGE = 4

# 添加此项，当数据库改变时，会自动更新索引，非常方便
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'blog.my_middleware.MyMiddleware',
    # 'blog.my_middleware.VisitCountMiddleware',
    # 'blog.my_middleware.Online',

]

ROOT_URLCONF = 'dj_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':  [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 新增
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.i18n',

                # 以下为自定义模板上下文
                'blog.my_context_processors.site',
                'blog.my_context_processors.cats',
                'blog.my_context_processors.links',
                'blog.my_context_processors.recommend',
                'blog.my_context_processors.site_count',
                'blog.my_context_processors.live_re',

            ],
        },
    },
]

WSGI_APPLICATION = 'dj_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CACHES = {
    # 默认使用的库，session，csrf等存储
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
        }
    },
    # 专做本站访问次数记录
    "four": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/4",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 10},
        }
    },

    "online": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/3",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },

    'session':{
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },

}

# 将用户的session保持到redis里面
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# 指定名字
SESSION_CACHE_ALIAS = 'session'

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'STATIC')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# ===========>Feed<===========
SITE_ID = 7

LOGGING_PATH = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOGGING_PATH): os.mkdir(LOGGING_PATH)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        # 日志格式
        'standard': {
            'format': '[%(levelname)s][%(asctime)s] [%(filename)s] [%(module)s.%(funcName)s:%(lineno)d]-%(message)s'},
        # 简单格式
        'simple': {
            'format': '%(levelname)s %(funcName)s %(message)s'
        },
    },
    # 过滤
    'filters': {
        # 暂无过滤
    },
    # 定义具体处理日志的方式
    'handlers': {
        # 默认记录所有日志
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_PATH, 'ishare.log'),
            'maxBytes': 1024 * 1024 * 10,  # 文件大小 10M
            'backupCount': 10,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码，否则打印出来汉字乱码
        },
        # 输出错误日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_PATH, 'error.log'),
            'maxBytes': 1024 * 1024 * 10,  # 文件大小
            'backupCount': 10,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码
        },
        # 控制台输出
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        # 输出info日志
        'info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_PATH, 'info.log'),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 10,
            'formatter': 'standard',
            'encoding': 'utf-8',  # 设置默认编码
        },
    },
    # 配置用哪几种 handlers 来处理日志
    'loggers': {
        # 类型 为 django 处理所有类型的日志， 默认调用
        'django': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': False,  # 是否轮转
        },
        # log 调用时需要当作参数传入
        'log': {
            'handlers': ['error', 'info', 'console', 'default'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}


# 维护期间阻止用户登录后台产生新的数据
UPGRADING = False


# 站点信息
SITE = {
    'team': 'ccmsy.com',
    'dns': ALLOWED_HOSTS[0],
    'host': 'https://{}'.format(ALLOWED_HOSTS[0]),
    'name': '张志刚的站点',
    'me': '/me/',
    'author': "lanyu",
    'email': {
        'jubao': 'zzg58g@163.com',
        'tougao': 'zzg58g@163.com',
        'support': 'zzg58g@163.com',
        'me': 'zzg58g@163.com',
    },
    # 工信部备案号
    'icp': {
        'code': '湘ICP备20003060号-1',
        'link': 'https://beian.aliyun.com/',
    },
    # 各种搜索引擎验证码
    'search_engine_metas': {
        'baidu-site-verification': '5amdMOKaXx',
        'google-site-verification': 'C2ujkHLAjxkyD2SXrnXNeoZum0YsZcl832GvR3XBTw4',
        '360-site-verification': '8a43aac6e4ecbfb7849b61c40cdebd76',
        'shenma-site-verification': '61038a23c3906f69d8ec598c57a5988c_1556268317',
        'sogou_site_verification': '7LJQRWpzdw',
        'msvalidate.01': '725274B06FEC1DAE34DA835E37A6D5D5',
    },
    'UPGRADING': UPGRADING,
}


AUTH_USER_MODEL = 'blog.UserAccount'


# 云评论插件的账户信息
LIVE_RE = {
    'data_id': 'city',
    'data_uid': 'MTAyMC81MjAxNy8yODQ5OA==',
}


# simpleui 配置
SIMPLEUI_DEFAULT_THEME = 'admin.lte.css'

# 条状地址
SIMPLEUI_INDEX = 'http://www.127.0.0.1:8000'

# SIMPLEUI_LOGO = ‘https://avatars2.githubusercontent.com/u/13655483?s=60&v=4’  #配置Logo
