from django.db import models

# Create your models here.
class Course(models.Model):
	name = models.TextField(null=True,blank=True)
	category = models.TextField(null=True,blank=True)
	description= models.TextField(null=True,blank=True)
	fees= models.CharField(max_length=30)
	link = models.URLField(max_length=200)