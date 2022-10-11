from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('logout/', views.signOut, name='logout'),
    path('sign-up/', views.signUp, name='signUp'),


]
