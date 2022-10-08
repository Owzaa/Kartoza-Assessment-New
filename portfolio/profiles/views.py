from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance

longitude = {}
latitude = {}
# Displaying profiles Details per User_id request
def profileDetails(request, userProfile_id):
    model = UserProfile
    profile = get_object_or_404(UserProfile, pk=userProfile_id)
    user_location = profile.location(longitude,latitude, srid=4326)
    return render(request,"profile-page.html",
    context={'profile':profile,'user_location':user_location})

# Profile edit profile details
def editProfile(request,userProfile_id):
    editPrf = get_object_or_404(userProfile_id)
    title = "User-Profile-Edit"
    return render(request,"profile-edit.html",
    context={'title':title,'editprof':editPrf})
    