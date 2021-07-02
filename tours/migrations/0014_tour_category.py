# Generated by Django 3.2 on 2021-07-02 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category'),
        ('tours', '0013_auto_20210701_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
            preserve_default=False,
        ),
    ]