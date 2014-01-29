from django.conf.urls import patterns, url

from .views import BlobListView, DelBlobView

urlpatterns = patterns('',
    url(r'^$', BlobListView.as_view()),
    url(r'^del/(?P<pk>\d+)$', DelBlobView.as_view()),
	
)
