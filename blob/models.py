from django.db import models

# Create your models here.
class Blob(models.Model):
	datext = models.CharField(max_length=4)


