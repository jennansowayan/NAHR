from django.db import models

# Create your models here.
class Technology(models.Model):
	name = models.TextField(null=True,blank=True)
	sub_category = models.TextField(null=True,blank=True)
	description= models.TextField(null=True,blank=True)
	fees= models.CharField(max_length=30)
	link = models.URLField(max_length=200)


class Business(models.Model):
	name = models.TextField(null=True,blank=True)
	sub_category = models.TextField(null=True,blank=True)
	description= models.TextField(null=True,blank=True)
	fees= models.CharField(max_length=30)
	link = models.URLField(max_length=200)

class Science(models.Model):
	name = models.TextField(null=True,blank=True)
	sub_category = models.TextField(null=True,blank=True)
	description= models.TextField(null=True,blank=True)
	fees= models.CharField(max_length=30)
	link = models.URLField(max_length=200)

class Art(models.Model):
	name = models.TextField(null=True,blank=True)
	sub_category = models.TextField(null=True,blank=True)
	description= models.TextField(null=True,blank=True)
	fees= models.CharField(max_length=30)
	link = models.URLField(max_length=200)
