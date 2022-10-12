from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('user-profile/', views.profileDetails, name='profile'),
    path('edit-profile/', views.editProfile, name='EditProfile'),

]
