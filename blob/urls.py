from django.conf.urls import patterns, url

from .views import BlobListView

urlpatterns = patterns('',
    url(r'^$', BlobListView.as_view())
)
