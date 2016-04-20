#-*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View, TemplateView
from .models import EcommerceListItem, CrawlingSiteList

# Create your views here.
class CrawlerMainView(TemplateView):
    template_name = 'crawler/index.html'
    success_url = template_name

    def get_context_data(self, **kwargs):
        context = super(CrawlerMainView, self).get_context_data(**kwargs)
        context['object_list'] = CrawlingSiteList.objects.all()
        print CrawlingSiteList.objects.all()
        return context

class NewCrawlView(View):
    def post(self, request, *args, **kwargs):
        p = request.POST['keyword']
        print 'scrapy crawl coupanglist'
        return HttpResponseRedirect(reverse('crawler:main'))
