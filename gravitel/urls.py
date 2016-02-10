from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('gravitel.grmain.views',
    (r'^admin/admin.js$', 'adminJs'),
    (r'^catalog/ajax/(\d+)/page-(\d+)$', 'catAjax'),
    (r'^catalog/ajax/(\d+)/', 'catAjax'),
    (r'^wizard/numbers-([\d,]*)/persons-(\d+)/fax-([01])/email-([01])/lines-(\d+)/catalog-([\d,:]*)/(gravitel\.(doc|html))?$', 'wizardSummary'),
    
    (r'^$', 'index'),
    (r'^profit/$', 'profit'),
    (r'^site-map/$', 'siteMap'),
    (r'^login/$', 'login'),
    (r'^login/(\d+)/$', 'login'),
    # (r'^registration/$', 'registration'),
    # (r'^registration/(\d+)/$', 'registration'),
    
    (r'^about/$', 'about'),
    (r'^news/$', 'news'),
    (r'^news/page-(\d+)$', 'news'),
    (r'^certificates/$', 'certificates'),
    (r'^partners/$', 'partners'),
    (r'^contact/$', 'contact'),
    
    (r'^services/$', 'services'),
    (r'^services/(.+)/(video/)$', 'services'),
    (r'^services/(.+)/$', 'services'),
    (r'^video/$', 'video'),
    (r'^video/(.+)/$', 'video'),
    (r'^presentation/$', 'presentation'),
    
    (r'^help/$', 'help'),
    (r'^help/(.+)/(.+)/page-(\d+)$', 'help'),
    (r'^help/(.+)/(.+)/$', 'help'),
    (r'^help/(.+)/()page-(\d+)$', 'help'),
    (r'^help/(.+)/$', 'help'),
    
    (r'^catalog/$', 'products'),
    (r'^catalog/()page-(\d+)$', 'products'),
    (r'^catalog/(.+)/$', 'products'),
    (r'^catalog/(.+)/page-(\d+)$', 'products'),
    (r'^product/(\d+)/$', 'product'),
    (r'^order/(\d+)/$', 'order'),

    (r'^payment/$', 'payment'),
    (r'^payment/(.+)/$', 'payment'),
    
    (r'^tariffs/$', 'tariffs'),
    (r'^tariffs/(calls)/$', 'tariffs'),
    (r'^tariffs/(calls)/(russia)/$', 'tariffs'),
    (r'^tariffs/(calls)/(sng)/$', 'tariffs'),
    (r'^tariffs/(calls)/(foreign)/$', 'tariffs'),
    (r'^tariffs/(numbers)/$', 'tariffs'),
    (r'^tariffs/(numbers)/(.+)/$', 'tariffs'),
    
    (r'^wizard/$', 'wizard'),
    
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    p = settings.MEDIA_ROOT
    urlpatterns += patterns('',
        # (r'^install-install-2/$', 'gravitel.grmain.views._install'),
        (r'^404/$', 'gravitel.grmain.views._404'),
        (r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': p+'img/'}),
        (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': p+'js/'}),
        (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': p+'css/'}),
        (r'^docs/(?P<path>.*)$', 'django.views.static.serve', {'document_root': p+'docs/'}),
    )

