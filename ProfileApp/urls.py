from django.urls import path
from ProfileApp import views

urlpatterns = [
    path('', views.firstWeb),
    path('firstWeb', views.firstWeb, name="firstWeb"),
    path('secondpage', views.secondpage, name="secondpage"),
    path('thridpage', views.thridpage, name="thridpage"),
    path('HappyNewYear', views.thridpage, name="Hny"),
    path('showMyData', views.showMyData, name="showMyData"),

]
