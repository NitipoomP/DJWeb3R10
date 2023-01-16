from django.contrib import admin
from django.urls import path, include
from ProfileApp import views

urlpatterns = [
    path('', views.firstWeb),
    path('ProfileApp/', include('ProfileApp.urls')),
]
