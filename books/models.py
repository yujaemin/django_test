# -*- coding : utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher')
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title
        # return smart_unicode(self.title)

class Author(models.Model):
    salutation = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    publication_date = models.DateField()

    def __unicode__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    website = models.URLField()

    def __unicode__(self):
        return self.name
