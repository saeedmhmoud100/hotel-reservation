# Generated by Django 3.2 on 2021-05-29 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0017_auto_20210518_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room_image',
            name='img',
            field=models.ImageField(blank=True, upload_to='rooms/'),
        ),
    ]
