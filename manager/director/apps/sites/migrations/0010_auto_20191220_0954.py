# Generated by Django 2.2.8 on 2019-12-20 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0009_auto_20191220_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='database',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='site', to='sites.Database'),
        ),
    ]
