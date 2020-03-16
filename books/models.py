from django.db import models
import datetime

class info(models.Model):
    name=models.CharField(max_length=55)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.CharField(max_length=5000)

class data(models.Model):
    username=models.CharField(max_length=20, default='hey')
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=10)







