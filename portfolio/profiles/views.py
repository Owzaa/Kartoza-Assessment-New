from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from django.contrib.auth.decorators import login_required,permission_required



# Displaying profiles Details per User_id request
@login_required(login_url='login')

def profileDetails(request):
    
    profile = get_object_or_404(UserProfile,id= +1)
    data = {}
   
    return render(request,"profile-page.html",
    context={'profile': profile,'data': data})

# Profile edit profile details
@login_required(login_url='login')

def editProfile(request,userProfile_id):
    editProf = get_object_or_404(userProfile_id)
    title = "User-Profile-Edit"
    
    return render(request,"profile-edit.html",
    context={'title': title,'editprof': editProf})

