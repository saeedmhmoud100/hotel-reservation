# Generated by Django 3.2 on 2021-07-27 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorie',
            options={'verbose_name': 'categorie', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id'], 'verbose_name': 'post', 'verbose_name_plural': 'Posts'},
        ),
    ]