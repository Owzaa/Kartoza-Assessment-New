from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from profiles.models import  UserProfile
import time
from django.contrib.auth.decorators import login_required,permission_required


# instantiate a new Nominatim client

def __init__(self):
    self.home_address = {}
    self.location = {}
    UserProfile.get_deferred_fields(self)    

# Home == function of index()
def homeView(request):
    title= 'Welcome to My Portfolio'
    return render(request,'index.html',
    context={'title':title})

# GET: address then passing it into location PointField()
def get_address(place):
    geolocator = place
    geocode = geolocator

    address = None
    try:
        location = geocode(place)
        if location is not None:
            address = geolocator.reverse(
                "{lat}, {lon}".format(lat=location.latitude, lon=location.longitude)
            ).raw["address"]
            address["latitude"] = location.latitude
            address["longitude"] = location.longitude
    except:
        # TODO: add 2 retries using tenacity
        print(f"Geocoder timed out for {place}!")

    return address

"""
    The following function reverses the coordinates 
    along with respecting Nominatim
    
"""

def get_location(latitude, longitude, language="en"):
    """
    This function returns an address as raw from a location
    will repeat until success

    """
    # build coordinates string to pass to reverse() function
    coordinates = f"{latitude}, {longitude}"
    # sleep for a second to respect Usage Policy
    time.sleep(1)
    try:
        return get_location.reverse(coordinates, language=language)
    except:
        return get_location(latitude, longitude)


# Mapping userProfile to map 
"""
PERMISSION 
"""
@login_required(login_url='login')
def mapDetails(request):
    title = "Screen Map Details"   
    return render(request,'map/mapDetail.html',
    context={'title':title})
    
# User_LoginAuthetication
def loginView(request):  
    #Session Activity Log Request for Our Admin Log HISTORY
    if request.user.is_authenticated:
        return redirect("")
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
                      
                        messages.info(request, f"Logged in as {{username}}")
                        return render(request,'index.html')
                    else:
                        messages.error(request, "Invalid username or password")
            else:
                messages.error(request,"Please kindly check username or password is registered")
        form = AuthenticationForm()
    return render (request=request, template_name="login/login.html")

# Logout-user
def signOut(request):
    logout(request)
    try:
        del request.session['user_id']
    except KeyError:
        pass
    messages.info(request,"You've been successfully logged out")
    return render(request,'login/login.html')

# Sign-up user
def signUp(request):
    title = "Sign-up User Profile"
    return render(request,"login/sign_up.html",context={'title':title})
    



