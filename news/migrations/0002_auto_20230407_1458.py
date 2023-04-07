# Generated by Django 3.2 on 2023-04-07 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
