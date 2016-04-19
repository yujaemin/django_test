from django.conf.urls import patterns, url
from crawler import views

urlpatterns = [
    url(r'^$', views.CrawlerMainView.as_view(), name='main'),
]
