from django.db import models

# Create your models here.


class Technology(models.Model):

	CATEGORY = (('prog', 'prog'),
	('cyber', 'cyber'), ('ai', 'ai'))

	CATEGORY = (('prog', 'programming'),
	('c', 'security'), ('UX', 'UX'))

	name = models.TextField(null=True,blank=True)
	sub_category = models.TextField(null=True,blank=True, choices=CATEGORY)
	description= models.TextField(null=True,blank=True)
	fees= models.CharField(max_length=30)
	link = models.URLField(max_length=200)


class Business(models.Model):
	CATEGORY = (('pm', 'pm'),
	('mark', 'mark'), ('acc', 'acc'))

	name = models.TextField(null=True,blank=True)
	sub_category = models.TextField(null=True,blank=True, choices=CATEGORY)
	description= models.TextField(null=True,blank=True)
	fees= models.CharField(max_length=30)
	link = models.URLField(max_length=200)

class Science(models.Model):
	CATEGORY = (('bio', 'bio'),
	('phy', 'phy'), ('chem', 'chem'),('math', 'math'))

	name = models.TextField(null=True,blank=True)
	sub_category = models.TextField(null=True,blank=True, choices=CATEGORY)
	description= models.TextField(null=True,blank=True)
	fees= models.CharField(max_length=30)
	link = models.URLField(max_length=200)

class Art(models.Model):
	CATEGORY = (('fash', 'fash'),
	('music', 'music'), ('da', 'da'))

	name = models.TextField(null=True,blank=True)
	sub_category = models.TextField(null=True,blank=True, choices=CATEGORY)
	description= models.TextField(null=True,blank=True)
	fees= models.CharField(max_length=30)
	link = models.URLField(max_length=200)

