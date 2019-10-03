from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()

class Event(models.Model):
    title = models.CharField(max_length=100,null=True)
    discription = models.CharField(max_length=400,null=True)
    start = models.CharField(max_length=30,null=True)
    end = models.CharField(max_length=30,null=True)

    