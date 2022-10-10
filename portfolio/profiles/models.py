from django.contrib.auth.models import User
from django.db import models
# Extending UserModul via our models.
class UserProfile(models.Model):
   
    username = models.OneToOneField(User, on_delete=models.CASCADE)  
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)     
    home_address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=10)
    location = models.CharField()  
         
