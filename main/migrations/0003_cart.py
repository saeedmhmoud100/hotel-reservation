# Generated by Django 3.2 on 2021-07-02 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('icon', models.CharField(max_length=50)),
                ('created_add', models.DateTimeField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
