# Generated by Django 3.2 on 2021-07-05 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_newsletter_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter_email',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]