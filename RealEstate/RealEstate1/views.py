from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

def homePage(request : HttpRequest):
    
    return render(request ,"RealEstate1/home.html")
