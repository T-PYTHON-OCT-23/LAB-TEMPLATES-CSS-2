from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.utils.crypto import get_random_string

# Create your views here.
def RealEstate_view(request : HttpRequest):
    reale_estate=[

    ]

    return render(request, 'main/RealEstate.html',context={"RealEstate":reale_estate})