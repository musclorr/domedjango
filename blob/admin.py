from django.contrib import admin

from .models import Blob, SomeAdditionalInfo

admin.site.register(Blob)
admin.site.register(SomeAdditionalInfo)
