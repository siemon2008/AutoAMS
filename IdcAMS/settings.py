# -*- coding: utf-8 -*-
"""
Django settings for IdcAMS project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kct*4ijy6(#5ge+pbq#zo54_$*4(6((pqzmppce@cc0adab_xl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# 自定义用户管理
AUTH_USER_MODEL = 'myauth.User'

SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_AGE = 60*60 # 配置会话超时时间为1小时
SESSION_EXPIRE_AT_BROWSER_CLOSE = True # 配置关闭浏览器会话消失

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'news',
    'DjangoUeditor',
    'myauth',
    'common',
    'idcroom',
    'server',
    'backup',
    'network',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'IdcAMS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

            ],
        },
    },
]

WSGI_APPLICATION = 'IdcAMS.wsgi.application'



# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 公共的 static 文件，比如 jquery.js 可以放这里，这里面的文件夹不能包含 STATIC_ROOT
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "common_static"),
    ('skin',os.path.join(STATIC_ROOT,'skin').replace('\\','/') ), # 配置后台样式文件夹路径，否则找不到
)

# upload folder
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 权限管理(两个app的view函数不能重复)
PERMISSIONS = {
    # myauth app
    "group_add":"用户分组添加",
    "group_update":"用户分组更新",
    "group_del":"用户分组删除",
    "group_list":"用户分组列表",

    "user_add":"用户添加",
    "user_update":"用户更新",
    "user_del":"用户删除",
    "user_list":"用户列表",

    # news app
    "column_add":"文章分类添加",
    "column_update":"文章分类更新",
    "column_del":"文章分类删除",
    "column_list":"文章分类列表",

    "article_add":"文章添加",
    "article_update":"文章更新",
    "article_del":"文章删除",
    "article_list":"文章列表",
    "article_show":"文章查看",

    # idcroom app
    "idcroom_add":"机房添加",
    "idcroom_update":"机房更新",
    "idcroom_del":"机房删除",
    "idcroom_list":"机房列表",

    # server app
    "server_list":"服务器列表",
    "server_update":"服务器属性更新",
    "server_updatemore":"服务器属性批量更新",

    # backup app
    "serverbk_add":"服务器备件添加",
    "serverbk_addmore":"服务器备件批量添加",
    "serverbk_update":"服务器备件更新",
    "serverbk_del":"服务器备件删除",
    "serverbk_list":"服务器备件列表",

    "diskbk_add":"硬盘备件添加",
    "diskbk_update":"硬盘备件更新",
    "diskbk_addmore":"硬盘备件批量添加",
    "diskbk_del":"硬盘备件删除",
    "diskbk_list":"硬盘备件列表",

    "memorybk_add":"内存备件添加",
    "memorybk_update":"内存备件更新",
    "memorybk_addmore":"内存备件批量添加",
    "memorybk_del":"内存备件删除",
    "memorybk_list":"内存备件列表",

    # network app
    "switch_add":"交换机添加",
    "switch_update":"交换机更新",
    "switch_del":"交换机删除",
    "switch_list":"交换机列表",

}
