from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView, DeleteView
from .models import Blob
from .forms import TextForm

from django.shortcuts import redirect
import logging
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# Get an instance of a logger
logger = logging.getLogger(__name__)

class BlobListView(ListView):
	model = Blob


class AddBlobView(SuccessMessageMixin, CreateView):
	model = Blob
	success_url = "/"
	success_message=" OK!"

	def form_invalid(self, form_invalid):
		#messages.error("invalid form")
		return redirect("/")
		

	
class DelBlobView(DeleteView):
	model = Blob
	success_url = "/"

