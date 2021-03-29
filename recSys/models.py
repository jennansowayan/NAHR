from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    user_name = models.CharField(max_length = 30)
    


class Course(models.Model):
    name = models.CharField(max_length = 50)
    date = models.DateTimeField()
    provider = models.CharField(max_length = 50)
    p_link = models.CharField(max_length = 100)
    

