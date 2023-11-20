from django.db import models
from players.models import Player
from users.models import CustomUser
from matches.models import Match
# Create your models here.
class Team(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,blank=True)
    match=models.ForeignKey(Match,on_delete=models.SET_NULL,null=True,blank=True)
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True)
    name=models.CharField(max_length=255)
    is_captain=models.BooleanField(null=True,blank=True)
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
