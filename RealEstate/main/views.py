from django.shortcuts import render, redirect
from django.http import HttpRequest
# Create your views here.

def home_page_view(request:HttpRequest):

    return render(request,'main/home.html')

def about_page_view(request:HttpRequest):

    return render(request,'main/about.html')

def contract_page_view(request:HttpRequest):

    return render(request,'main/contract.html')

def properties_page_view(request:HttpRequest):

    return render(request, 'main/properties.html')

def service_page_view(request:HttpRequest):

    return render(request, 'main/service.html')

def small_page_redirictor(request:HttpRequest):
    
    responce = redirect('main:home_page_view')
    responce.set_cookie("font_is_small","False")

    return responce

def larg_page_redirictor(request:HttpRequest):

    responce = redirect('main:home_page_view')
    responce.set_cookie('font_is_small',"True")

    return responce