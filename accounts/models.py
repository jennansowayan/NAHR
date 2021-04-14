from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.
class intrest(models.Model):
 intrest_choices = (
    ('cyber', 'Cybersecurity'),
    ('prog', 'Programming'),
    ('ai', 'Artificial Intelligence'),
    ('math', 'Math'),
    ('chem', 'Chemistry'),
    ('phy', 'Physics'),
    ('bio', 'Biology'),
    ('pm', 'Project Managment'),
    ('acc', 'Accounting'),
    ('mark', 'Marketing'),
    ('music', 'Music'),
    ('da', 'Digital Art'),
    ('fash', 'Fashion'),
    
    )

 intrests = MultiSelectField(choices = intrest_choices)
 

