# Generated by Django 4.1.5 on 2023-01-30 03:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(default='', max_length=13)),
                ('name', models.CharField(default='', max_length=35)),
                ('surname', models.CharField(default='', max_length=13)),
                ('address', models.CharField(default='', max_length=13)),
                ('gender', models.BooleanField(default=True)),
                ('birthdate', models.DateField(default=datetime.date(2023, 1, 30))),
                ('salary', models.FloatField(default=0.0)),
            ],
        ),
    ]
