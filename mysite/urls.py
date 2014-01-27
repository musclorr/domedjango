from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.admindocs import urls as admindocurls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^$', include('blob.urls')),
    url(r'^blob/', include('blob.urls')),
    url(r'^admin/doc/', include(admindocurls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
)
