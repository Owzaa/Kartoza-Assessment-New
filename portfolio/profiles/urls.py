from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('profile-Details/', views.profileDetails, name='profileDetails'),
    path('edit-Profile/', views.editProfile, name='editProfile'),

]
