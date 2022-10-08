from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Extending UserModul via our models.
class UserProfile(models.Model):
   
    username = models.OneToOneField(User, on_delete=models.CASCADE)  
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)     
    home_address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=10)
    location = models.PointField() 

         
# return userProfile name as string     
def __str__(self):
        return self.username
