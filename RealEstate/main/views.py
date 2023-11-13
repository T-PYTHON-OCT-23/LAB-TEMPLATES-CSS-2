from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse

def home_view(request:HttpRequest):
    print(request.COOKIES["fontsize"])
       
    return render(request, 'main/home.html')


def about_view(request: HttpRequest):

    return render(request, "main/about.html")

def large_view(requset: HttpRequest):

    response = redirect("main:about_view")
    response.set_cookie("fontsize", "large")

    return response

def small_view(requset: HttpRequest):

    response = redirect("main:about_view")
    response.set_cookie("fontsize", "small")

    return response
# Create your views here.
