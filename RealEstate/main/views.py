from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home_views(request:HttpRequest):

    return render(request , 'main/home.html')

def about_viwes(request:HttpRequest):
    return render(request , 'main/about.html')


def zoom_in(requset: HttpRequest):

    response = redirect("main:about_viwes")
    response.set_cookie("mode", "zoom_in")

    return response

def zoom_out(requset: HttpRequest):

    response = redirect("main:about_viwes")
    response.set_cookie("mode", "zoom_out")

    return response

