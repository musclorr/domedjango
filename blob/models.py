from django.db import models

# Create your models here.
class Blob(models.Model):
	datext = models.CharField(max_length=4)
	someotherfield=models.CharField(max_length=40)

	def __unicode__(self):
		return self.datext


