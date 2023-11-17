from django.db import models

# Create your models here.
class Country(models.Model):
    name=models.CharField(max_length=255)
    short_code=models.CharField(max_length=5)
    color=models.CharField(max_length=15)
    flag=models.ImageField()