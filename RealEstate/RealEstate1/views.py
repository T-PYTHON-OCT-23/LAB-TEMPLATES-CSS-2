from django.shortcuts import render, redirect

from django.http import HttpRequest, HttpResponse

def homePage(request : HttpRequest):
    
    return render(request ,"RealEstate1/home.html")

def aboutPage(request : HttpRequest):
    
    return render(request ,"RealEstate1/about.html")

def large_size_view(request: HttpRequest):

    response = redirect("RealEstate1:about")
    response.set_cookie("size", "large")
    
    
    return response 


def small_size_view(request: HttpRequest):

    response = redirect("RealEstate1:about")
    response.set_cookie("size", "small")
   

    return response 
