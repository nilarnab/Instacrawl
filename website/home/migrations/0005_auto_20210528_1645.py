# Generated by Django 3.0.8 on 2021-05-28 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210528_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='is_not_crawled',
            field=models.IntegerField(default=0),
        ),
    ]
