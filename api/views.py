from django.shortcuts import render
from blob.models import Blob
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .serializers import BlobSerializer

class BlobList(ListCreateAPIView):
	model = Blob
	serializer_class = BlobSerializer

class OneBlob(RetrieveAPIView):
	model = Blob
	serializer_class = BlobSerializer

