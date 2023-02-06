# Create your views here.
from urllib import request
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django import forms
from ProfileApp.models import *
from ProfileApp.forms import *
from django.views.decorators.csrf import requires_csrf_token




def test(request):
    return HttpResponse("<H1> Hello World </H1>")

def firstWeb(request):
    return render(request,"FirstWeb.html")

def personalRecord(request):
    return render(request, "personalRecord.html")

def secondpage (request):
    return render(request,'secondpage.html')

def thridpage (request):
    return render(request,'thridpage.html')

def productsForSale (request):
    return render(request, "productsForSale.html")

def roleModel (request):
    return render(request, "roleModel.html")

def showMyData (request):
    IdName = "65342310149-4"
    name  = "Ntitpoom Maharhong"
    address = "12/36 ถนนเมวาภิบาล ตำบลในเมือง อำเภอเมือง จังหวัดร้อยเอ็ด 45000"
    height = "160 ซม."
    favoriteColors = "Black with red edges"
    favoriteFood = "แพนงหมู"
    gender = "Male"
    status = "นักศึกษา"
    work = "ธุรกิจส่วนตัว"
    education = "ราชมงคลอีสานวิทยาเขตขอนแก่น"
    return render(request, 'showMyData.html',
    {'IdName': IdName, 'name': name, 'address': address, 'height': height, 'favoriteColors': favoriteColors, 'favoriteFood': favoriteFood,
      'gender': gender, 'status': status, 'work': work, 'education': education})


productList = []
def showProduct (request):

    context = {'products': productList}
    return render(request, 'showProduct.html', context)

#CRUD
def retrieveAllProduct(request):
    # categories = Category.objects.all()
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'products/retrieveAllProduct.html', context)

def reteieveOneProduct(request, pid):
    product = Product.objects.get(pid=pid)
    context = {'product': product}
    return render(request, 'products/reteieveOneProduct.html', context)

# def retrieveOneCat(request, id):
#     products = Product.filter(category_id = id)

from django.contrib import messages
def createProduct(request):
    if request.method == "POST":
        form = ProductMForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'บันทึกข้อมูลสินค้าใหม่เรียบร้อย......')
            return redirect("retrieveAllProduct")
        else: #ข้อมูลมีปัญหา
            product = Product.objects.get(pid=request.POST['pid'])
            if product:
                messages.add_message(request, messages.WARNING, 'รหัสสินค้าซ้ากันในระบบ......')
                return redirect("retrieveAllProduct")
            else:
                messages.add_message(request, messages.WARNING, 'ไม่สามารถบันทึกข้อมูลสินค้าได้......')
                return redirect("retrieveAllProduct")
    else:
        form = ProductMForm()
    context = {'form': form}
    return render(request, 'products/createProduct.html', context)

from ProfileApp import models
lstOutProduct =[]
def listProduct(request):
    context = {'product': lstOutProduct}
    return render(request, 'listProduct.html', context)

def inputProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            id = form.get("id")
            name = form.get("name")
            brand = form.get("brand")
            price = form.get("price")
            amount = form.get("amount")
            made = form.get("made")
            total = price * amount
            if amount < 3:
                discount = 0.00
            elif amount <= 5:
                discount = total * 0.05
            else:
                discount = total * 0.10
            net = total - discount
            product = Mproduct(id,name, brand, price, amount,made, total, discount, net)
            lstOutProduct.append(product)
            return redirect('listProduct')
        else:
            form = ProductForm(form)
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'inputProduct.html', context)

def updateProduct(requsetm, pid):
    product = get_object_or_404(Product, pid=pid)
    form = ProductMForm(data=request.POST or None, instance=product)

    if request.method == 'POST' :
        if form.is_valid():
            form.save()
        else:
            pass

    else:
        context = {'form':form}
        return render(request, 'products/updateProduct.html', context)
