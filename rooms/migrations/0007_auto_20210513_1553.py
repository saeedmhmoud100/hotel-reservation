# Generated by Django 3.2 on 2021-05-13 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_auto_20210512_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Active_Room',
            fields=[
            ],
            options={
                'verbose_name': 'Active Rooms',
                'verbose_name_plural': 'Active Rooms',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('rooms.room',),
        ),
        migrations.AddField(
            model_name='room',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]