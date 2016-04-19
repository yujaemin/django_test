#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import EcommerceListItem, CrawlingSiteList

# Create your views here.
class CrawlerMainView(TemplateView):
    template_name = 'crawler/index.html'

    def get_context_data(self, **kwargs):
        context = super(CrawlerMainView, self).get_context_data(**kwargs)
        context['object_list'] = CrawlingSiteList.objects.all()
        print CrawlingSiteList.objects.all()
        return context
