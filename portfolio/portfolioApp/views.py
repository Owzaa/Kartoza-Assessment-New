from django.shortcuts import render

# HomeView function of index()
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
# Logout-user
# Sign-up user



