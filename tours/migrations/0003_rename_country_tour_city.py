# Generated by Django 3.2 on 2021-06-06 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_auto_20210606_0953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='country',
            new_name='city',
        ),
    ]
