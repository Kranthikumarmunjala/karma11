from django.contrib import admin
from.models import Team
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display=['user','match','player','name','is_captain','logo']
    list_filter=['player']

admin.site.register(Team,TeamAdmin)