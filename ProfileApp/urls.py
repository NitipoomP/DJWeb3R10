from django.urls import path
from ProfileApp import views

urlpatterns = [
    path('', views.firstWeb),
    path('firstWeb', views.firstWeb, name="firstWeb"),
    path('personalRecord', views.personalRecord, name="personalRecord"),
    path('secondpage', views.secondpage, name="secondpage"),
    path('thridpage', views.thridpage, name="thridpage"),
    path('productsForSale', views.productsForSale, name="productsForSale"),
    path('roleModel', views.roleModel, name="roleModel"),
    path('showMyData', views.showMyData, name="showMyData"),
    path('showProduct', views.showProduct, name="showProduct"),
    path('listProduct', views.listProduct, name="listProduct"),
    path('inputProduct', views.inputProduct, name="inputProduct"),

    path('retrieveAllProduct', views.retrieveAllProduct, name="retrieveAllProduct"),
    path('reteieveOneProduct/<pid>', views.reteieveOneProduct, name="reteieveOneProduct"),
    path('createProduct', views.createProduct, name="createProduct"),
    path('updateProduct/<pid>', views.updateProduct, name="updateProduct"),


]
