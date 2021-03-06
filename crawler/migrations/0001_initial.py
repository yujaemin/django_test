# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-19 07:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrawlingSiteList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rClass', models.CharField(default='site', max_length=30)),
                ('message', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(default='READY', max_length=10)),
                ('url', models.CharField(max_length=200)),
                ('spiderName', models.CharField(default='', max_length=30)),
                ('siteName', models.CharField(max_length=50)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('latestCrawlTime', models.DateTimeField(default=datetime.datetime.today)),
            ],
        ),
        migrations.CreateModel(
            name='EcommerceListItem',
            fields=[
                ('rClass', models.CharField(default='ecommerceList', max_length=30)),
                ('message', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(default='ok', max_length=10)),
                ('crawlTime', models.DateTimeField(default=datetime.datetime.today)),
                ('uid', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('category', models.CharField(blank=True, max_length=20, null=True)),
                ('linkUrl', models.CharField(blank=True, max_length=100, null=True)),
                ('createTime', models.DateTimeField(default=datetime.datetime.today)),
                ('refCount', models.PositiveIntegerField(blank=True, null=True)),
                ('reviewCount', models.PositiveIntegerField()),
                ('writerId', models.CharField(blank=True, max_length=30, null=True)),
                ('writerName', models.CharField(blank=True, max_length=30, null=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True, null=True)),
                ('rawData', models.TextField(blank=True, null=True)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('totalCount', models.PositiveIntegerField(blank=True, null=True)),
                ('agreeCount', models.PositiveIntegerField(blank=True, null=True)),
                ('refuseCount', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
