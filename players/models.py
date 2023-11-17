from django.db import models
from countries.models import Country
#from players.models import Player
from matches.models import Match
# Create your models here.
class Player(models.Model):
    country=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    number=models.IntegerField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    runs=models.IntegerField(null=True,blank=True)
    matches=models.IntegerField(null=True,blank=True)
    wickets=models.IntegerField(null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    batting_style=models.CharField(max_length=255,null=True,blank=True,choices=[
        ('Left-hand bat','Left-hand bat'),
        ('Right-hand bat','Right-hand bat'),
    ])
    bowling_style=models.CharField(max_length=255,null=True,blank=True,choices=[
        ('Right-arm fast','Right-arm fast'),
        (' Left-arm fast','Left-arm fast'),
        ('Right-arm medium','Right-arm medium'),
        ('Left-arm medium','Left-arm medium'),
        ('Right-arm ofbreak','Right-arm ofbreak'),
        ('Left-arm ofbreak','Left-arm ofbreak'),
        ('Right-arm fast-medium','Right-arm fast-medium'),
        ('Left-arm fast-medium', 'Left-arm fast-medium'),
    ])
    player_type=models.CharField(max_length=255,null=True,blank=True,choices=[
        ('Batsman','Batsman'),
        ('Bowler','Bowler'),
        ('Allrounder','Allrounder'),
        ('Wicketkeeper','Wicketkeeper'),
    ])
    is_captain=models.BooleanField(null=True,blank=True)

    def __str__(self):
        return self.name

class PlayerMatchPoints(models.Model):
    player=models.ForeignKey(Player,on_delete=models.SET_NULL,null=True,blank=True)
    match=models.ForeignKey(Match,on_delete=models.SET_NULL,null=True,blank=True)
    points=models.IntegerField(null=True,blank=True)
