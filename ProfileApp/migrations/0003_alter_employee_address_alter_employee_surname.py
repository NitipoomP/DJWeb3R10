# Generated by Django 4.1.5 on 2023-01-30 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileApp', '0002_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='employee',
            name='surname',
            field=models.CharField(default='', max_length=35),
        ),
    ]
