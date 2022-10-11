from django.urls import path
from . import views

urlpatterns = [
    path('login-user/', views.loginView, name='loginView'),
    path('sign-out/', views.signOut, name='signOut'),
    path('sign-up/', views.signUp, name='signUp'),


]
