from django.shortcuts import render,redirect
from django.http import HttpRequest
# Create your views here.


def index(request:HttpRequest):

    return render(request,'main/index.html')

def about(request:HttpRequest):

    return render(request,'main/about.html')

def large_font(request:HttpRequest):

    response = redirect('main:home')
    response.set_cookie('font','large')
    return response

def small_font(request:HttpRequest):

    response= redirect('main:home')
    response.set_cookie('font','small')
    return response