from django.shortcuts import render
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