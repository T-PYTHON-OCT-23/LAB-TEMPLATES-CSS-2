from django.shortcuts import render
from django.http import HttpRequest, HttpResponse 
# Create your views here.

def home(request : HttpRequest):

    return render(request, "main/home.html")


def properties(request : HttpRequest):
    return render(request,"main/properties.html")

def service(request : HttpRequest):
    return render(request,"main/service.html")


def about(request : HttpRequest):
    return render(request,"main/about.html")


