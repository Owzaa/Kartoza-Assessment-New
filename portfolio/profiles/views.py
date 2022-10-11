from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from django.contrib.auth.decorators import login_required,permission_required



# Displaying profiles Details per User_id request
@login_required(login_url="loginView/")
@permission_required(perm='folioApp.view_choice')

def profileDetails(request, userProfile_id):
    
    profile = get_object_or_404(UserProfile, pk=userProfile_id)
    
    return render(request,"profile-page.html",
    context={'profile':profile})

# Profile edit profile details
@login_required(login_url="loginView/")
@permission_required(perm='profiles.view_choice')

def editProfile(request,userProfile_id, *kwargs,**args):
    editProf = get_object_or_404(userProfile_id)
    title = "User-Profile-Edit"
    
    return render(request,"profile-edit.html",
    context={'title':title,'editprof':editProf})

