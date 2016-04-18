from django.conf.urls import patterns, url
from polls import views
from polls.views import MyView
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultView.as_view(), name='results'),
    #url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<pk>\d+)/vote/$', views.VoteView.as_view(), name='vote'),
    url(r'^form_test/$', views.form_test, name='form_test'),
    url(r'about/$', MyView.as_view()),
]
