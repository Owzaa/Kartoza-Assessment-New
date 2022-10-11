from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.signOut, name='logout'),
    path('sign-up/', views.signUp, name='signUp'),


]
