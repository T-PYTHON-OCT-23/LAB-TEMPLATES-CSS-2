from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home_view(request: HttpRequest):

    return render(request, "main/index.html")
def about_view(request: HttpRequest):

    return render(request, "main/about.html")


def font_large_view(requset: HttpRequest):

    response = redirect("main:home_view")
    response.set_cookie("font", "large")

    return response


def font_small_view(requset: HttpRequest):

    response = redirect("main:home_view")
    response.set_cookie("font", "small")

    return response