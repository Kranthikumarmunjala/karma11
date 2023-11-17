from django.contrib import admin
from .models import Leaderboard
# Register your models here.
class LeaderboardAdmin(admin.ModelAdmin):
    list_display=['player','points','rank']
    list_filter=['points']

admin.site.register(Leaderboard,LeaderboardAdmin)