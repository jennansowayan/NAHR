from django.db import models

# Create your models here.


class Technology(models.Model):

	CATEGORY = (('prog', 'Programming'),
	('cyber', 'Cybersecurity'), ('ai', 'Artificial intelligence'))

	
	name = models.TextField(null=True,blank=True)
	sub_category = models.TextField(null=True,blank=True, choices=CATEGORY)
	description= models.TextField(null=True,blank=True)
	fees= models.CharField(max_length=30)
	link = models.URLField(max_length=200)


class Business(models.Model):
	CATEGORY = (('pm', 'Project Managment'),
	('mark', 'Marketing'), ('acc', 'Accounting'))

	name = models.TextField(null=True,blank=True)
	sub_category = models.TextField(null=True,blank=True, choices=CATEGORY)
	description= models.TextField(null=True,blank=True)
	fees= models.CharField(max_length=30)
	link = models.URLField(max_length=200)

class Science(models.Model):
	CATEGORY = (('bio', 'Biology'),
	('phy', 'Physics'), ('chem', 'Chemistry'),('math', 'Math'))

	name = models.TextField(null=True,blank=True)
	sub_category = models.TextField(null=True,blank=True, choices=CATEGORY)
	description= models.TextField(null=True,blank=True)
	fees= models.CharField(max_length=30)
	link = models.URLField(max_length=200)

class Art(models.Model):
	CATEGORY = (('fash', 'Fashion'),
	('music', 'Music'), ('da', 'Digital Art'))

	name = models.TextField(null=True,blank=True)
	sub_category = models.TextField(null=True,blank=True, choices=CATEGORY)
	description= models.TextField(null=True,blank=True)
	fees= models.CharField(max_length=30)
	link = models.URLField(max_length=200)

