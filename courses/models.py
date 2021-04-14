from django.db import models

# Create your models here.


class Technology(models.Model):
	CATEGORY = (('prog', 'programming'),
	('c', 'security'), ('UX', 'UX'))

	name = models.TextField(null=True,blank=True)
	sub_category = models.TextField(null=True,blank=True, choices=CATEGORY)
	description= models.TextField(null=True,blank=True)
	fees= models.CharField(max_length=30)
	link = models.URLField(max_length=200)


class Business(models.Model):
	CATEGORY = (('Project Managment', 'Project Managment'),
	('Marketing', 'Marketing'), ('Accounting', 'Accounting'))

	name = models.TextField(null=True,blank=True)
	sub_category = models.TextField(null=True,blank=True, choices=CATEGORY)
	description= models.TextField(null=True,blank=True)
	fees= models.CharField(max_length=30)
	link = models.URLField(max_length=200)

class Science(models.Model):
	CATEGORY = (('Biology', 'Biology'),
	('Physics', 'Physics'), ('Chemistry', 'Chemistry'),('Math', 'Math'))

	name = models.TextField(null=True,blank=True)
	sub_category = models.TextField(null=True,blank=True, choices=CATEGORY)
	description= models.TextField(null=True,blank=True)
	fees= models.CharField(max_length=30)
	link = models.URLField(max_length=200)

class Art(models.Model):
	CATEGORY = (('Fashion', 'Fashion'),
	('Music', 'Music'), ('Digital', 'Digital'))

	name = models.TextField(null=True,blank=True)
	sub_category = models.TextField(null=True,blank=True, choices=CATEGORY)
	description= models.TextField(null=True,blank=True)
	fees= models.CharField(max_length=30)
	link = models.URLField(max_length=200)

