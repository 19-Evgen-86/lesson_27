# Generated by Django 4.0.6 on 2022-07-09 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='ads',
            name='price',
            field=models.IntegerField(default=100),
        ),
    ]
