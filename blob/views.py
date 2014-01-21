from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import ListView
from .models import Blob

class BlobListView(ListView):
    model = Blob

