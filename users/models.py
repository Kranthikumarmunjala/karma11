from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    # user_role=models.CharField(max_length=255,null=True,blank=True,choices=[
    #     ('Admin','Admin'),
    #     ('User','User'),
    # ])
    user=models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(unique=True)
    mobile_number=models.IntegerField(null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    dob = models.DateField(null=True, blank=True)
