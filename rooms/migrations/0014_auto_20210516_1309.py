# Generated by Django 3.2 on 2021-05-16 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0013_auto_20210516_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room_reservation',
            old_name='email',
            new_name='email_entred',
        ),
        migrations.AddField(
            model_name='room_reservation',
            name='email_registered',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]