from django.db import models
from countries.models import Country
#from players.models import Player


# Create your models here.
class Match(models.Model):
    country_one=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True,blank=True, related_name='matches_as_country_one')
    country_two=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True,blank=True, related_name='matches_as_country_two')
    datetime=models.DateTimeField(null=True,blank=True)
    venue=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self(self.id)


class MatchResult(models.Model):
    match=models.ForeignKey(Match,on_delete=models.SET_NULL,null=True,blank=True)
    winner=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True,blank=True,related_name='won_results')
    runner=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True,blank=True,related_name='lost_results')
    country_one_runs=models.IntegerField(null=True,blank=True)
    country_one_wickets=models.IntegerField(null=True,blank=True)
    country_two_runs=models.IntegerField(null=True,blank=True)
    country_two_wickets=models.IntegerField(null=True,blank=True)
    man_of_match=models.ForeignKey('players.Player',on_delete=models.SET_NULL,null=True,blank=True)