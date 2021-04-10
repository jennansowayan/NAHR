from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.
class intrest(models.Model):
 intrest_choices = (
    ('cybersecurity', 'cybersecurity'),
    ('math', 'math'),
    ('project managment', 'project managment'),
    ('music', 'music'),
    ('Photography', 'Photography'),
    ('Fashion Design', 'Fashion Design'),
    ('Artificial Intelligence', 'Artificial Intelligence'),
    ('Accounting', 'Accounting'),
    ('Chemistry', 'Chemistry'),
    ('Marketing', 'Marketing'),
    )

 intrests = MultiSelectField(choices = intrest_choices)
