#-*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View, TemplateView, ListView
from .models import EcommerceListItem, CrawlingSiteList

import commands
import urllib2, re

def convert_category(category):
    if category == u'출산/유아동':
        category='94404'
    elif category == u'반려/애완용품':
        category='41853'
    elif category == u'반려/애완용품':
        category='41853'
    elif category == u'식품':
        category='41563'
    elif category == u'뷰티':
        category='108460'
    else:
        category=None
    return category

# Create your views here.
class CrawlerMainView(TemplateView):
    model = CrawlingSiteList
    template_name = 'crawler/index.html'
    success_url = template_name

    def get_context_data(self, **kwargs):
        context = super(CrawlerMainView, self).get_context_data(**kwargs)
        context['object_list'] = CrawlingSiteList.objects.all()
        print CrawlingSiteList.objects.all()
        return context

class NewCrawlView(View):
    model = CrawlingSiteList

    def post(self, request, *args, **kwargs):
        keyword = request.POST['keyword']
        category = convert_category(request.POST['category'])
        cmd = u'curl http://localhost:6800/schedule.json -F project=MAScrapper -F spider=coupanglist -F setting=DOWNLOAD_DELAY=30 -F category={category} -F keyword={keyword}'.format(keyword=keyword, category=category)
        cmd = cmd.encode('utf8')
        failure, result = commands.getstatusoutput(cmd)
        if failure:
            print 'FAILED!'
        return HttpResponseRedirect(reverse('crawler:main'))

class CrawlerListView(TemplateView):
    model = EcommerceListItem
    template_name = 'crawler/ecommerce_list.html'

    def get_context_data(self, **kwargs):
        category = self.request.GET['category']
        category = convert_category(category)
        context = super(CrawlerListView, self).get_context_data(**kwargs)
        #context['object_list'] = EcommerceListItem.objects.all()
        context['object_list'] = EcommerceListItem.objects.filter(category=category)
        return context
