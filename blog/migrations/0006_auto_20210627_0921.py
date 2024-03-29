# Generated by Django 3.2 on 2021-06-27 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210627_0918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorie',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='post',
            name='categorie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.categorie'),
            preserve_default=False,
        ),
    ]
