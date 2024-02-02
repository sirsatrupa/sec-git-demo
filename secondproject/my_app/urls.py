from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    # path('index/', views.index),
    path('home/', views.home),
    path('createbatch/', views.createbatch, name='create'),
    path('showbatch/', views.showbatch, name='show'),
    path('signup/', views.signup, name='register'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
]