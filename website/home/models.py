from django.db import models

# Create your models here.


class Accounts(models.Model):
    name = models.CharField(max_length=255, default='NA')
    insta_username = models.CharField(max_length=255, unique=True, default='NA')
    api_user_id = models.CharField(max_length=255, unique=True, default='NA')
    followers = models.IntegerField(default=0)
    image_url = models.TextField(default='NA')
    email = models.EmailField(unique=True, default='na@gmail.com')
    genre = models.CharField(max_length=255, default='MISC')
    date = models.DateField()
    is_not_crawled = models.IntegerField(default=0)


class Resource(models.Model):
    action = models.CharField(max_length=255, default=None)
    done = models.IntegerField(default=0)




