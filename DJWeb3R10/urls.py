from django.contrib import admin
from django.urls import path, include
from ProfileApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.firstWeb, name='firstWeb'),
    path('ProfileApp/', include('ProfileApp.urls')),
]
