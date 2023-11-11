from django.shortcuts import render
from django.http import HttpRequest , HttpResponse

# Create your views here.
def home_page_view(request : HttpRequest):
    return render(request,"main/homepage.html")

def propertes_page_view(request : HttpRequest):
    return render(request,"main/propertespage.html")

def service_page_view(request : HttpRequest):
    return render(request,"main/servicepage.html")

def about_page_view(request : HttpRequest):
    return render(request,"main/aboutpage.html")

def contacts_page_view(request : HttpRequest):
    return render(request,"main/contactspage.html")