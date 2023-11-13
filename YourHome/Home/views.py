from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, response

# Create your views here.


def home(request: HttpRequest):
    return render(request, 'Home/home.html')


def about(request: HttpRequest):
    response = render(request, 'Home/home.html')


def large_size(request: HttpRequest):

    response = redirect("main:about.viwes")
    response.set_cookie("size", "large")
    return response


def small_size(request: HttpRequest):

    response = redirect("main:about.viwes")
    response.set_cookie("size", "small")
    return response
