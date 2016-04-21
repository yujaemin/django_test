from django.contrib import admin
from .models import EcommerceListItem, CrawlingSiteList, EcommerceReviewItem

# Register your models here.
admin.site.register(CrawlingSiteList)
admin.site.register(EcommerceListItem)
admin.site.register(EcommerceReviewItem)
