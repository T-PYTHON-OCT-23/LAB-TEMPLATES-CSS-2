from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse

# Create your views here.

def home_views(request : HttpRequest):
 
    return render ( request , "main/home.html"  )




def about_views(request : HttpRequest):
 
    return render ( request , "main/about.html"  )




def large_size(request : HttpRequest):
    response = redirect("main/about.html")
    response.set_cookie("font" , "large")
    return response


def small_size(request : HttpRequest):
    response = redirect( "main/about.html")
    response.set_cookie("font" , "small")
    return response