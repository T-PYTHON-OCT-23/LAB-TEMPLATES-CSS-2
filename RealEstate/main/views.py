from django.shortcuts import render ,resolve_url
from django.http import HttpRequest, HttpResponse

def home_view(request:HttpRequest):
    return render(request, 'main/home.html')

# Create your views here.
