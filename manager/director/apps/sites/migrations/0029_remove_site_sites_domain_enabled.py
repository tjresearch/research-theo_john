# Generated by Django 2.2.10 on 2020-02-16 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0028_auto_20200216_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='sites_domain_enabled',
        ),
    ]
