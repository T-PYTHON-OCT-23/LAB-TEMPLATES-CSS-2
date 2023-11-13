
from django.shortcuts import render, resolve_url , redirect
from django.http import HttpRequest, HttpResponse
from django.utils.crypto import get_random_string
# Create your views here.



def home_view(request:HttpRequest):

    
    return render(request, 'main1/home.html')


def another_view(request:HttpRequest):

    
    return render(request, 'main1/another.html')

 #getting the cookies
    print(request.COOKIES["mode"])

    return render(request, "main1/another.html")


def another_view(request: HttpRequest):

    return render(request, "main1/another.html")


def small_mode_view(requset: HttpRequest):

    response = redirect("main1:another_view")
    response.set_cookie("mode", "small")

    return response


def big_mode_view(requset: HttpRequest):

    response = redirect("main1:another_view")
    response.set_cookie("mode", "big")

    return response