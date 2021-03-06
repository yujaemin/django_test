#-*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View, TemplateView, ListView
from .models import EcommerceListItem, CrawlingSiteList, EcommerceReviewItem

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

class NewCrawlEcommerceListView(View):
    model = CrawlingSiteList

    def post(self, request, *args, **kwargs):
        print request.POST
        keyword = request.POST['keyword']
        if not keyword or keyword == '' or len(re.findall('\s+', keyword)) > 1:
            ## 작업 추가..
            print 'error'
            return HttpResponseRedirect(reverse('crawler:main'))
        else:
            category = convert_category(request.POST['category'])
            cmd = u'curl http://localhost:6800/schedule.json -F project=MAScrapper -F spider=coupanglist -F setting=DOWNLOAD_DELAY=30 -F category={category} -F keyword={keyword}'.format(keyword=keyword, category=category)
            cmd = cmd.encode('utf8')
            failure, result = commands.getstatusoutput(cmd)
            if failure:
                print 'FAILED!'
            return HttpResponseRedirect(reverse('crawler:main'))

class NewCrawlEcommerceReviewView(View):
    model = EcommerceReviewItem

    def post(self, request, *args, **kwargs):
        print request.POST
        uid = request.POST['uid']
        if not uid or uid == '':
            ## 작업 추가..
            print 'error'
            return HttpResponseRedirect(reverse('crawler:main'))
        else:
            cmd = u'curl http://localhost:6800/schedule.json -F project=MAScrapper -F spider=coupangreview -F setting=DOWNLOAD_DELAY=30 -F uid={uid}'.format(uid=uid)
            cmd = cmd.encode('utf8')
            failure, result = commands.getstatusoutput(cmd)
            print "###"
            print failure
            print result
            print "###"
            if failure:
                print 'FAILED!'
            return HttpResponseRedirect(request.POST['previous'])

class CrawlerListView(TemplateView):
    model = EcommerceListItem
    template_name = 'crawler/ecommerce_list.html'

    def get_context_data(self, **kwargs):
        print kwargs
        category = kwargs['category']
        category = convert_category(category)
        context = super(CrawlerListView, self).get_context_data(**kwargs)
        #context['object_list'] = EcommerceListItem.objects.all()
        context['object_list'] = EcommerceListItem.objects.filter(category=category)
        return context

class CrawlerReviewView(TemplateView):
    model = EcommerceReviewItem
    template_name = 'crawler/ecommerce_review.html'

    def get_context_data(self, **kwargs):
        print '!!'
        uid = kwargs['uid']
        context = super(CrawlerReviewView, self).get_context_data(**kwargs)
        context['object_list'] = EcommerceReviewItem.objects.filter(uid_id=uid)
        return context
