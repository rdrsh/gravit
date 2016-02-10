# -*- coding: utf-8 -*-

from django.contrib import admin
from gravitel.grmain.models import *

####################################################################################################
## banners
####################################################################################################    

admin.site.register(Banner)
admin.site.register(Banner2)

####################################################################################################
## menu
####################################################################################################    

class MenuModelAdmin(admin.ModelAdmin):
    list_display = ('sort_no', 'title', 'url',)
    search_fields = ('title', 'url',)
    
admin.site.register(MenuTop, MenuModelAdmin)
admin.site.register(MenuBottom, MenuModelAdmin)
admin.site.register(MenuStart, MenuModelAdmin)

####################################################################################################
## about
####################################################################################################    

class PageAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'sort_no')
    search_fields = ('title', 'content')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('sort_no', 'img', 'title')
    search_fields = ('title', 'content')
    
class NewsAdmin(admin.ModelAdmin):
    # fieldsets = (
        # (None,{'fields': ('title', 'datetime')}),
        # ('Содержимое', {'fields': ('text',)}))
    list_display = ('title', 'created')
    search_fields = ('created', 'title')
    list_filter = ('created',)
    date_hierarchy = 'created'
    fields = ('title', 'content')
    # filter_horizontal = ('authors',)

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('sort_no', 'img', 'title')
    search_fields = ('title', 'content')
    
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('sort_no', 'img', 'title', 'extr_url')
    search_fields = ('title', 'content', 'extr_url')
    
admin.site.register(Page, PageAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Client, PartnerAdmin)

####################################################################################################
## 
####################################################################################################    

class HelpCatAdmin(admin.ModelAdmin):
    list_display = ('sort_no', 'title', 'url')
    search_fields = ('title', 'url')
    
class HelpSubcatAdmin(admin.ModelAdmin):
    list_display = ('sort_no', 'cat', 'title', 'url')
    list_filter = ('cat',)
    search_fields = ('title', 'url')
    
class HelpAdmin(admin.ModelAdmin):
    list_display = ('sort_no', 'subcat', 'question', 'answer')
    list_filter = ('subcat',)
    search_fields = ('question', 'answer')
    
class VendorAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    
class ProductCatAdmin(admin.ModelAdmin):
    list_display = ('sort_no', 'title', 'url')
    search_fields = ('title', 'url')
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('img', 'cat', 'vendor', 'title', 'price')
    list_filter = ('cat', 'vendor', 'price')
    search_fields = ('cat', 'vendor', 'title', 'price', 'annotation', 'description')
    ordering = ('cat', 'vendor',)
    
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('sort_no', 'title')
    search_fields = ('title', 'content', 'video')
    
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('sort_no', 'img', 'title')
    search_fields = ('title', 'annotation', 'description')
    
admin.site.register(HelpCat, HelpCatAdmin)
admin.site.register(HelpSubcat, HelpSubcatAdmin)
admin.site.register(Help, HelpAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(ProductCat, ProductCatAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Payment, PaymentAdmin)

####################################################################################################
## phone
####################################################################################################    

class NumberTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'price', 'sort_no')
    list_editable = ('url', 'price', 'sort_no')
    search_fields = ('title', 'url', 'price')
    
class NumberAdmin(admin.ModelAdmin):
    list_display = ('title', 'type')
    list_filter = ('type',)
    list_editable = ('type',)
    # radio_fields = ('type',)
    search_fields = ('title',)
    
admin.site.register(NumberType, NumberTypeAdmin)
admin.site.register(Number, NumberAdmin)
admin.site.register(CallRussia)
admin.site.register(CallSng)
admin.site.register(CallForeign)

####################################################################################################
## settings
####################################################################################################    

class SettingsAdmin(admin.ModelAdmin):
    # list_display = ('name', 'value', 'comment')
    # list_editable = ('value', 'comment')
    list_display = ('comment', 'value')
    list_editable = ('value',)
    
admin.site.register(Settings, SettingsAdmin)

class IncomingAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    
admin.site.register(Incoming, IncomingAdmin)