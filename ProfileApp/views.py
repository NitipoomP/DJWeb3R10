# Create your views here.
from django.shortcuts import render, HttpResponse

# Create your views here.
def test(request):
    return HttpResponse("<H1> Hello World </H1>")

def firstWeb(request):
    return render(request,"FirstWeb.html")

def secondpage (request):
    return render(request,'secondpage.html')

def thridpage (request):
    return render(request,'thridpage.html')