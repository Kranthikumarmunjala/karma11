from django.db import models
from countries.models import Country
# Create your models here.
class Team(models.Model):
    country=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True, null=True)
    logo=models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.name






# class Player(models.Model):
#     team =models.ForeignKey(Team, on_delete=models.SET_NULL,null=True,blank=True)
#     name=models.CharField(max_length=255)
#     number=models.IntegerField(null=True,blank=True)
#     image=models.ImageField(null=True,blank=True)
#     runs=models.IntegerField(null=True,blank=True)
#     matches_played=models.IntegerField(null=True,blank=True)
#
#     def __str__(self):
#         return self.name
#
