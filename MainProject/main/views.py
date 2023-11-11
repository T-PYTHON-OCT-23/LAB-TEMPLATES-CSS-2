from django.shortcuts import render
from django.http import HttpRequest, HttpResponse



def main_view(request :HttpRequest):
      
      return render(request, "main/main.html" )

def home_view(request :HttpRequest):
      
      return render(request, "main/home.html" )

def properites_view(request :HttpRequest):
      
      return render(request, "main/properites.html" )


def services_view(request :HttpRequest):
      
      return render(request, "main/services.html" )

def about_view(request :HttpRequest):
      
      return render(request, "main/about.html" )

def contact_view(request :HttpRequest):
      
      return render(request, "main/contact.html" )


