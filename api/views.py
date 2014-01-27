from django.shortcuts import render
from blob.models import Blob
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

class BlobList(ListCreateAPIView):
	model = Blob

class OneBlob(RetrieveAPIView):
	model = Blob

