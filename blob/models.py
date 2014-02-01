from django.db import models

	

# Create your models here.
class Blob(models.Model):
	datext = models.CharField(max_length=4)
	someotherfield=models.CharField(max_length=40, default='')

	def __unicode__(self):
		return self.datext


class SomeAdditionalInfo(models.Model):
	blob = models.ForeignKey(Blob,  related_name='other')
	sometext = models.CharField(max_length=17)


