
from django.shortcuts import render, resolve_url
from django.http import HttpRequest, HttpResponse
from django.utils.crypto import get_random_string
# Create your views here.




def home_view(request:HttpRequest):

    
    return render(request, 'main1/home.html')

def base_view(request:HttpRequest):

    
    return render(request, 'main1/base.html')