# Create your views here.
from django.shortcuts import render, HttpResponse

# Create your views here.
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