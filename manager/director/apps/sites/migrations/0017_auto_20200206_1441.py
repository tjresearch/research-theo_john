# Generated by Django 2.2.10 on 2020-02-06 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0016_auto_20200202_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='type',
            field=models.CharField(choices=[('create_site', 'Creating site'), ('rename_site', 'Renaming site'), ('edit_site_names', 'Changing site name/domains'), ('change_site_type', 'Changing site type'), ('regen_nginx_config', 'Regenerating Nginx configuration'), ('create_site_database', 'Creating site database'), ('delete_site_database', 'Deleting site database'), ('regen_site_secrets', 'Regenerating site secrets'), ('delete_site', 'Deleting site'), ('restart_site', 'Restarting site')], max_length=24),
        ),
    ]
