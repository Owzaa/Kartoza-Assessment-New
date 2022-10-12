from django.db import models
from location_field.models.plain import PlainLocationField
from django.contrib.auth.models import User

# Extending UserModul via our models.
class UserProfile(models.Model):
   
    username = models.OneToOneField(User, on_delete=models.CASCADE)  
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)     
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=255,default="false")
    location =  PlainLocationField(based_fields=['address'], zoom=7)     
    