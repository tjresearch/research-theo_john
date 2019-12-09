# Generated by Django 2.2.7 on 2019-12-09 12:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_auto_20191208_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='name',
            field=models.CharField(max_length=32, unique=True, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator(message='Site names must consist of lowercase letters, numbers, and dashes. Dashes must go between two non-dash characters.', regex='^[a-z0-9]+(-[a-z0-9]+)*$')]),
        ),
    ]
