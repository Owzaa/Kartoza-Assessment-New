from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from . models import *
from django.contrib.auth.decorators import login_required,permission_required



# Displaying profiles Details per User_id request
@login_required(login_url='/login/')
def profileDetails(request):
    Profile = UserProfile.objects.get(id)
       
    return render(request,"profile-page.html",
    context={'Profile':Profile})

# Profile edit profile details
@login_required(login_url='/login/')
def editProfile(request,):

    
    return render(request,"profile-edit.html",context={})

