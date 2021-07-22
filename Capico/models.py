from django.db import models

# Create your models here.
class Coffee(models.Model):
    cname=models.CharField(max_length=200)
    cprice=models.IntegerField()
    ctag=models.TextField()
    cimg=models.ImageField(upload_to='pics')