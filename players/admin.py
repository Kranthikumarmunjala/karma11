from django.contrib import admin
from .models import Player,PlayerMatchPoints
# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display=['name','number','image','runs','matches','matches','wickets','age','batting_style','bowling_style','player_type','is_captain']

admin.site.register(Player,PlayerAdmin)

class PlayerMatchPointsAdmin(admin.ModelAdmin):
    list_display=['player','match','points']


admin.site.register(PlayerMatchPoints,PlayerMatchPointsAdmin)