from django.shortcuts import render
from blob.models import Blob
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework import filters
from .serializers import BlobSerializer

class BlobList(ListCreateAPIView):
	model = Blob
	serializer_class = BlobSerializer
	filter_fields = ("datext", "someotherfield","other__sometext")
	filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)
	search_fields = ('other__sometext',)

class OneBlob(RetrieveAPIView):
	model = Blob
	serializer_class = BlobSerializer

