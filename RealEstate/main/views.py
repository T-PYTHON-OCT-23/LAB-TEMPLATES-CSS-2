from django.shortcuts import render , redirect
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



def about(request: HttpRequest):

    return render(request, "main/about.html")


def large_view(requset: HttpRequest):

    response = redirect("main:about")
    response.set_cookie("size", "large")

    return response


def small_view(requset: HttpRequest):

    response = redirect("main:about")
    response.set_cookie("size", "small")

    return response