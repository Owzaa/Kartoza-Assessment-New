from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from profiles.models import  UserProfile
from geopy.geocoders import Nominatim
import time
from pprint import pprint

# instantiate a new Nominatim client
app = Nominatim(user_agent=[])

# Home == function of index()
def index(request):
    title= 'Welcome to My Portfolio'
    return render(request,'index.html',
    context={'title':title})

def get_location_by_address(address):
    """This function returns a location as raw from an address
    will repeat until success"""
    time.sleep(1)
    try:
        return app.geocode(address).raw
    except:
        return get_location_by_address(address)  

# Mapping userProfile to map 
def mapDetails(request):
    title = "Screen Map Details"
    
    return render(request,'map/mapDetail.html',
    context={'title':title})
    
# Login-user
def loginView(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data= request.POST)
            if form.is_valid():
                username =form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user != None:
                    user1 = UserProfile.objects.get(user=user)
                    if user1.username == 'user':
                        login(request, user)
                        messages.info(request, f"Logged in as {{username}}")
                        return render(request,'index.html')
                    else:
                        messages.error(request, "Invalid username or password")
            else:
                messages.error(request,"Please kindly check username or password is registered")
        form = AuthenticationForm()
    return render (request=request, template_name="admin/")

# Logout-user
def signOut(request):
    logout(request)
    messages.info(request,"You've been successfully logged out")
    return render(request,'admin/')

# Sign-up user
def sign__up(request):
    title = "Sign-up User Profile"
    return render(request,"login/sign_up.html",context={'title':title})
    



