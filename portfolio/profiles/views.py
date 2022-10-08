from django.shortcuts import render, get_object_or_404
from models import UserProfile

# Displaying profiles Details per User_id request
def profileDetails(request, userProfile_id):
    profile = get_object_or_404(UserProfile, pk=userProfile_id)
    user_location = UserProfile.location
    return render(request,"profiles/templates/profile-page.html",
    context={'profile':profile,'user_location':user_location})

# Profile edit profile details
def editProfile(request,userProfile_id):
    editPrf = get_object_or_404(userProfile_id)
    title = "User-Profile-Edit"
    return render(request,"profiles/templates/profile-edit.html",
    context={'title':title,'editprof':editPrf})
    