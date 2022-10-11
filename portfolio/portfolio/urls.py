"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from portfolioApp.views import homeView,login,signOut,signUp,mapDetails
from profiles.views import profileDetails,editProfile
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='home'),
    path('login/',login, name='login'),
    path('sign-out/',signOut,name='logout'),
    path('sign-up/',signUp,name='signUp'),
    path('all-profiles/',mapDetails,name='mapDetails'),
    path('profile-details/',profileDetails, name="profileDetails"),
    path('edit-profile/',editProfile, name="ëditProfile"),
]
