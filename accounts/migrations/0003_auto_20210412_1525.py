# Generated by Django 3.1.7 on 2021-04-12 15:25

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210411_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intrest',
            name='intrests',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Cybersecurity', 'Cybersecurity'), ('Programming', 'Programming'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Math', 'Math'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics'), ('Biology', 'Biology'), ('Project Managment', 'Project Managment'), ('Accounting', 'Accounting'), ('Marketing', 'Marketing'), ('Music', 'Music'), ('Digital Art', 'Digital Art'), ('Fashion', 'Fashion')], max_length=145),
        ),
    ]
