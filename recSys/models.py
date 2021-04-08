from django.db import models

# Create your models here.

class rules():
    antecedents = models.CharField(max_length=30)
    consequents = models.CharField(max_length=30)

