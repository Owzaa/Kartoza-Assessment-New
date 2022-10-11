from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from django.contrib.auth.decorators import login_required,permission_required



# Displaying profiles Details per User_id request
@login_required(login_url='login')
def profileDetails(request):
    
    Profile_id = get_object_or_404(UserProfile,pk=0)
    data = {}
   
    return render(request,"profile-page.html",
    context={})

# Profile edit profile details
@login_required(login_url='login')
def editProfile(request, userEditProfile_id):
    userEditProfile = get_object_or_404(UserProfile,pk=userEditProfile_id)
    data = userEditProfile
    data = {""}
    title = "User-Profile-Edit"
    
    return render(request,"profile-edit.html",context={})

