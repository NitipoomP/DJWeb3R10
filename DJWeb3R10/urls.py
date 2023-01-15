from django.contrib import admin
from django.urls import path
from ProfileApp import views

urlpatterns = [
    path('', views.firstWeb),
    path('test', views.test, name="test"),
    path('firstWeb', views.firstWeb, name="firstWeb"),
    path('secondpage', views.secondpage, name="secondpage"),
    path('thridpage', views.thridpage, name="thridpage"),
]
