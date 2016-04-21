from django.conf.urls import patterns, url
from crawler import views
from mysite import settings
urlpatterns = [
    url(r'^$', views.CrawlerMainView.as_view(), name='main'),
    url(r'^new_crawl/$', views.NewCrawlView.as_view(), name='new_crawl'),
    url(r'^ecommerce_list/$', views.CrawlerListView.as_view(), name='ecommerce_list'),
    url(r'^ecommerce_review/$', views.CrawlerReviewView.as_view(), name='ecommerce_review'),
]
