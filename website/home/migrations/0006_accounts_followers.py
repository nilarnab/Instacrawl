# Generated by Django 3.0.8 on 2021-05-28 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210528_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='followers',
            field=models.CharField(default='NA', max_length=255),
        ),
    ]
