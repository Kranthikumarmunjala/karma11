from django.db import models
from teams.models import Team
# Create your models here.
class Leaderboard(models.Model):
    team=models.ForeignKey(Team,on_delete=models.SET_NULL,null=True,blank=True)
    points=models.IntegerField(null=True,blank=True)
    rank=models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.player
