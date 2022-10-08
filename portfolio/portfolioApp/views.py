from django.shortcuts import render

# HomeView function of index()
def index(request):
    title= 'Welcome to My Portfolio'
    return render(request,'portfolioApp/template/index.html',
    context={'title':title})

# Mapping userProfile to map 
def mapDetails(request):
    title = "Screen Map Details"
    return render(request,'portfolioApp/template/map/mapDetail.html',
    context={'title'