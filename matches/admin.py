from django.contrib import admin
from .models import Match,MatchResult
# Register your models here.

class MatchAdmin(admin.ModelAdmin):
    list_display=['country_one','country_two','datetime','venue']

admin.site.register(Match,MatchAdmin)

class MatchResultAdmin(admin.ModelAdmin):
    list_display=['match','winner','runner','country_one_runs','country_one_wickets','country_two_runs','country_two_wickets','man_of_match']

admin.site.register(MatchResult,MatchResultAdmin)