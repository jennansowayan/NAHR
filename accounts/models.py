from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.
class intrest(models.Model):
 intrest_choices = (
    ('Cybersecurity', 'Cybersecurity'),
    ('Programming', 'Programming'),
    ('Artificial Intelligence', 'Artificial Intelligence'),
    ('Math', 'Math'),
    ('Chemistry', 'Chemistry'),
    ('Physics', 'Physics'),
    ('Biology', 'Biology'),
    ('Project Managment', 'Project Managment'),
    ('Accounting', 'Accounting'),
    ('Marketing', 'Marketing'),
    ('Music', 'Music'),
    ('Digital Art', 'Digital Art'),
    ('Fashion', 'Fashion'),
    
    )

 intrests = MultiSelectField(choices = intrest_choices)
