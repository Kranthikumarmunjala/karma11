from django.contrib import admin
from.models import Team
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display=['name','country','description','logo']
    list_filter=['country']

admin.site.register(Team,TeamAdmin)