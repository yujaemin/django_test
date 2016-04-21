#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_unicode
import datetime

# Create your models here.
class CrawlingSiteList(models.Model):
    rClass = models.CharField(max_length=30, default="site")
    message = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=10, default="READY")
    url = models.CharField(max_length=200)
    spiderName = models.CharField(max_length=30, default="")
    siteName = models.CharField(max_length=50)
    category = models.CharField(max_length=50, null=True, blank=True)
    latestCrawlTime = models.DateTimeField(default=datetime.datetime.today)

    def __unicode__(self):
        return u'siteName : %s, spiderName : %s, category : %s' %(self.siteName, self.spiderName, self.category)
        # return smart_unicode(self.title)

class EcommerceListItem(models.Model):
    rClass = models.CharField(max_length=30, default="ecommlist")
    message = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=10, default="ok")
    crawlTime = models.DateTimeField(default=datetime.datetime.today)
    uid = models.CharField(max_length=30, primary_key=True)
    category = models.CharField(max_length=20, null=True, blank=True)
    linkUrl = models.CharField(max_length=100, null=True, blank=True)
    createTime = models.DateTimeField(default=datetime.datetime.today)
    refCount = models.PositiveIntegerField(null=True, blank=True)
    reviewCount = models.PositiveIntegerField()
    writerId = models.CharField(max_length=30, null=True, blank=True)
    writerName = models.CharField(max_length=30, null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    rawData = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    totalCount = models.PositiveIntegerField(null=True, blank=True)
    agreeCount = models.PositiveIntegerField(null=True, blank=True)
    refuseCount = models.PositiveIntegerField(null=True, blank=True)

    def __unicode__(self):
        return u'title : %s, status : %s ' %(self.title, self.status)
        # return smart_unicode(self.title)

class EcommerceReviewItem(models.Model):
    rClass = models.CharField(max_length=30, default="ecommreview")
    message = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=10, default="ok")
    uid = models.ForeignKey(EcommerceListItem, on_delete=models.CASCADE)
    reviewId = models.CharField(max_length=30, primary_key=True)
    writerId = models.CharField(max_length=30, null=True, blank=True)
    writerName = models.CharField(max_length=30, null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    crawlTime = models.DateTimeField(default=datetime.datetime.today)
    createTime = models.DateTimeField(default=datetime.datetime.today)
    commentCount = models.PositiveIntegerField(null=True, blank=True)
    refCount = models.PositiveIntegerField(null=True, blank=True)
    totalCount = models.PositiveIntegerField(null=True, blank=True)
    agreeCount = models.PositiveIntegerField(null=True, blank=True)
    refuseCount = models.PositiveIntegerField(null=True, blank=True)

    def __unicode__(self):
        return u'title : %s, status : %s ' %(self.title, self.status)
        # return smart_unicode(self.title)
