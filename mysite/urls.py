#-*- coding: utf-8 -*-
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView # 뷰를 따로 안만들어도 이미 만들어진 html로 접속할 수 있음
from django.views.generic import RedirectView # 원하는 url로 리다이렉트
from mysite import views
from django.conf.urls import url, patterns

urlpatterns = [
    #url(r'^$', TemplateView.as_view(template_name='mysite/index.html'), name='home'),
    #url(r'^$', RedirectView.as_view(url='polls')),
    url(r'^admin/', admin.site.urls),
    #url(r'^polls/$', views.index, name='index'),
    #url(r'^polls/(?P<question_id>\d+)/$', views.detail, name='detail'),
    #url(r'^polls/(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    #url(r'^polls/(?P<question_id>\d+)/results/$', views.results, name='results')
    #url(r'', include('polls.urls', namespace="polls")),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^books/', include('books.urls', namespace="books")),
    url(r'^crawler/', include('crawler.urls', namespace="crawler")),
]
