from django.conf.urls import patterns, url

from .views import BlobListView, AddBlobView, DelBlobView

urlpatterns = patterns('',
    url(r'^$', BlobListView.as_view()),
    url(r'^del/(?P<pk>\d+)$', DelBlobView.as_view()),
    url(r'^add$', AddBlobView.as_view()),
	
)
