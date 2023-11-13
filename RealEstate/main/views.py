from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
def home_page(request : HttpRequest):
    return render(request,'main/home.html')

def about_page(request : HttpRequest):
    return render(request,'main/about.html')

def large_size_view(requset: HttpRequest):
    response = redirect("main:about_page")
    response.set_cookie("size", "large")
    return response

def small_size_view(requset: HttpRequest):
    response = redirect("main:about_page")
    response.set_cookie("size", "small")
    return response