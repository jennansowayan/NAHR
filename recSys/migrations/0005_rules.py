
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recSys', '0004_auto_20210408_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antecedents', models.CharField(max_length=30)),
                ('consequents', models.CharField(max_length=30)),
            ],
        ),
    ]
