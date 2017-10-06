from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 80, unique = True)
	content = models.TextField()
	timestamp = models.DateTimeField()


	def __str__(self):
		return self.title

	#def __unicode__(self):
	#	return self.title        #for python2 users