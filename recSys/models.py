from django.db import models

# Create your models here.


class rules(models.Model):
    antecedents = models.CharField(max_length=30)
    consequents = models.CharField(max_length=30)

    # def __init__(self, ant, con):
    #     self.antecedents = ant
    #     self.consequents = con

    # def __str__(self):
    #     return self.antecedents, self.consequents
