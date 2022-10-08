from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


# Home == function of index()
def index(request):
    title= 'Welcome to My Portfolio'
    return render(request,'index.html',
    context={'title':title})

# Mapping userProfile to map 
def mapDetails(request):
    title = "Screen Map Details"
    return render(request,'map/mapDetail.html',
    context={'title':title})
    
# Login-user
def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            username =form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user != None:
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
def signUp(request):
    logout(request)
    messages.info(request,"You've been successfully logged out")
    return render(request,'admin/')

# Sign-up user




