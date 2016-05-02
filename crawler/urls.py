from django.conf.urls import patterns, url
from crawler import views
from mysite import settings
urlpatterns = [
    url(r'^$', views.CrawlerMainView.as_view(), name='main'),
    url(r'^new_crawl/coupang/ecommerce_list$', views.NewCrawlEcommerceListView.as_view(), name='new_crawl_ecommerce_list'),
    url(r'^new_crawl/coupang/ecommerce_review$', views.NewCrawlEcommerceReviewView.as_view(), name='new_crawl_ecommerce_review'),
    url(r'^ecommerce_list/coupang/(?P<category>\S+)/$', views.CrawlerListView.as_view(), name='ecommerce_list'),
    url(r'^ecommerce_review/coupang/(?P<uid>\d+)/$', views.CrawlerReviewView.as_view(), name='ecommerce_review'),
]
