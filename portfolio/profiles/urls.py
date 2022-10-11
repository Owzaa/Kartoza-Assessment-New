from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('profileDetails/', views.profileDetails, name='profileDetails'),
    path('profileDetails/{{pk=+id}}', views.profileDetails, name='profileDetails'),

    path('editProfile/', views.editProfile, name='editProfile'),
    path('profileDetails/', views.profileDetails, name='profileDetails'),

]
