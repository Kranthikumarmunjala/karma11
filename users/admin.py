from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display=['user','email','mobile_number','age','dob']

admin.site.register(CustomUser,CustomUserAdmin)