# Generated by Django 4.0.4 on 2022-08-10 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curdapp', '0003_remove_studentdata_assigentnt3'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentdata',
            old_name='first_name',
            new_name='Data',
        ),
    ]
