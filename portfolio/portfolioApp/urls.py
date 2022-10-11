from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homeView, name='homeView'),
    path('login/', views.loginView, name='loginView'),

]
