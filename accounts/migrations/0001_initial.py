# Generated by Django 3.1.7 on 2021-04-09 22:27

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='intrest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intrests', multiselectfield.db.fields.MultiSelectField(choices=[('cybersecurity', 'cybersecurity'), ('math', 'math'), ('project managment', 'project managment'), ('music', 'music')], max_length=42)),
            ],
        ),
    ]
